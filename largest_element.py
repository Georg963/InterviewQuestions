#Program to find largest element in an array
def find_le(x: list):

    for i in range(len(x)-1):
        le = x[i]
        if x[i] < x[i+1]:
            le = x[i+1]
    
    return le

print(find_le([1,2,3,4,9])) #9