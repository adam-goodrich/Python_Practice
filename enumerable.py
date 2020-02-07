def take(arr,n):
    my_list = []
    for i in arr[:n]:
        my_list.append(i)
    return my_list

print(take([0, 1, 2, 3, 5, 8, 13], 3))