def removeSpaces(s: str) -> str:
    s = list(s)
    for i in range(len(s)-1):
        if i == 0 and s[i] == ' ':
            s[i] = ''
        elif i != 0 and s[i] == ' ' and (s[i+1] in ['.', '!', '?', '-', ':', '=', ' ']):
            s[i] = ''
        else:
            continue
    return ''.join(s)

if __name__ == "__main__":
    string_1 = " Hello .   This is   a Python   program !! "
    print(removeSpaces(string_1)) #Hello. This is a Python program!!