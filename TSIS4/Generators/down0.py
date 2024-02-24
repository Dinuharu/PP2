def downcount(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
num = downcount(n)
print(*num, sep=", ")
