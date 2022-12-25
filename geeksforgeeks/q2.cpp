#include<iostream>
#include <vector>
using namespace std;

int main()
{

    ios_base ::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n , x , y ;
    cin >> n >> x >> y ;
    vector<int> nums;
    int  p ;

    while (n) {
        cin >> p ; 
        nums.push_back(p);
        n-- ; 
    }

    int i = 0 ;
    int j ;
    int c ; 
    while ( i < nums.size()) {
        // cout << nums[i] ; 
        j = i + 1;
        while (j < nums.size()) {
            if (x <= nums[i]*nums[j] <= y) {
                c++; 
            }
            j++;
        }
        i++ ; 

    }
    cout << c ; 
}