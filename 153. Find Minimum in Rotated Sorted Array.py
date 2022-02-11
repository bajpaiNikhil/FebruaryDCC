nums = [3,3,1,3]

left = 0
right = len(nums) - 1

while left < right:
    mid = left + (right - left) // 2
    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid
print(left, nums[left] ,  right , nums[right])
