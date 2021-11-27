# Find the maximum product of two integers in an array
def maxProd(x: list) -> tuple:
    maxProduct = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] * x[j] > maxProduct:
                maxProduct = x[i] * x[j]
                maxI, maxJ = i, j
    
    return x[maxI], x[maxJ]
    pass


if __name__ == '__main__':
    arr = [2,6,8,1,9,3,30]
    print(maxProd(arr)) #(9, 30)