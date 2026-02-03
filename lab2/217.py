n = int(input())

nums = [input() for _ in range(n)]

count = 0

for x in set(nums):
    if nums.count(x) == 3:
        count += 1

print(count)
