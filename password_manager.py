from cryptography.fernet import Fernet

master_pwd = input("what is the master password ? :  ")

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: #wb is write in bits
        key_file.write(key)

write_key()

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            #rstrip used to remove the extra space in output
            user,passw = data.split("|")
            #split is used to split the username and password
            print('user name = ', user, 'password = ', passw)

def add():
    name = input("account name :")
    pwd = input ("password : ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("would you like to add new password or edit old one (view,new) or Press q to quit ? : ").lower()
    if mode == 'q':
        break
    
    if mode == "view":
        view()
    elif mode == "new":
        add()
    else:
        print("invalid input.")
        continue