'''
Given an integer n, return the number of prime numbers that are strictly less than n.
'''
def count(n: int) -> int:
    count = 0
    for i in range(2, n):
        Flag = True
        for j in range(2, i):
            if i%j == 0:
                Flag = False
                break
        if Flag:
            count += 1

    return count

if __name__ == "__main__":
    print(count(0))  #0
    print(count(1))  #0
    print(count(10)) #4
    print(count(20)) #8