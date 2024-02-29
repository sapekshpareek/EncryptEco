import json
import string
import text

def dictcont(dict1, chrr):
    input = text.read('sample.txt')
    input = input.lower()
    input = text.convert(input)

    for i in range(len(input)):
        dict1[input[i]] = chrr[i]

    with open('data.txt', 'w') as f:
        f.write(json.dumps(dict1))


def write(chrr, dict1):

    for char in string.ascii_lowercase:
        a = char
        for ch in string.ascii_lowercase:
            b = a + ch
            for ar in string.ascii_lowercase:
                c = b + ar
                chrr.append(str(c))
    dictcont(dict1, chrr)

