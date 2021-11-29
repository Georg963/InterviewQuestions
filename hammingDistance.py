'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.
'''
def hd(x: int, y:int) -> int:
    x_bin = format(x, "b")
    y_bin = format(y, "b")
    count = 0

    if len(x_bin) != len(y_bin):
        if len(x_bin) > len(y_bin):
            y_bin = str(y_bin).zfill(len(x_bin))
        else:
            x_bin = str(x_bin).zfill(len(y_bin))
    
    for i, j in zip(x_bin, y_bin):
        if i != j:
            count += 1
        else:
            continue
    
    return count

if __name__ == "__main__":
    print(hd(2, 15))