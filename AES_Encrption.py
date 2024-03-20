import time
import text
import algo
from Crypto.Random import get_random_bytes

curr = time.time()

key = get_random_bytes(32)
print("\nKey:", key.hex())
plaintext = text.read('input.txt').lower()
plaintext = plaintext.encode()
encrypted_data = algo.encrypt_AES(plaintext, key).hex()
# print(encrypted_data)
size = str(encrypted_data)
print('\nLength of The Encrypted Data: ', len(size))

new = time.time()
print('\nDuration: {}'.format(new-curr))
