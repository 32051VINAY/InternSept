import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Assess overall strength
    if strength < 3:
        feedback.append("Password is weak.")
    elif strength == 3:
        feedback.append("Password is moderate.")
    else:
        feedback.append("Password is strong.")

    return feedback

def main():
    print("Welcome to the Password Strength Assessment Tool!")
    while True:
        password = input("Enter a password to assess its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break
        feedback = assess_password_strength(password)
        print("\nFeedback:")
        for line in feedback:
            print(f"- {line}")
        print()

if __name__ == "__main__":
    main()
