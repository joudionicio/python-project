from flask import Flask, render_template, request
import random
import getpass

app = Flask(__name__)

def generate_password(length=8):
    """Generate a random password."""
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def get_password():
    password = getpass.getpass("Enter your password: ")
    return password

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    password = request.form['password']
    common_passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "qwerty", "abc123", "football", "monkey"]
    attempts = 0
    guessed = False

    for guess in common_passwords:
        attempts += 1
        if guess == password:
            guessed = True
            break

    return render_template('result.html', guessed=guessed, attempts=attempts, password=password)

if __name__ == "__main__":
    password = get_password()
    print("Password retrieved successfully.")
    app.run(debug=True)
