def is_prime(num):
    if num in [0, 1, 2, 3]:
        return True
    for n in range(2, num):
        if num % n == 0:
            return False
    else:
        return True
