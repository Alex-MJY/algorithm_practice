# word = "racecar"
# if word == word[::-1]:
#     print("True")
# else:
#     print("False")
    
def is_palindrome(word: str):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left, right = left + 1, right - 1
    return True

words = ["racecar", "rotor", "tomato", "별똥별", "코끼리"]

for word in words:
    print(f"Is '{word}' is palindrome? {is_palindrome(word)}")        