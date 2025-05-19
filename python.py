def is_palindrome(n):
    return str(n) == str(n)[::-1]

num = 121  # You can change this
print(f"Is {num} a palindrome? {is_palindrome(num)}")
