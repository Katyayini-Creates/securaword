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