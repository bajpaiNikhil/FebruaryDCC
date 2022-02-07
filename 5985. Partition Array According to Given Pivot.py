nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
less = []
equal = []
greater = []






for i in nums:
    if i >pivot:
        greater.append(i)
    elif i<pivot:
        less.append(i)
    else:
        equal.append(i)
print(less+equal+greater)