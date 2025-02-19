import random
import string

def generate():
    print("Welcome to Password gnerator")
    print("---------------------------")
    password_length = int(input("Enter the desired Password length: "))
    if password_length <0:
        print("Password length Must be an integer")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        print("Generated Password: ","",password)
        print("\nProgram Succesfully Executed 🦖")

generate()