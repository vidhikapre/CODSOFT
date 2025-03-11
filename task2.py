import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4!"

    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User Input
length = int(input("Enter the desired password length: "))

# Generate and display password
password = generate_password(length)
print(f"Generated Password: {password}")
