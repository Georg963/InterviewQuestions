# print prime numbers between 100 and 200
def prime_nums() -> list:
    num_list = []

    for i in range(100, 201):
        if(i%2 != 0):
            num_list.append(i)
    
    return num_list

print(prime_nums())