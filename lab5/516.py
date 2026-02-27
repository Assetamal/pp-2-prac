import re
s = input()
pat = r"^Name:\s(.+),\s*Age:\s*(.+)$"
mat = re.search(pat , s)
if mat:
    name = mat.group(1)
    age = mat.group(2)
    print(name , age)