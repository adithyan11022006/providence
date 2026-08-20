n=int(input("Enter no of elements:"))
l=  []
for i in range(n):
    a=input("Enter first element:")
    b=input("Enter second element:")
    l.append((a,b))
print(l)
l.sort(key=lambda x:x[1])
print("the sorted element are:")
print(l)