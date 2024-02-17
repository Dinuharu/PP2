def even_number(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number (n): "))
num = even_number(n)
print("Even numbers between 0 and", str(n) + ":", end=" ")
print(*num, sep=", ")
