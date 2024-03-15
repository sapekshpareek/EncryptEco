import algo
from Crypto.Random import get_random_bytes
def encrypt_main(lst, data):
    for i in range(len(lst)):
        if lst[i] in data.keys():
            lst[i] = data.get(lst[i])
    key = get_random_bytes(32)
    print("Key:", key.hex())
    plaintext = " ".join(lst)
    # print(plaintext)
    encrypted_data = algo.encrypt_AES(plaintext, key)
    print("Encrypted data:", encrypted_data)

    # with open('output.txt', 'w') as f:
    #     f.write(" ".join(lst))
