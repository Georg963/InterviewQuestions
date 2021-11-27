# Move all zeros present in an array to the end
def moveZeros1(x: list) -> list:
    for i in range(len(x)):
        if x[i] == 0:
            x.remove(0)
            x.append(0)
    return x

def moveZeros2(x: list) -> list:
    k = 0
    for i in x:
        if i:
            x[k] = i
            k = k + 1
    for i in range(k, len(x)):
        x[i] = 0
    return x

if __name__ == "__main__":
    arr = [0,5,3,2,0,8,9,14,0,22,0,0,65,89,0,1]
    print(moveZeros1(arr)) #[5, 3, 2, 8, 9, 14, 22, 65, 89, 1, 0, 0, 0, 0, 0, 0]
    print(moveZeros2(arr)) #[5, 3, 2, 8, 9, 14, 22, 65, 89, 1, 0, 0, 0, 0, 0, 0]
