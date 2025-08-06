#basic of python input()

b=input("enter your name:")
print("Hii",b)

#using the python in evaluate the given expression
exp="23+23*2"
k=eval(exp)
print(k)

exp="6*15//5"
d=eval(exp)
print(d)

#type castng or type conversion
r="123"
u=int(r)
print(u)

str=int("765")
f=float(str)
t=(f)
print(t)


#python list append(),pop(),remove()
list1=[65,23,12,87,43]
list=list1.append(34)
print(list1)

list2=([65,23,12,87,43])
c=list2.pop(2)
print(c,list2)

list3=[23,65,86,24,45]
r=list3.remove(23)
print(list3)

list4=[23,65,86,24,45]
del(list4[0:2])
print(list4)

# python tuples
country=("india","australia","canada","dubai","england","france")
print(country[0:3])
print(country.count("india"))

#python sets operation (union,intersection,difference)

set1={1,4,7}
set2={6,4,8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

#python dictionaries (Key:value)

dict1={"india":"dehli","japan":"tokyo","china":"beijing","bangladesh":"daaka","italy":"rome"}
for key in dict1 :
    print(f"{key}")

#input method()
name=input("enter a name:")
age=input("enter your age:")
print("Hello " + name + " you are "+ age + " years old")
 
#2 input in one line
name,age=input("enter name & age :").split()
print("Hello " + name + " you are "+ age + " years old")
