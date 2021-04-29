def isprime(n):
    if not isinstance(n, int):
        raise TypeError("n must be an instance of integer")
    if n < 1:
        raise ValueError("n must be a positive greater than or equal to 1")
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
