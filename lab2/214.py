a = int(input())
num = list(map(int, input().split()))

best = num[0]
mx = 0

for x in num:
    c = num.count(x)
    if c > mx or (c == mx and x < best):
        mx = c
        best = x

print(best)
