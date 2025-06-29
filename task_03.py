import string
from getpass import getpass

def check_common_password(password):
    with open('common-password.txt', 'r') as f:
        common = f.read().splitlines()
    return password in common

def password_strength(password):
    score = 0
    length = len(password)

    lower_case = any(c.islower() for c in password)
    upper_case = any(c.isupper() for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)
    not_common = not check_common_password(password)

    if lower_case:
        score += 1
    if upper_case:
        score += 1
    if special:
        score += 1
    if digits:
        score += 1
    if length >= 8:
        score += 1
    if not_common:
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Okay"
    elif score == 5:
        return "Good"
    else:
        return "Strong"

def feedback(password):
    improvements = []

    if check_common_password(password):
        improvements.append("Avoid using common passwords.")

    if len(password) < 8:
        improvements.append("Make your password at least 8 characters long.")
    if not any(c.isupper() for c in password):
        improvements.append("Include uppercase letters.")
    if not any(c.islower() for c in password):
        improvements.append("Include lowercase letters.")
    if not any(c in string.punctuation for c in password):
        improvements.append("Add special characters (e.g., @, #, $, %, etc.).")
    if not any(c.isdigit() for c in password):
        improvements.append("Include numbers.")

    strength = password_strength(password)

    feedback_msg = f"\nPassword strength: {strength}\n"

    if strength != "Strong":
        feedback_msg += "Improvements needed:\n"
        for item in improvements:
            feedback_msg += f"→ {item}\n"

    return feedback_msg


password = getpass("Enter the password: ")
print(feedback(password))
