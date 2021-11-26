# Given an array of integers and an integer k where k is smaller than size of array, we need to find the k’th smallest element in the given array.

def Kth_smallest(x: list, k: int) -> int:

    if k >= len(x):
        return None
    elif k == 1:
        return min(x)
    else:
        x.sort()
        return x[k-1]

print(Kth_smallest([18,12,34,41,56,60,17], 3)) #18
