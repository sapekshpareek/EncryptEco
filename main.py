import json
import text
import data
import encryption

dataf = text.read('data.txt')
dataf = json.loads(dataf)

def choice():
    a = int(input("Enter Your Choice\n1. Encryption\t\t2. Load Data\n3. Quit\n\nEnter Your Choice: "))
    if a==1:
        input_data = text.read('input.txt').lower()
        print('\nEncrypting Data from input.txt...')
        encryption.encrypt_main(text.convert(input_data), dataf)
        print('\nSuccess!\nEncrypted Data stored in ouput.txt.')

    elif a==2:
        chrr = []
        dict1 = {}
        data.write(chrr, dict1)

    elif a==3:
        print('\nHave a nice Day!')
        return

    else:
        print('\nEnter a Valid Choice!\n')
        choice()

choice()
