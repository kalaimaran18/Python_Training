# Reverse a string (Problem 1)

name=input()
print(name[::-1])

#fibonacci series (Problem 2)

n=int(input())
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b , a+b

#prime number check (Problem 3)

val=int(input())
if val>1:
    for i in range(2,int(val**0.5 +1)):
        if val%i==0:
            print("not a prime")
            break
    else:
        print("prime")
else:
    print("not a prime")



#Odd or Even (Problem 4)

number=int(input())
if number%2==0:
    print("EVEN")
else:
    print("ODD")
    

#max element of array (Problem 5)
array=list(map(int,input().split()))
val=max(array)
print(val)

#palindrome 12121 (Problem 6)

def palindrome(s):
    return s==s[::-1]
print(palindrome("level"))
print(palindrome("camel"))
