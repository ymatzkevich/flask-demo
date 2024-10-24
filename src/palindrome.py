def palindrome(n: int) -> str:
    """Checks whether n is a palindrome"""
    if n < 0:
        return "False"

    m = 0
    temp = n

    while temp != 0:
        digit = temp % 10
        m = m * 10 + digit
        temp //= 10

    return str(m == n)