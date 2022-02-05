
n = 11111111111111111111111111111101
ans = 0
for i in range(32):
    ans = (ans << 1) + (n & 1)
    n >>= 1
print(ans)





