from mpi4py import MPI
import numpy as np

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        # Generate random array on rank 0
        arr = np.random.randint(0, 100, 16)
        print("Original array on rank 0:", arr)
        # Compute the chunk sizes for Scatterv and Gatherv
        chunk_sizes = [len(arr) // size] * size
        chunk_sizes[0] += len(arr) % size
        displs = [sum(chunk_sizes[:i]) for i in range(size)]
    else:
        arr = None
        chunk_sizes = None
        displs = None

    # Broadcast the chunk sizes and displacements to all ranks
    chunk_sizes = comm.bcast(chunk_sizes, root=0)
    displs = comm.bcast(displs, root=0)

    # Prepare the receive buffer for Scatterv
    recv_buf = np.empty(chunk_sizes[rank], dtype=np.int32)

    # Scatterv the array to all ranks
    comm.Scatterv([arr, chunk_sizes, displs, MPI.INT], recv_buf, root=0)

    # Perform local quick sort
    recv_buf = quick_sort(recv_buf)

    # Gather the sorted arrays on rank 0
    sorted_arr = None
    if rank == 0:
        sorted_arr = np.empty(sum(chunk_sizes), dtype=np.int32)
    comm.Gatherv(recv_buf, [sorted_arr, chunk_sizes, displs, MPI.INT], root=0)

    if rank == 0:
        # Print the sorted array on rank 0
        print("Sorted array on rank 0:", sorted_arr)
