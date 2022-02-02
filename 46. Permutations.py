nums = "3z4"

result = []


def dfsWeHave(nums, result, path):
    if not nums:
        result.append(path)

    for i in range(len(nums)):
        print(nums[:i] + nums[i + 1:], path, path + [nums[i]], result)
        dfsWeHave(nums[:i] + nums[i + 1:], result, path + [nums[i]])


dfsWeHave(nums, result, path=[])
print(result)
