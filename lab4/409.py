def f(n):
    for num in range(n+1):
        yield 2**num
a = int(input())
print(*f(a))