import os
from cryptography.fernet import Fernet

folder_name = "#05 Password Manager"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

'''def write_key():
    key = Fernet.generate_key()
    with open(os.path.join(folder_name, 'key.key'), 'wb') as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    file = open(os.path.join(folder_name, 'key.key'), 'rb') 
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open(os.path.join(folder_name, 'passwords.txt'), 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("Username:", user, ", Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Username: ")
    pwd = input("Password: ")

    with open(os.path.join(folder_name, 'passwords.txt'), 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)?, or press q to quit: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input")
        continue
