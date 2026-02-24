a = int(input())
for i in range(0,a+1 , 2):
    if i == 0:
        print(i , end="")
    else:
        print(","+str(i),end="")