n = 4
k = 2


def dfsWeHave(nums, k, ret, path):
    if len(path) == k:
        ret.append(path)
        return
    for i in range(len(nums)):
        dfsWeHave(nums[i+1:] , k , ret , path+[nums[i]])

def combine(n , k ):

    ret = []
    dfsWeHave(list(range(1,n+1)) , k ,ret , path = [])
    return ret
print(combine(n , k))