'''
right-rotate an array by specified positions. 
For example, right rotating array { 1, 2, 3, 4, 5, 6, 7 } three times will result in array { 5, 6, 7, 1, 2, 3, 4 }.
'''

def rightRotate(x: list, k: int) -> list:
    new_arr = x[k+1:]
    for i in range(0, k+1):
        new_arr.append(x[i])

    return new_arr

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    k = 3
    print(rightRotate(arr, k)) #[5, 6, 7, 1, 2, 3, 4]