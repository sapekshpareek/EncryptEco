import text

a = "Sapeksh Pareek Sarthak Nagar Shivansh Bhatnagar"
b = "Sarthak Nagar"
c = "Shivansh"
d = "Nimit Agrawal"

lst = text.convert(a)
# print(lst)

index = text.finder(a, "a")
print(index)

test = []
for i in index:
    z = i+1
    test.append(z)
print(test)


