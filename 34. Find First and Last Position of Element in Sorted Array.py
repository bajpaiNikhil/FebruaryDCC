nums = [5, 7, 7, 8, 8, 10]
target = 8


def binarySearchLeft(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        print(mid , nums[mid])

        if nums[mid] < target:
            left = mid + 1

        else:
            right = mid
    return left if nums[left] == target else -1


def binarySearchRight(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2+1

        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid

    return right if nums[right] == target else -1


def firstLast(nums, target):
    if target not in nums:
        return [-1, -1]

    else:
        return [binarySearchLeft(nums, target), binarySearchRight(nums, target)]


print(firstLast(nums, target))
