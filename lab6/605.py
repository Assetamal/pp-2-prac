s = input()
vowel = "aeiouAIEOU"
if any(latter in vowel for latter in s):
    print("Yes")
else:
    print("No")