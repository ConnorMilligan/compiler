def check_even(n):
    quotient = n / 2
    if quotient * 2 == n:
        return True
    else:
        return False
print(check_even(7))