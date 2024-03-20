import algo
from Crypto.Random import get_random_bytes
def encrypt_main(lst, data):
    for i in range(len(lst)):
        if lst[i] in data.keys():
            lst[i] = data.get(lst[i])
    key = get_random_bytes(32)
    print("\nKey:", key.hex())
    text = " ".join(lst)
    plaintext = text.encode()
    encrypted_data = algo.encrypt_AES(plaintext, key).hex()
    size = str(encrypted_data)
    print('\nLength of THe Encrypted Data: ', len(size))
    with open('output.txt', 'w') as f:
        f.write(encrypted_data)
