a = int(input())
if a<=0:
    print("No")
else:
    for i in [2,5,3]:
        while a%i==0:
            a//=i
    if a==1:
        print("Yes")
    else:
        print("No")