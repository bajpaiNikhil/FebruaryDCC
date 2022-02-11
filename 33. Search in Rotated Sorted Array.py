nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

minEle = nums.index(min(nums))

left = 0
right = len(nums) - 1
if nums[minEle] <= target <= nums[right]:
    left = minEle
else:
    right = minEle
while left <= right:
    mid = left + (right - left) // 2

    if nums[mid] > target:
        right -= 1
    elif nums[mid] < target:
        left += 1
    else:
        print(mid)
        break
print(-1)
