'''
Removing Minimum and Maximum From Array
%%
Input: nums = [2,10,7,5,4,1,8,6]
Output: 5
Explanation: 
The minimum element in the array is nums[5], which is 1.
The maximum element in the array is nums[1], which is 10.
We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
This results in 2 + 3 = 5 deletions, which is the minimum number possible
'''

def numOfDeletions(x: list[int]) -> int:
    minNum = min(x)
    maxNum = max(x)

    if len(x) != 1:
        for i in range(len(x)):
            if x[i] == minNum:
                ind_min = i
            elif x[i] == maxNum:
                ind_max = i
        
        deletions_min_back = 0
        deletions_min_front = 0
        if len(x[:ind_min+1]) > len(x[ind_min:]):
            deletions_min_back = len(x[ind_min:])
        elif x[:ind_min+1] < x[ind_min:]:
            deletions_min_front = len(x[:ind_min+1])
        
        deletions_max_back = 0
        deletions_max_front = 0
        if maxNum in x:
            if x[:ind_max+1] > x[ind_max:]:
                deletions_max_back = len(x[ind_max:])
            elif x[:ind_max+1] < x[ind_max:]:
                deletions_max_front = len(x[:ind_max+1])
                
        return deletions_min_back + deletions_min_front + deletions_max_back + deletions_max_front

    return 1

if __name__ == "__main__":
    print(numOfDeletions([2,10,7,5,4,1,8,6]))       #5
    print(numOfDeletions([0,-4,19,1,8,-2,-3,5]))    #3
    print(numOfDeletions([101]))                    #1
    