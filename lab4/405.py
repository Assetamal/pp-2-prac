def re(a):
    while a>=0:
        yield a
        a-=1
a = int(input())
for i in re(a):
    print(i)   