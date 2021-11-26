#Python program to remove character from string
def remove_char(x: str, c: str) -> str:
    x = list(x)
    new_x = []

    for i in range(len(x)):
        if(x[i] != c):
            new_x.append(x[i])
    
    return ''.join(new_x)

#Using replace() method
def remove_char2(x: str, c: str) -> str:
    return x.replace(c, '')

word = 'abcdefghij'

char = 'j'
word_without_j = remove_char(word, char)
print(word_without_j) #abcdefghi

char2 = 'i'
word_without_i = remove_char2(word_without_j, char2)
print(word_without_i) #abcdefgh
