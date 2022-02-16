
s = [1,2,3]

result = [[]]
for item in s:
    result += [r + [item] for r in result]
print(result)