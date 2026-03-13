a = int(input())
b = input().split()
c = input().split()
f = dict(zip(b , c))
d = input()
if d in f:
    print(f[d])
else:
    print("No")