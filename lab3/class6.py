def ispr(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = lambda n: n > 1 and ispr(n)
primes = list(filter(num, nums))
print(primes)