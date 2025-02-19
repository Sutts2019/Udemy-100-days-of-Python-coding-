def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


num = int(input("Enter number to be checked for primality: "))
prime_check = is_prime(num)
print(prime_check)