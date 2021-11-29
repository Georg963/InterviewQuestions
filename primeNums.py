# print prime numbers between x and y
def prime_nums(x: int, y: int) -> list:
    num_list = []

    for i in range(x, y):
        Flag = True
        for j in range(2, i):
            if i%j == 0:
                Flag = False
                break
        if Flag:
            num_list.append(i)
    
    return num_list

if __name__ == "__main__":
    print(prime_nums(100, 200))
    #[101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]