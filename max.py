a=[1,4,6,8,5]
a.sort()
print(a[-2])
max=a[0] 
for i in range (len(a)):
    if(a[i]>max):
        max=a[i]
print(max)
