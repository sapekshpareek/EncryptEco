a = "Sapeksh Pareek Sarthak Nagar Shivansh Bhatnagar"
b = "Sarthak Nagar"
c = "Shivansh Bhatnagar"
d = "Nimit Agrawal"

lst = []


def convert(string):
    li = list(string.split(" "))
    # return li
    for i in li:
        lst.append(i)
        # print(i)

convert(a)

def new(lst):
    for i in lst:
        print(i)
        # print (i.find_all('a'))
        if( 'a' in i):
            print('hi')
        # for j in i:
        #     if(j == 'a'):
        #         print('hi')

new(lst)

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

find_all('spam spam spam spam', 'am') # [0, 5, 10, 15]