# Find the number of 1’s in a sorted binary array
def counts(x: list) -> int:
    counter = 0
    for i in x:
        if i:
            counter+=1
    
    if counter:
        return counter
    return 0

if __name__ == "__main__":
    arr = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
    print(counts(arr))