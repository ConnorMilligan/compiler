def fact(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

PLEASE = 0
print(fact(5))
