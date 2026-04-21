import random
import string



print("-------------RANDOM PASSSWORD GENERATOR-------------------------------")
while True:
    usr_inp = input("Do you want to generate randdom password? (y/n):  ").strip().lower()
    
    if usr_inp == 'n':
        print("Exiting the program....")
        break
    
    characters = string.ascii_letters+ string.digits + string.punctuation
    length = 10 

    rand_password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Random Password is: {rand_password}")
