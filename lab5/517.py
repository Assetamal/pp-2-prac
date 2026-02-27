import re 
s = input()
pat = r"\b\d{2}/\d{2}/\d{4}\b"
mat = re.findall(pat , s)
print(len(mat))
