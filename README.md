# Password Strength Checker

This is a simple Python script that evaluates the strength of a password based on its length, character variety, and whether it appears in a common password list. It gives helpful feedback and suggestions for making your passwords stronger.

---

## How It Works

- Checks if the password exists in a list of common passwords (`common-password.txt` file required in the same directory).
- Calculates a score based on:
  - Password length
  - Presence of uppercase letters
  - Presence of lowercase letters
  - Presence of numbers
  - Presence of special characters
- Rates the password as **Weak**, **Okay**, **Good**, or **Strong**
- Provides improvement tips if the password is weak.

---

##  Requirements

- Python 3 (no extra libraries needed, uses built-in `string` module)

---

##  How to Use

1. Make sure you have a file named `common-password.txt` in the same directory as the script.  
   This file should contain a list of weak passwords (one per line).

2. Run the script:

```bash
python3 password_checker.py


📑 Notes

The password list file common-password.txt must exist in the same directory.

The password score is out of 7.

Longer, more varied passwords with uppercase, lowercase, numbers, and special characters get better scores.

Passwords found in the common list immediately fail the check.

Customizing the Common Password List

You can replace or expand the common-password.txt file with your own list of weak passwords for testing.
