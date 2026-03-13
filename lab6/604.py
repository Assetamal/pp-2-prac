a = int(input())
b = list(map(int , input().split()))
c = list(map(int , input().split()))
result = []
for x,y in zip(b,c):
    result.append(x*y)
print(sum(result))