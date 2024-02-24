def div3and4(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
div_nums = div3and4(n)
for num in div_nums:
    print(num)
