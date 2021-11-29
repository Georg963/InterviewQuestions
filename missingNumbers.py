'''
Given an array nums containing n distinct numbers in the range [0, n]
return the only number in the range that is missing from the array.
'''
def missingNums(x: list[int]) -> int:
    n = len(x)
    new_x = list(range(0, n+1))
    for i in new_x:
        if i not in x:
            return i
    return None

if __name__ == "__main__":
    print(missingNums([0,1,3]))         #2
    print(missingNums([1,2,3,4,5,6,7])) #0
    print(missingNums([0,1,2,3,4,5,7])) #6