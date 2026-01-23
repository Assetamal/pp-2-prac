#1 int
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#2 float
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#3 Strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0

#4 (optional): converting complex to an integer:
try:
    a = 7 + 0j
    b = int(a)
    print(a, b)
except TypeError:
    print("You cant convert complex number to an integer!\nAutomatically converted to a str")
    b = str(a)
    print(a, b)

#5 (optional): converting str to a complex number
a = 4.5
b = complex(a)
print(a , b)
