n=int(10)
a=[]
for i in range(0,n):
    Height=int(input("Enter Height: "))
    a.append(Height)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))
