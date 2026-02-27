# from src.core.checker import analyze_password

# def classify(score: int) -> str:
#     if score == 5:
#         return "Strong 💪"
#     elif score >= 3:
#         return "Medium ⚠️"
#     else:
#         return "Weak ❌"

# if __name__ == "__main__":
#     password = input("Enter your password: ")

#     result = analyze_password(password)
#     strength = classify(result["score"])

#     print("\nPassword Analysis:")
#     print("Strength:", strength)
#     print("Details:", result["details"])

# from src.core.checker import analyze_password

# def classify(score: int) -> str:
#     if score == 5:
#         return "Strong 💪"
#     elif score >= 3:
#         return "Medium ⚠️"
#     else:
#         return "Weak ❌"

# if __name__ == "__main__":
#     password = input("Enter your password: ")

#     result = analyze_password(password)
#     strength = classify(result["score"])

#     print("\nPassword Analysis:")
#     print("Strength:", strength)

#     if result["feedback"]:
#         print("\nSuggestions:")
#         for item in result["feedback"]:
#             print("-", item)

from src.core.checker import analyze_password

def classify(score: int) -> str:
    if score == 5:
        return "Strong 💪"
    elif score >= 3:
        return "Medium ⚠️"
    else:
        return "Weak ❌"

if __name__ == "__main__":
    password = input("Enter your password: ")

    result = analyze_password(password)
    strength = classify(result["score"])

    print("\nPassword Analysis:")
    print("Strength:", strength)
    print("Entropy (bits):", result["entropy"])

    if result["feedback"]:
        print("\nSuggestions:")
        for item in result["feedback"]:
            print("-", item)