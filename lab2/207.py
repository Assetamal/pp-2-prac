n = int(input())
num = list(map(int , input().split()))
max_val = max(num)
pos = num.index(max_val)+1
print(pos)