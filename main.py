import json
import text
import encryption

data = text.read('data.txt')
data = json.loads(data)

input = text.read('input.txt')
input = input.lower()
print(input)

encryption.encrypt(text.convert(input), data)
