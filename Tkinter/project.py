import random
import string

def generate_password(length=12):
    """
    Generate a random password containing lowercase letters, uppercase letters,
    digits, and punctuation.

    Parameters:
    length (int): The length of the password (default is 12).

    Returns:
    str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    punctuation = random.choice(string.punctuation)

    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining_characters = [random.choice(all_characters) for _ in range(length - 4)]


    password_list = list(lowercase + uppercase + digit + punctuation + ''.join(remaining_characters))
    random.shuffle(password_list)

    return ''.join(password_list)

if __name__ == "__main__":
    print("Welcome to the Random Password Generator!")
    try:
        length = int(input("Enter the desired password length (default is 12): ") or 12)
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
