def is_palindrome(s):
    s = s.lower()
    # Сравниваем строку с перевернутой версией самой себя
    return s == s[::-1]

print(is_palindrome('шалаш'))