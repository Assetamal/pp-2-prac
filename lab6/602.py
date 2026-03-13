a = int(input())
b = list(map(int , input().split()))
count = len(list(filter(lambda x : x%2==0 , b)))
print(count)