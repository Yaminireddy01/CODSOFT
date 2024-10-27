import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6): "))
            if length >= 6:
                return length
            else:
                print("Please enter a length of at least 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def display_password(password):
    print(f"Generated Password: {password}")

def main():
    length = get_password_length()
    password = generate_password(length)
    display_password(password)

if __name__ == "__main__":
    main()