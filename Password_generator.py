import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure password length is valid
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        # Prompt the user to input the desired length of the password
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        
        if password:
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()