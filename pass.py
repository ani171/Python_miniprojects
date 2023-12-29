import random
import string

def generate_password(length=12, include_digits=True, include_symbols=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # Ensure at least one symbol
    password = random.choice(string.punctuation)
    
    # Generate the remaining part of the password
    password += ''.join(random.choice(characters) for _ in range(length - 1))

    # Shuffle the password to enhance randomness
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

# Example usage:
password = generate_password()
print("Generated Password:", password)
