votes = (
    "john,johnny,jackie,johnny,john,jackie,jamie,jamie,john,johnny,jamie,johnny,john"
)


votes = list(votes.rstrip().split(","))
print(votes)


hash1 = {}


for candi in votes:
    if candi in hash1.keys():
        hash1[candi] += 1
    else:
        hash1[candi] = 1

# print(hash1)


mv = hash1[list(hash1.keys())[2]]


for k in hash1.keys():
    if hash1[k] > mv:
        mv = hash1[k]

# print(mv)

for k in hash1.keys():
    if hash1[k] == mv:
        print(k, mv)
        break
