import getpass
import random
import string

def generate_password(length):
    # Get all the printable ASCII characters
    characters = string.printable
    # Remove the characters that might cause problems, such as backslashes
    characters = characters.replace('\\', '')
    # Remove single and double quotes
    characters = characters.replace('\'', '').replace('\"', '')
    # Generate the password
    password = ''.join(random.choices(characters, k=length))
    return password

def create_account(username, password=None):
    if not password:
        password = generate_password(16)
    # Store the account information in a dictionary
    account = {'username': username, 'password': password}
    return account

def login(username, password):
    # Check if the account exists and the password is correct
    if username in accounts and accounts[username]['password'] == password:
        return True
    return False

def change_password(username, old_password, new_password):
    # Check if the account exists and the password is correct
    if login(username, old_password):
        # Update the password
        accounts[username]['password'] = new_password
        return True
    return False

# Initialize the accounts dictionary
accounts = {}

# Create a new account
username = input('Enter a username: ')
account = create_account(username)
accounts[username] = account
print(f'Your password is: {account["password"]}')

# Log in to the account
username = input('Enter your username: ')
password = getpass.getpass('Enter your password: ')
if login(username, password):
    print('Login successful!')
else:
    print('Login failed.')

# Change the password
old_password = getpass.getpass('Enter your old password: ')
new_password = getpass.getpass('Enter your new password: ')
if change_password(username, old_password, new_password):
    print('Password changed.')
else:
    print('Failed to change password.')
