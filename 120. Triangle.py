


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]


dp = [0] *(len(triangle) + 1)

for row in triangle[::-1]:
    print(row)
    for i , n in enumerate(row):
        print( i , n)
        dp[i] = n+ min(dp[i] , dp[i+1])
print(dp)
