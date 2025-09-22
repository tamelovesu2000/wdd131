# CSE 111: W02 Project - Password Strength
# Author: [Your Name]
# Enhancement (for full credit): Added feedback to the user suggesting which
# character types (uppercase, lowercase, digits, special symbols) are missing
# from their password. This helps the user improve security beyond the
# assignment’s base requirements.

LOWER = list("abcdefghijklmnopqrstuvwxyz")
UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = list("0123456789")
SPECIAL = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", "|", ";", ":", '"', "'", ",", ".", "<", ">", "?",
    "/", "`", "~"
]

def word_in_file(word, filename, case_sensitive=False):
    """Return True if the word is found in the file, otherwise False."""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            file_word = line.strip()
            if case_sensitive:
                if word == file_word:
                    return True
            else:
                if word.lower() == file_word.lower():
                    return True
    return False

def word_has_character(word, character_list):
    """Return True if the word contains at least one character in the list."""
    for ch in word:
        if ch in character_list:
            return True
    return False

def word_complexity(word):
    """Return the complexity score (0–4) based on character variety."""
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    """Return strength score (0–5) and print messages based on rules."""
    # Check dictionary
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # Check top passwords
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Check length
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # Complexity-based scoring
    complexity = word_complexity(password)
    strength = 1 + complexity

    # Enhancement: give advice for improvement
    missing_types = []
    if not word_has_character(password, LOWER):
        missing_types.append("lowercase")
    if not word_has_character(password, UPPER):
        missing_types.append("uppercase")
    if not word_has_character(password, DIGITS):
        missing_types.append("digit")
    if not word_has_character(password, SPECIAL):
        missing_types.append("special symbol")
    if missing_types:
        print(f"Tip: Add {', '.join(missing_types)} to strengthen your password.")

    return strength

def main():
    """Main input loop for testing passwords until user quits."""
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == "q":
            print("Goodbye!")
            break
        strength = password_strength(password)
        print(f"Password strength = {strength}\n")

if __name__ == "__main__":
    main()
