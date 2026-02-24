def func(a,b):
    for i in range(b):
        for j in a:
            yield j
a = input().split()
b = int(input())
print(*func(a,b))