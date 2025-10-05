
# 1.Login system


# Stored credentials
username = "admin"
password = "1234"

# Allow up to 3 attempts
attempts = 3
logged_in = False

while attempts > 0:
    user = input("Enter username: ")
    pw = input("Enter password: ")

    if user == username and pw == password:
        print("Login successful ")
        logged_in = True
        break
    else:
        attempts -= 1
        print(f"Incorrect! {attempts} attempts left.")

if not logged_in:
    print("Account locked ")
    exit()  # stop program if login failed


# 2. Find prime number


# Ask for number N
N = int(input("Enter a number N: "))

print(f"Prime numbers between 2 and {N}:")
for num in range(2, N + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # checking divisibility up to sqrt(num)
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
