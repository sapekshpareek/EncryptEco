from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt_AES(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext


def decrypt_AES(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data



# plaintext = b"This is the message to be encrypted"
# key = get_random_bytes(32)  # Generating keys/passphrase
# print("Key:", key.hex())
# encrypted_data = encrypt(plaintext, key)
# print("Encrypted data:", encrypted_data)
# decrypted_data = decrypt(encrypted_data, key)
# print("Decrypted data:", decrypted_data)