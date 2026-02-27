import re
s = input()
d = input()
if re.search(d , s):
    print("Yes")
else:
    print("No")