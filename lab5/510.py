import re
s = input()
pat = r"cat|dog"
if re.search(pat , s):
    print("Yes")
else:
    print("No")