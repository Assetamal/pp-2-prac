import re
s = input()
p = input()
r = input()
if re.search(p , s):
    print(re.sub(p , r , s))
else:
    print(s)
