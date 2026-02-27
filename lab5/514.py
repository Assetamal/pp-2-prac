import re
s = input().strip()
pat = re.compile(r'^\d+$')
if pat.fullmatch(s):
    print("Match")
else:
    print("No match")