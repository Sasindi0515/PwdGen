import string
import random

characters = string.ascii_letters + string.digits + "!@#$%&*+-"

def generate():
    length =int(input("Enter length : "))
    password =''
    for a in range (length):
        password =password + random.choice(characters)
    print("password : "+password)
    choise =str(input("Retry (y/n) :"))
    return choise
choise = generate()
while choise =="y":
    generate()
if choise == "n" :
    print("Okey , Good")


