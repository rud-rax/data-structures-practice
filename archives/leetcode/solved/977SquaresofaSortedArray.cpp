#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int>, int, int);
void quickSort(vector<int>, int, int);

int main()
{

    ios_base ::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    vector<int> nums = {0, -1, 10, 3, -4};
    quickSort(nums, 0, nums.size() - 1);

    for (auto &i : nums)
    {
        cout << i << " ";
    }
}

int partition(vector<int> nums, int l, int h)
{
    int i = l, j = l + 1;
    int temp;

    while (j <= h)
    {
        if (nums[l] > nums[j])
        {
            i += 1;
            // temp = nums[i];
            // nums[i] = nums[j];
            // nums[j] = temp;

            swap(nums[i], nums[j]);
        }
        j += 1;
    }

    // temp = nums[l];
    // nums[l] = nums[i];
    // nums[i] = temp;

    swap(nums[l], nums[i]);

    return i;
}

void quickSort(vector<int> nums, int l, int h)
{
    if (l < h)
    {
        int i = partition(nums, l, h);
        quickSort(nums, l, i - 1);
        quickSort(nums, i + 1, h);
    }
}