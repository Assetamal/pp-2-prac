import re
s = input()
pat = r"\d{2,}"
mat = re.findall(pat , s)
print(" ".join(mat))