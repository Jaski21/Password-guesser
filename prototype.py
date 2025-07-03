import random
import time

a = time.time()

def password_generator(length = 4):
    password = ""
    for i in range(length):
        password += str(random.randint(0,9))
    return password


def password_guesser(length = 4):
    guess = ""
    for i in range (length):
        guess += str(random.randint(0, 9))
    return guess


n = 0
guessed = []
password = password_generator()
print("Password to guess is:", password)
time.sleep(2)
generated_guess = password_guesser()
while generated_guess != password:
    if generated_guess in guessed:
        generated_guess = password_generator()
        continue
    guessed.append(generated_guess)
    print(generated_guess)
    generated_guess = password_guesser()
    n += 1
print(generated_guess)
print("Number of attempts:", n)
b = time.time()
print(f"Time taken: {b-a-2}")
