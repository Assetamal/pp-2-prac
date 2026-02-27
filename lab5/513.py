import re
s = input()
ma = re.findall(r"\w+" , s)
print(len(ma))