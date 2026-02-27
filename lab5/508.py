import re
s = input().strip()
d = input().strip()
part = re.split(d,s)
print(','.join(part))