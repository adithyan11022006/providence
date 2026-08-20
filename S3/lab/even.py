n=int(input("Enter a number:"))
number=[]
for i in range(n):
    num=int(input("Enter the element {i+1}:"))
    number.append(num)
    even_number=[]
    odd_number=[]
for num in number:
    if num%2==0:
        even_number.append(num)
    else:
        odd_number.append(num)
print("original number is",number)
print("Even number is",even_number)
print("Odd number is",odd_number)