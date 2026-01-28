a = int(input())
count = 0
num = list(map(int , input().split()))
for x in num:
    if(x>0):
        count+=1
print(count)