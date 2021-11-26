# find all pairs in array of integers whose sum is equal to given number
def find_sum_eq_num(x: list, k: int) -> list:
    pairs = []

    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if(x[i] + x[j] == k):
                pairs.append([x[i], x[j]])
    
    return pairs

x = [0,1,2,3,4,5,6,7,8,9,10]
k = 9
print(find_sum_eq_num(x, k))
