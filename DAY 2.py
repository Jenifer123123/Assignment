n = int(input("Enter a number :"))
count = 0
for i in range(2,n):
    if(n%i == 0):
        count += 1
if(count==0):
    print("yes this is prime")
else:
    print("No this is not prime")
