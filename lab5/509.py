import re
s = input().strip()
se = re.findall(r'\b\w{3}\b' , s)
print(len(se))
