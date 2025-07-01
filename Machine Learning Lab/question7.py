# Write a recursive function to check if a given string is a palindrome.
def isPalindrome(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return True
    
    return isPalindrome(s[1:-1])

word = input("Enter the word: ")

print(isPalindrome(word))