# Reverse an array in groups of given size

def rev(x: list, k: int) -> list:
    subArray_k = x[:k]
    subArray_rest = x[k:]

    reversed_subArray_k = subArray_k[::-1]
    return reversed_subArray_k + subArray_rest

arr = [1,2,3,4,5,6,7]

num = 2
print(rev(arr, num)) #[2, 1, 3, 4, 5, 6, 7]

num = 3
print(rev(arr, num)) #[3, 2, 1, 4, 5, 6, 7]