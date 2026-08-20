n=int(input("Enter the number of elements:"))
l=[]
for i in range(n):
    l.append(int(input("Enter the element")))
unique_set=set(l)
print("the unique elements are:")
print(unique_set)