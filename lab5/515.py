import re
s = input()
def di(d):
    dig = d.group()
    return dig * 2
pat = re.sub(r'\d' , di , s)
print(pat)