x = int(input())
if(x<=1):
    print("NO")
else:
    prime = True

    for i in range(2 , int(x**0.5)+1):
        if x%i == 0:
            prime = False
            break
    
    if prime:
        print("YES")
    else:
        print("NO")

