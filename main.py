import text

a = "Sapeksh Pareek Sarthak Nagar Shivansh Bhatnagar"
print(a)
b = "Sarthak Nagar"
dict = {"Sarthak": "sar", "Nagar": "nag"}
d = "Nimit Agrawal"
lst = text.convert(a)
# print(lst)
# wrd = text.convert(b)
# print(lst)
# print(wrd)

# index = text.finder(a, "a")
# print(index)

# for i in lst:
#     if i in wrd:
#         print("Yes")
#     else:
#         print("NO")

# print(str(dict))

for i in range(len(lst)):
    if lst[i] in dict.keys():
        lst[i] = dict.get(lst[i])
# print(lst)
str = " "
print(str.join(lst))