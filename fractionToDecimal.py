'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format. Output: "x.x".
If the fractional part is repeating, enclose the repeating part in parentheses.
'''
def ftd(numerator: int, denominator: int) -> str:
    fraction = numerator/denominator
    fraction = list(str(fraction))

    for i in range(len(fraction)):
        if fraction[i] == '.':
            ind_1 = i+1
            break
    
    Flag = False
    for i in range(ind_1, len(fraction)):
        ac = fraction[i:]
        if i != len(fraction)-1 and len(set(ac)) == 1:
            ind_2 = i
            Flag = True
            break
    
    if Flag:
        fraction = fraction[:ind_2+1]
        ele = fraction[ind_2]
        fraction[ind_2] = '('
        fraction.append(ele)
        fraction.append(')')

    return '"{}"'.format(''.join(fraction))

if __name__ == "__main__":
    print(ftd(2, 3)) # = 0.66666666666 - Output: "0.(6)"
    print(ftd(2, 5)) # = 0.4 - Output: "0.4"
    print(ftd(2, 7)) # = 0.2857142857142857 - Output: "0.2857142857142857"

