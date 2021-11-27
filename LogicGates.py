# Logic Gates in Python

# The AND gate gives an output of 1 if both the two inputs are 1, it gives 0 otherwise
def AND(x: int, y: int) -> int:
    if x == 1 and y == 1:
        return 1
    return 0

# The OR gate gives an output of 1 if either of the two inputs are 1, it gives 0 otherwise
def OR(x: int, y: int) -> int:
    if x == 1 or y == 1:
        return 1
    return 0
# It acts as an inverter. It takes only one input. If the input is given as 1, it will invert the result as 0 and vice-versa
def NOT(x: int) -> int:
    if x == 1:
        return 0
    return 1

# The XOR gate gives an output of 1 if either of the inputs is different, it gives 0 if they are the same
def XOR(x: int, y: int) -> int:
    if x != y:
        return 1
    return 0


if __name__ == "__main__":
    x=1
    y=0
    print(AND(x, y)) #AND. output: 0
    print(OR(x, y)) #OR. output: 1
    print(NOT(x)) #NOT. output: 0
    print(NOT(AND(x,y))) #NAND is not AND: The NAND gate (negated AND) gives an output of 0 if both inputs are 1, it gives 1 otherwise. output: 1
    print(NOT(OR(x,y))) #NOR is not OR: The NOR gate (negated OR) gives an output of 1 if both inputs are 0, it gives 1 otherwise. output: 0
    print(XOR(x,y))#XOR. output: 1
    print(OR(AND(x, NOT(y)), AND(NOT(x), y))) #XOR with (and, or, not).  xor=xy' + x'y. output: 1
    print(NOT(XOR(x, y)))#The XNOR gate (negated XOR - not XOR) gives an output of 1 both inputs are same and 0 if both are different. output: 0