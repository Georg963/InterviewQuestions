'''
left-rotate an array by specified positions. 
For example, left-rotating array { 1, 2, 3, 4, 5 } twice results in array { 3, 4, 5, 1, 2 }.
'''
def leftRotate(x: list, k:int) -> list:
    new_arr = x[k:]
    for i in range(k):
        new_arr.append(x[i])
    return new_arr


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    k = 3
    print(leftRotate(arr, k)) #[4, 5, 6, 7, 1, 2, 3]