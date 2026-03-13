b = int(input())
a = list(map(int , input().split()))
sq = map(lambda x : x**2 , a)
print(sum(sq))