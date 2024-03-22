import time
import json
import text
import data
import encryption
import decryption

curr = time.time()
dataf = text.read('data.txt')
dataf = json.loads(dataf)

a=1
def choice():
    # a = int(input("Enter Your Choice\n1. Encryption\t\t2. Decryption\n3. Load Data\t\t4. Quit\n\nEnter Your Choice: "))
    if a==1:
        input_data = text.read('input.txt').lower()
        print('\nEncrypting Data from input.txt...')
        encryption.encrypt_main(text.convert(input_data), dataf)
        print('\nSuccess!\nEncrypted Data stored in ouput.txt')

    elif a==2:
        encodedtext = text.read('output.txt')
        key = input('\nEnter Key to Decrypt: ')
        print('\nDecrypting Data from Output.txt...')
        decryption.decrypt_main(encodedtext, key, dataf)
        print('\nSuccess!\nDecrypted Data stored in input.txt')

    elif a==3:
        chrr = []
        dict1 = {}
        data.write(chrr, dict1)

    elif a==4:
        print('\nHave a nice Day!')
        return

    else:
        print('\nEnter a Valid Choice!\n')
        choice()


choice()

new = time.time()
print('\nDuration: {}'.format((new-curr)*100))
