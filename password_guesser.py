import random

def generate_password(length=8):
    """Generate a random password."""
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def password_guesser():
    """Main function to run the password guessing game."""
    password = generate_password()  # Simulate a password to guess
    common_passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "qwerty", "abc123", "football", "monkey"]
    attempts = 0

    print("Welcome to the Password Guesser!")
    print("The app will try to guess the password.")

    for guess in common_passwords:
        attempts += 1
        print(f"Trying: {guess}")
        if guess == password:
            print(f"Congratulations! The app guessed the password '{password}' in {attempts} attempts.")
            break
    else:
        print("The app could not guess the password.")

if __name__ == "__main__":
    password_guesser()
