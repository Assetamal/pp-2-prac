# added from nurik's pc 28.01.2026

a = int(input())
b = list(map(int, input().split()))
c = max(b)
d = min(b)
for i in range(a):
    if b[i] == c:
        b[i] = d
print(*b)