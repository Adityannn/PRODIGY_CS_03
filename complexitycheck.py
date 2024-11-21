import re
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate strength score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria,
                 digit_criteria, special_char_criteria])

    # Determine strength level
    if score <= 2:
        strength = "Weak"
        color = Fore.RED
    elif score == 3:
        strength = "Moderate"
        color = Fore.YELLOW
    elif score == 4:
        strength = "Strong"
        color = Fore.LIGHTGREEN_EX
    else:
        strength = "Very Strong"
        color = Fore.GREEN

    return strength, color

def main():
    print(Fore.CYAN + Style.BRIGHT + "Welcome to the Password Strength Checker!")
    print(Fore.CYAN + "Please enter your password:")

    password = input(Fore.YELLOW + "Password: ")

    strength, color = check_password_strength(password)

    print(color + f"Your password strength is: {strength}")
    print(Fore.WHITE + Style.DIM + "Password Criteria:")
    print(Fore.WHITE + "- At least 8 characters long")
    print(Fore.WHITE + "- At least one uppercase letter")
    print(Fore.WHITE + "- At least one lowercase letter")
    print(Fore.WHITE + "- At least one digit")
    print(Fore.WHITE + "- At least one special character (e.g., !@#$%^&*)")

if __name__ == "__main__":
    main()
