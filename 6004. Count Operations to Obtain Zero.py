

n = 79
m = 68
count = 0
while n>0 and m>0:

    if n==m:
        n-=m
        count +=1
    elif n>m:
        n-=m
        count+=1
    else:
        m-=n
        count+=1
print(count)