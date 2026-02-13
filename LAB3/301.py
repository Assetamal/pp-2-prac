s = input()
is_cor = True
for i in s:
    if int(i)%2==1:
        is_cor = False
        break

if(is_cor):
    print("Valid")
else:
    print("Not valid")      