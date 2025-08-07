#square pattern

n=int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        print("* ", end="")
    print()

b=int(input("enter the value:"))
for j in range(b):
    for h in range(b):
        print("w ",end="")
    print()

# Right triangle pattern

n=int(input("enter the value:"))
for i in range(1,n+1):
    print("4" * i)
print()


#Right triangle pattern

def right_triangle(rows):
    for i in range(1,rows+1):
        print(' '* (rows-i)+'*' * i)
right_triangle(5)

#Traversed triangle pattern

n=int(input("enter a value:"))
for i in range(n):
    for j in range(n-i):
        print("* ",end="")
    print()

#Traversed triangle program

n=int(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if(j<i):
            print(" ",end=' ')
        else:
            print("*",end=' ')
    print()

#pramid pattern

n=int(input())
for i in range(n):
    print(" " *(n-i-1)+ "* " * (i+1))
