def isPalindrome(s):
    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalnum())

    return s == s[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
