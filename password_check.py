
min_length = 6
password = input("Enter password: ")
while len(password) < min_length:
    print("invalid")
    password = input("Enter password")
print(len(password) * "*", "was set!")
