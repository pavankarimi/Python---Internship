n=int(input("Enter N:"))

for i in range(n):
    for j in range(n):
        if j==2 or i==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()