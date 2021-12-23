username = input("Hi, what's your name? ")
password = input("What is your password? ")

passwordlength = len(password)
password = "*" * passwordlength

print(f"Hey {username}, your password {password} is {passwordlength} letters long")