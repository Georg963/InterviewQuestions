'''
rotate an array by specified positions. 
'''
def rotate(x: list, k:int) -> list:
    new_arr = x[k:]
    for i in range(k):
        new_arr.append(x[i])
    return new_arr


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    k = 3
    print(rotate(arr, k)) #[4, 5, 6, 7, 1, 2, 3]