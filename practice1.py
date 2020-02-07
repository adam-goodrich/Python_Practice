def min_num_taxis(*requests):
    args = []
    pu_do = []
    taxis = 0
    for i in requests:
        args.append(i) 
    for i in args:
        pu = i[0]
        do = i[-1]
        pu_do.append(pu)
        pu_do.append(do)
    return pu_do
print(min_num_taxis((1,4), (2, 9), (3, 6)))
