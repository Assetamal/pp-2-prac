import re
s = input()
pat = r"[A-Z]"
m = re.findall(pat , s)
print(len(m))