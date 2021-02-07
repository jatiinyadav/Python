nums = [10,9,2]

print(nums)

print(nums[0])
print(nums[1])
print(nums[2])

for i in nums:
    print(i)

it = iter(nums)

print(it.__next__())
print(it.__next__())
print(it.__next__())

print(next(it))
print(next(it))
print(next(it))