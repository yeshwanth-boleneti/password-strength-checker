from typing import Literal


def check_password_strength(
    password: str,
) -> Literal["Strong", "Medium", "Weak"]:
    length_ok = len(password) >= 8
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True

    if length_ok and has_upper and has_digit and has_special:
        return "Strong"
    elif length_ok and (has_upper or has_digit):
        return "Medium"
    else:
        return "Weak"


def main() -> None:
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")


if __name__ == "__main__":
    main()
