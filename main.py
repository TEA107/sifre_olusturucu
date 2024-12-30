import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def generate_password(numOfChars):
    password = ""
    for i in range(numOfChars):
        password += random.choice(karakterler)
    return password
num_of_letters = int(input("Kaç karakterli bir şifre istersiniz:"))
password = generate_password(num_of_letters)
print(password)