# COMMON_PASSWORDS = {
#     "123456",
#     "password",
#     "password123",
#     "admin",
#     "admin123",
#     "admin@123",
#     "qwerty",
#     "letmein",
#     "welcome",
#     "iloveyou"
# }

# def is_common_password(password: str) -> bool:
#     """
#     Check if password exists in common password list.
#     """
#     return password.lower() in COMMON_PASSWORDS

# def load_common_passwords(filepath: str) -> set:
#     """
#     Load common passwords from a file into a set.
#     """
#     try:
#         with open(filepath, "r", encoding="utf-8") as file:
#             return {line.strip().lower() for line in file}
#     except FileNotFoundError:
#         return set()


# COMMON_PASSWORDS = load_common_passwords("data/common_passwords.txt")


# def is_common_password(password: str) -> bool:
#     return password.lower() in COMMON_PASSWORDS

# def load_common_passwords(filepath: str) -> set:
#     """
#     Load common passwords from a file into a set.
#     """
#     try:
#         with open(filepath, "r", encoding="utf-8") as file:
#             return {line.strip().lower() for line in file}
#     except FileNotFoundError:
#         return set()


# COMMON_PASSWORDS = load_common_passwords("data/common_passwords.txt")

# def is_common_password(password: str) -> bool:
#     return password.lower() in COMMON_PASSWORDS

# def has_repeated_characters(password: str, threshold: int = 3) -> bool:
#     """
#     Detect if a character repeats consecutively more than threshold times.
#     Example: 'aaaa' or '1111'
#     """
#     count = 1

#     for i in range(1, len(password)):
#         if password[i] == password[i - 1]:
#             count += 1
#             if count >= threshold:
#                 return True
#         else:
#             count = 1

#     return False

# def has_sequential_pattern(password: str) -> bool:
#     """
#     Detect simple ascending sequences like 1234 or abcd.
#     """
#     for i in range(len(password) - 3):
#         chunk = password[i:i+4]

#         if chunk.isdigit():
#             if chunk in "0123456789":
#                 return True

#         if chunk.isalpha():
#             if chunk.lower() in "abcdefghijklmnopqrstuvwxyz":
#                 return True

#     return False

def load_common_passwords(filepath: str) -> set:
    """
    Load common passwords from a file into a set.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return {line.strip().lower() for line in file}
    except FileNotFoundError:
        return set()


COMMON_PASSWORDS = load_common_passwords("data/common_passwords.txt")

def is_common_password(password: str) -> bool:
    return password.lower() in COMMON_PASSWORDS

def has_repeated_characters(password: str, threshold: int = 3) -> bool:
    """
    Detect if a character repeats consecutively more than threshold times.
    Example: 'aaaa' or '1111'
    """
    count = 1

    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            count += 1
            if count >= threshold:
                return True
        else:
            count = 1

    return False

def has_sequential_pattern(password: str) -> bool:
    """
    Detect simple ascending sequences like 1234 or abcd.
    """
    for i in range(len(password) - 3):
        chunk = password[i:i+4]

        if chunk.isdigit():
            if chunk in "0123456789":
                return True

        if chunk.isalpha():
            if chunk.lower() in "abcdefghijklmnopqrstuvwxyz":
                return True

    return False

def has_repeated_block(password: str) -> bool:
    """
    Detect repeated substring patterns like abcabcabc.
    """
    length = len(password)

    for size in range(1, length // 2 + 1):
        if length % size == 0:
            block = password[:size]
            if block * (length // size) == password:
                return True

    return False

def has_word_plus_numbers(password: str) -> bool:
    """
    Detect patterns like word123 or admin2024.
    """
    import re
    return bool(re.match(r"^[A-Za-z]+[0-9]+!?$", password))

KEYBOARD_PATTERNS = [
    "qwerty",
    "asdfgh",
    "zxcvbn",
    "qwertyuiop",
    "123456",
    "098765"
]

def has_keyboard_pattern(password: str) -> bool:
    lower_pw = password.lower()
    return any(pattern in lower_pw for pattern in KEYBOARD_PATTERNS)