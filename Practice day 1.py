#problem 1   (area of circle)
e=float(input())
print(22/7*e**2)

#problem 2 (find greatest number in 2 value)
i=int(input("enter the number:"))
e=int(input("enter the number"))
if i>e:
    print(i)
else:
    print(e)

#problem 2.1 (find greatest number in 3 value)
i=int(input("enter the number:"))
e=int(input("enter the number:"))
q=int(input("enter the number:"))
if i>e:
    print(i)
elif q>i:
    print(q)
else:
    print(e)
    

#problem 3 (find even number 9 to 100 )
for i in range(10,101,2):
    print(i)
    
#problem 4 (calculate average number)
num=list(map(int,input("enter a number:").split()))
print(sum(num)/len(num))

#problem 5 (sum of two num)
num1=int(input())
num2=int(input())
print(num1+num2)

#problem 6 (product of two num)
num1=int(input())
num2=int(input())
print(num1*num2)

#problem 7 (Type casting int,float,string)
u="23"
t=int(u)
v=float(t)
print(type(u))
print(t)
print(v)

#problem 8 (user num mul*10)
while True:
    num=int(input("enter a number:"))
    if num%10==0:
        print("you entered a multiple of 10. program stopped")
        break
else:
    ("not a multiple of 10.try again")

#problem 9 (find except multiply of 10)
while True:
    num=int(input("enter a number:"))
    if num%10!=0:
        print("you entered a not a multiple of 10.try again")
        
    else:
        print("multiple of 10.program stopped")
        break

#problem 10 (find prime number or not)
num=int(input("enter the value:"))
if num>1:
    for i in range(1,num):
        if num%2==0:
            print("not a prime")
            break
    else:
        print("prime")
else:
    print("not a prime")