'''
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3 ** x.
'''
import math

# solution approach
# 3 ** x = 81
# x * log(3) = log(81)
# x = log(81)/log(3) = 4
def powerOf3(n: int) -> bool:
    x = math.log(n) / math.log(3)
    return True if 3 ** x == n else False


if __name__ == "__main__":
    print(powerOf3(27))  #True
    print(powerOf3(81))  #True
    print(powerOf3(100)) #False