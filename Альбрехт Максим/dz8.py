import random
N = int(input("Введите N: "))
nums = []
for i in range(N):
    nums.append(random.randint(1,100))
print(nums)
nums2 = []
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        nums2.append(nums[i])
print("Чётные числа: ", nums2)
