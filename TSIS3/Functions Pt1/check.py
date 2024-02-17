def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num,1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    for i in numbers:
        if(is_prime(i)):
            print(i,end=' ')
        
print(filter_prime(list))
