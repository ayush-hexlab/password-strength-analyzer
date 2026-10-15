
import string
from getpass import getpass


def analyze_password(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Try using at least 12 characters.")

    # Check lowercase letters
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Check uppercase letters
    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Check numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    # Check symbols
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Consider adding symbols.")

    # Assign a rating
    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Moderate"
    else:
        rating = "Strong"

    return score, rating, suggestions


def main():
    print("=" * 40)
    print("   PASSWORD STRENGTH ANALYZER")
    print("=" * 40)

    password = getpass("Enter a test password: ")

    if not password:
        print("Password cannot be empty.")
        return

    score, rating, suggestions = analyze_password(password)

    print("\nScore:", score, "/ 6")
    print("Rating:", rating)

    print("\nSuggestions:")

    if suggestions:
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Good job! All basic checks passed.")


if __name__ == "__main__":
    main()
