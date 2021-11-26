import numpy as np

def firstRecurringChar_1(x: str) -> str:
    char_list = list(x)
    length_char = len(char_list)
    ind_list = []

    for i in range(length_char):
        for j in range(i+1, length_char):
            if(char_list[i]==char_list[j]):
                ind_list.append([i, j])

    if(len(ind_list) != 0):
        np_list = np.array(ind_list)
        Indexes = np_list[min(np_list[:, 1])-1,:]
        return char_list[Indexes[0]]
    
    return None

# using dictionary
def firstRecurringChar_2(x: str) -> str:
    char_list = list(x)
    length_char = len(char_list)
    dict_1 = {}

    for i in range(length_char):
        if(char_list[i] in dict_1.keys()):
            return char_list[i]
        else:
            dict_1[char_list[i]] = 1

    return None

chars = "QAEEAECBRDUEQIOB"
print(firstRecurringChar_1(chars)) #E
print(firstRecurringChar_2(chars)) #E