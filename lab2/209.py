a = int(input())
num = list(map(int,input().split()))
b = max(num)
c = min(num)
for i in range(len(num)):
    if num[i] == b:
        num[i] = c

print(*num)