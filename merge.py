#Given k sorted arrays of size n each, merge them and print the sorted output.
def merge(x: list, y: list) -> list:
    merged_list = x + y

    for i in range(len(merged_list)):
        for j in range(i+1, len(merged_list)):
            if(merged_list[i]>merged_list[j]):
                merged_list[i], merged_list[j] = merged_list[j], merged_list[i]
    
    return merged_list
    


array_1 = [1, 3, 5, 7]
array_2 = [2, 4, 6, 8]
array_3 = [0, 9, 10, 11]
merged_array = merge(merge(array_1, array_2), array_3)
print(merged_array) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
