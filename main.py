import json
import text
import data
import encryption

dataf = text.read('data.txt')
dataf = json.loads(dataf)

input = text.read('input.txt').lower()
print(input)

# chrr = []
# dict1 = {}
# data.write(chrr, dict1)


encryption.encrypt(text.convert(input), dataf)
