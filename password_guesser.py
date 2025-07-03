import random
import matplotlib.pyplot as plt

def password_generator(length=4):
    password = ""
    for i in range(length):
        password += str(random.randint(0, 9))
    return password

def password_guesser_BruteForce(length=4):
    guess = ""
    for i in range(length):
        guess += str(random.randint(0, 9))
    return guess


number_of_runs = int(input("How many times do you want to crack a password: "))
data1 = [] 
data2 = [] 
plt.style.use('dark_background')
plt.ion()
fig, ax = plt.subplots()
ax.set_title("Attempts Needed to Crack Passwords")
ax.set_xlabel("Run Number")
ax.set_ylabel("Number of Attempts")
line1, = ax.plot([], [], marker='o', color='cyan', label="Brute Force")
line2, = ax.plot([], [], marker='o', color='lime', label="Linear Search")
avg_line1, = ax.plot([], [], 'r--', label="Brute Avg")
avg_line2, = ax.plot([], [], 'orange', linestyle='--', label="Linear Avg")
for i in range(number_of_runs):
    print(f"\n--- Run {i + 1} ---")
    password = password_generator()
    print("Password to guess is:", password)
    n1 = 0
    guessed = []
    generated_guess = password_guesser_BruteForce()
    while generated_guess != password:
        if generated_guess in guessed:
            generated_guess = password_generator()
            continue
        guessed.append(generated_guess)
        print(f"[Brute] {generated_guess}")
        generated_guess = password_guesser_BruteForce()
        n1 += 1
    print(f"[Brute] {generated_guess}")
    data1.append(n1)
    n2 = 1
    guess_int = 0
    while True:
        guess = str(guess_int).zfill(4)
        print(f"[Exhaustive] {guess}")
        if guess == password:
            break
        guess_int += 1
        n2 += 1
    data2.append(n2)
    x_vals = list(range(1, len(data1) + 1))
    line1.set_xdata(x_vals)
    line1.set_ydata(data1)
    line2.set_xdata(x_vals)
    line2.set_ydata(data2)
    avg1 = sum(data1) / len(data1)
    avg2 = sum(data2) / len(data2)
    avg_line1.set_xdata([0, len(data1) + 1])
    avg_line1.set_ydata([avg1, avg1])
    avg_line2.set_xdata([0, len(data2) + 1])
    avg_line2.set_ydata([avg2, avg2])
    ax.relim()
    ax.autoscale_view()
    ax.legend()
    plt.pause(0.1)
plt.ioff()
plt.show()
