import re
s = input()
num = re.findall(r'\d' , s)
print(*num)