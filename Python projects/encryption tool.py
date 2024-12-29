import cryptography.fernet
from cryptography.fernet import Fernet
import json

key = Fernet.generate_key()
encrypter = Fernet(key)

user_data = input('What is the data you want to encrypt(type "g" to get previous save): ')
if user_data.lower() == 'g':
    try:
        with open('encrypted_data.json', 'r') as file:
            print('Previous encrypted data = ' + json.load(file))
            decrypted_data = str(encrypter.decrypt(json.load(file)))
            print(f'Decrypted data = {decrypted_data}')
    except FileNotFoundError:
        with open('encrypted_data.json', 'w') as file:
            print('There is no data or the file is just created')
else:
    encrypted_data = str(encrypter.encrypt(user_data.encode()))
    encrypted_data_formatted = ''
    for i in encrypted_data:
        if i != 'b' and i != "'":
            encrypted_data_formatted += i
    print(f'Encrypted data = {encrypted_data_formatted}')
    user_choice_for_saving = input('Do you want to save this (\'Y\' for yes and \'N\' for no): ')
    if user_choice_for_saving.upper() == 'Y':
        with open('encrypted_data.json', 'w') as file:
            json.dump(encrypted_data_formatted, file)
            print('Encrypted data saved in file encrypted_data.json')
    else:
        pass
    user_choice_to_decrypt = input('Do you want to decrypt some data(Y for yes and N for no): ')
    if user_choice_to_decrypt.upper() == 'Y':
        try:
            data_to_be_decrypted = input('What is the data you want to decrypt: ')
            print(f'Decrypted data = {encrypter.decrypt(data_to_be_decrypted)}')
        except cryptography.fernet.InvalidToken:
            print('Data to decrypt is not valid.')
