import string

common_passwords = {
    "123456", "password", "123456789", "12345678", "12345",
    "1234567", "qwerty", "abc123", "football", "monkey"
}

def calculate_strength(password):
    score = 0

    if password in common_passwords:
        return 0

    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if length >= 8:
        score += 2
    elif length >= 6:
        score += 1

    score += has_upper + has_lower + has_digit + has_special

    return score

def insertion_sort_passwords(passwords):
    for i in range(1, len(passwords)):
        key = passwords[i]
        j = i - 1
        while j >= 0 and calculate_strength(passwords[j]) < calculate_strength(key):
            passwords[j + 1] = passwords[j]
            j -= 1
        passwords[j + 1] = key
    return passwords

def run_password_checker():
    passwords = []

    print("Welcome to the Password Strength Checker (Console Version)")
    print("Type 'exit' to finish and view the password ranking.\n")

    while True:
        pwd = input("Enter a password to check: ").strip()
        if pwd.lower() == "exit":
            break
        if not pwd:
            print("Please enter a non-empty password.\n")
            continue

        score = calculate_strength(pwd)
        passwords.append(pwd)
        print(f"Strength score for '{pwd}': {score}\n")

    if passwords:
        print("\nPassword Ranking (from strongest to weakest):")
        sorted_pwds = insertion_sort_passwords(passwords.copy())
        for pwd in sorted_pwds:
            print(f" - {pwd} → Score: {calculate_strength(pwd)}")
    else:
        print("\nNo passwords entered.")

if __name__ == "__main__":
    run_password_checker()
