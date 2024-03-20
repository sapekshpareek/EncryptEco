import algo
import text


def decrypt_main(encodedtext, key, data):
    encodedtext = bytes.fromhex(encodedtext)
    key = bytes.fromhex(key)
    decrypted_data = algo.decrypt_AES(encodedtext, key)
    decrypted_data = decrypted_data.decode()
    decrypted_data = text.convert(decrypted_data)
    values = list(data.values())
    keys = list(data.keys())
    for i in range(len(decrypted_data)):
        if decrypted_data[i] in data.values():
            position = values.index(str(decrypted_data[i]))
            decrypted_data[i] = keys[position]
    decrypted_data = " ".join(decrypted_data)
    with open('input.txt', 'w') as f:
        f.write(decrypted_data)
