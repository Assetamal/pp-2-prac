import re
s = input()
p = input()
pat = re.escape(p)
mat = re.split( pat , s)
print(len(mat)-1)