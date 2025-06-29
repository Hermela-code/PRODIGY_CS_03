# Password Strength Checker

This is a simple Python script that evaluates the strength of a password based on its length, character variety, and whether it appears in a common password list. It provides helpful feedback and suggestions for making your passwords stronger.

---

## How It Works

- Checks if the password exists in a list of common passwords (`common-password.txt` file required in the same directory) as **one of the criteria**.
- Evaluates the password based on:
  - Minimum length of 8 characters
  - Presence of uppercase letters
  - Presence of lowercase letters
  - Presence of numbers
  - Presence of special characters (e.g., @, #, $, %)
  - Whether it's **not found in the common password list**
- Rates the password as:
  - **Weak**
  - **Okay**
  - **Good**
  - **Strong**
- Provides a list of specific improvements if the password is not "Strong"

---

## Requirements

- Python 3  
- No external libraries required (uses built-in `string` and `getpass` modules)

---

## How to Use

1. Create a file named `common-password.txt` in the same directory as the script.  
   This file should contain a list of common weak passwords, with one password per line.

2. Run the script:

```bash
python3 password_checker.py
```

3. Enter your password when prompted (the input is hidden for security).

4. Review the feedback:

   -  The script will tell you the password’s overall strength.

   - If it’s not “Strong,” it will list clear improvements you can make to strengthen your password.


## Notes

   - The password list file common-password.txt must exist in the same directory for the check to work.

   - Passwords that meet all criteria are rated Strong.

   - You can replace or expand the common-password.txt file with your own list of weak passwords for testing or stricter policy enforcement.
