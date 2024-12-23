import random
print('Password Generator')
char = "ABCDEFGTIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&"

# fun to save password in a simple dataBase
def save_password(password):
    named_password = input('Do you want to save password with a specific name? Type "yes" or "no": ')

    if named_password == 'yes':
        the_name_of_password = input('Enter the name of the password: ')

    else:
        the_name_of_password = "Unnamed Password"
    
    with open('password.txt', 'a') as f:
        f.write(f"{the_name_of_password}: {password}" + '\n')

    print(f"Password saved as '{the_name_of_password}'")
# ---------------------end fun----------------------

# fun to show password
def show_passwords():
    try:
        with open('password.txt', 'r') as f:
            print("\nSaved Passwords:")
            print(f.read())
    except FileNotFoundError:
        print("\nNo saved passwords found.")
# ---------------------end fun----------------------

# loop for password generation
while True:
    length = input("\nEnter password length (or 'q' to quit, 'get' to view saved passwords): ").strip()

    if length == 'q':
        print("Goodbye!")
        break
    elif length == 'get':  
        show_passwords()
#  generate password
    elif length.isdigit(): 
        length = int(length)
        password = "" 
        for _ in range(length):
            password += random.choice(char) 
        print(f"Generated Password: {password}")
        save_password(password)
# ---------------------end generate----------------------
    else:  
        print("Invalid input. Please enter a number, 'q', or 'get'.")
# ---------------------end loop----------------------

