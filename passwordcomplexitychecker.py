import re

def check_password_strength(password):
    """
    Checks the strength of a password based on various criteria.

    Args:
        password (str): The password to be checked.

    Returns:
        str: A message indicating the password strength.
    """

   
    has_upper = re.compile(r"[A-Z]")
    has_lower = re.compile(r"[a-z]")
    has_digit = re.compile(r"\d")
    has_special = re.compile(r"[^\w\d]")


    if len(password) < 8:
        return "Weak: Password is too short. Consider using a longer password."

  
    conditions = [
        has_upper.search(password),
        has_lower.search(password),
        has_digit.search(password),
        has_special.search(password)
    ]

    if all(conditions):
        return "Strong: Excellent password strength!"
    elif sum(conditions) >= 3:
        return "Medium: Good password strength, but could be stronger."
    else:
        return "Weak: Password lacks diversity. Consider adding more character types."


password = input("Enter your password: ")
strength = check_password_strength(password)
print(strength)