import re 
s = input()
pat = re.compile(r"\b\w+\b")
mat = re.findall(pat , s)
print(len(mat))