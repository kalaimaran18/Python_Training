#Swapping two number (Problem 7)
a=int(input())
b=int(input())
temp=a
a=b
b=temp
print(a,b)

#Average all the elements in a array (Problem 8)
arr=list(map(int,input().split()))
print(sum(arr)/len(arr))

#Maximum value of the list  (Problem 9)
arr=list(map(int,input().split()))
print(max(arr))

#Find the length of the string (Problem 10)
st=input()
print(len(st))

#If the number is positive or negative (Problem 11)
num=int(input())
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")
    
#Reverse an array      (Problem 12)
arr=list(map(int,input().split()))
print(arr[::-1])

#Minimum element of the array  (Problem 13)
arr=list(map(int,input().split()))
print(min(arr))

#Sum of digits   (Problem 14)
num=map(int,input().split())
print(sum(num))

#Max of two number (Problem 15)
num1=int(input())
num2=int(input())
if num1>num2:
    print(num1)
else:
    print(num2)
    
#Check the number is perfect square  (Problem 16)
num=int(input())
square=num*num
print(square)

#Find the duplicate elements in array  (Problem 17)
arr=list(map(int,input().split()))
duplicate=list(set([x for x in arr if arr.count(x)>1]))
print(duplicate)