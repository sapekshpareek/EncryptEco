def encrypt(lst, data):
    for i in range(len(lst)):
        if lst[i] in data.keys():
            lst[i] = data.get(lst[i])
    print(" ".join(lst))
