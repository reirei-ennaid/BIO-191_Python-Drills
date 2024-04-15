R = int(input("Enter integer, R: "))

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

count = 0
i = 2
while count < R:
    if isPrime(i):
        print(i)
        count += 1
    i += 1

