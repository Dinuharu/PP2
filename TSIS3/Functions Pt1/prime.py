def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = []
    for i in numbers:
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers
        
numbers = [1, 3, 5, 6, 7, 8, 9]
print(filter_prime(numbers))
