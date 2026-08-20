m=int(input("Enter a number:"))
n=int(input("Enter a number:"))
Even_sqr={i*i for i in range(m,n+1)if i%2==0}
print(Even_sqr)