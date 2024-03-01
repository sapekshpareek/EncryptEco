def encrypt(lst, data):
    for i in range(len(lst)):
        if lst[i] in data.keys():
            lst[i] = data.get(lst[i])
    with open('output.txt', 'w') as f:
        f.write(" ".join(lst))
