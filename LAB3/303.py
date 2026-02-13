s = input().strip()

code_to_digit = {
    "ZER":"0","ONE":"1","TWO":"2","THR":"3","FOU":"4",
    "FIV":"5","SIX":"6","SEV":"7","EIG":"8","NIN":"9"
}

digit_to_code = {v:k for k,v in code_to_digit.items()}

# find operator
for op in ['+','-','*']:
    if op in s:
        left,right = s.split(op)
        operator = op
        break

def decode(x):
    return int("".join(code_to_digit[x[i:i+3]] for i in range(0,len(x),3)))

a = decode(left)
b = decode(right)

if operator=='+':
    c=a+b
elif operator=='-':
    c=a-b
else:
    c=a*b

result = "".join(digit_to_code[d] for d in str(c))
print(result)
