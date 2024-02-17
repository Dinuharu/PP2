def square(N):
    for i in range(1, N + 1):
        yield i ** 2

N = int(input())
squares = square(N)

for square in squares:
    print(square)
