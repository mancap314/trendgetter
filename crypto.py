from Crypto.Cipher import AES
import base64
import os
import numpy as np
from Crypto.Hash import SHA512


def encrypt_credentials():
    '''encrypt the credentials'''
    credentials = {} #dict where the key / encrypted value pairs will be stored

    if os.path.exists('password.txt'):
        password_file = open('password.txt')
        password = password_file.readline()
    else:
        print('ERROR: file \'password.txt\' doesn\'t exit')
        return

    # hash the password and store the hash in order to be able to check it later
    hasher = SHA512.new()
    hasher.update(password.encode('utf-8'))
    hashed_password = hasher.hexdigest()
    print('hashed_password: {}'.format(hashed_password))
    f = open('pwd_hash.txt', 'w')
    f.close()
    f = open('pwd_hash.txt', 'w')
    f.write(hashed_password)
    f.close()

    cipher = AES.new(password, AES.MODE_ECB)

    if os.path.exists('cred_clear.txt'): #file containing the uneencrypted (clear) credentials
        file = open('cred_clear.txt', 'r')
        for line in file.readlines(): #read the credentials line by line
            key, value = line.replace(' ', '').replace('\'', '').replace('\n', '').split('=')
            value = value.rjust(128)
            credentials[key] = base64.b64encode(cipher.encrypt(value))
    else:
        print('ERROR: file \'cred_clear.txt\' doesn\'t exit')
    # persist the key / encrypted credential value pairs
    np.save('cred.npy', credentials)


def check_password(password):
    '''hash password and compares the hash with the one of the real password'''
    hasher = SHA512.new()
    hasher.update(password.encode('utf-8'))
    hashed_password = hasher.hexdigest()

    f = open('pwd_hash.txt', 'r') #file containing the hash of the real password
    true_hashed_password = f.readline()

    return hashed_password == true_hashed_password


def get_credentials(password):
    '''retrieve the key / value credentials pairs from the encrypted persisted dictionary'''
    cipher = AES.new(password, AES.MODE_ECB)

    credentials = np.load('cred.npy').item()
    for key, value in credentials.items():
        value = cipher.decrypt(base64.b64decode(value)).strip()
        credentials[key] = value

    return credentials
