# passwords.py
# BYU-I CSE 111: Password Strength Project

# Character sets
LOWER = list("abcdefghijklmnopqrstuvwxyz")
UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = list("0123456789")
SPECIAL = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
    "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",",
    ".", "<", ">", "?", "/", "`", "~"
]


def word_in_file(word, filename, case_sensitive=False):
    """Check if a word is in a file (one word per line)."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                file_word = line.strip()
                if not case_sensitive:
                    if word.lower() == file_word.lower():
                        return True
                else:
                    if word == file_word:
                        return True
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    return False


def word_has_character(word, character_list):
    """Check if the word contains any character from the list."""
    for ch in word:
        if ch in character_list:
            return True
    return False


def word_complexity(word):
    """Return complexity score based on types of characters in the word."""
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
    """Evaluate the strength of the given password and return score (0–5)."""

    # 1. Dictionary check (case insensitive)
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # 2. Common password check (case sensitive)
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # 3. Too short
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # 4. Very long passwords are strong
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # 5. Complexity-based scoring
    complexity = word_complexity(password)
    score = 1 + complexity
    return score


def main():
    """Main loop for password checking."""
    print("Welcome to the Password Strength Checker!")
    print("Enter a password to test its strength.")
    print("Type 'q' or 'Q' to quit.\n")

    while True:
        password = input("Enter password: ")
        if password.lower() == "q":
            print("Goodbye!")
            break
        strength = password_strength(password)
        print(f"Password strength: {strength}/5\n")


if __name__ == "_main_":
    main()