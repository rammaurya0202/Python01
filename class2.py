from collections import deque
# import os;
# print(os.listdir());

# a=99;
# b="RamMaurya"
# c=40.54;
# print(a);
# print(b);
# print(type(a));

#arithmetic Operators
# a=5;
# b=9;
# print("sum of a and b is", a+b);
# print("The value of a minus b",a-b);
# print("The valus of a*b is",a*b);


#list in python
# l=[2,17,3,4,5,6,7,14,15,16,18];
# print(l)
# l.append(19);
# print(l)
# l.sort();
# print(l)


#creating a tuple
#you can not change the value of a tuple this is the main difference 
# t=(4,5,6,7,8,9,1,3,4,4,4,4,133,16);
# print(t.index(4))  #this function will count the number of occurnces of same element
# print(t)

# fruit1=input("Entered the fruit name 1 :" )
# fruit2=input("Entered the fruit name 2 :" )
# fruit3=input("Entered the fruit name 3 :" )
# fruit4=input("Entered the fruit name 4 :" )
# fruit5=input("Entered the fruit name 5 :" )
# fruit6=input("Entered the fruit name 6 :" )

# myFruitList=[fruit1,fruit2,fruit3,fruit4,fruit5,fruit6]
# print(myFruitList)

# myDictionary={
#     "Fruits" : "apple" ,
#     "Juice"  :  "Mango" ,
#     "Bike"   : "R15"

# }

# print(myDictionary.get("Fruits"))
# print(myDictionary["Bike"])

# mySet={2,3,4,5,67,8,9,12}
# print(mySet.add(13))
# mySet.pop()
# mySet.pop()
# mySet.pop()
# mySet.pop()
# print(mySet.remove(5))
# print(mySet.__init__)


# conditionals Questions
# i=1
# while i<=10 :
#     print(2*i)
#     i=i+1


# def Sum(marks) : 
#     return marks[0] + marks[1] + marks[2]


# marks2=[23,45,65]
# p=Sum(marks2)
# print(p)


# def calculateGmean(a,b) :
#     mean=a*b/a+b
#     print(mean)


# a=10
# b=10

# calculateGmean(a,b)


# AGAIN lIST
# marks=int(input("Please enter your marks"))
# if(marks>50) :
#     print("PASS")
# else :
#     print("FAIL") 

# append method
# numbers=[23,1,4,5,6,78,9,4,4,4,4]
# num=[11,22,33,44]
# numbers.sort();
# print(numbers)
# numbers.append(8)

# print(numbers)
# numbers.insert(3,10)
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.extend(num)
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.pop(4)
# print(numbers)
# numbers.clear()
# print(numbers)
# print(numbers.count(4))

# stack=[2,3,4,5,6]
# stack.append(8)
# stack.append(10)
# print(stack)
# stack.pop()
# print(stack)

# List Comprehensions

# squares=[]
# for x in range(11) :
#     squares.append(x**2)

# print(squares)
# squares = [x**2 for x in range(10)]
# print(squares)

# i=1
# for i in  range (4) :
#     print(i)


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])

# print(transposed)


# the del statement
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)

# del a[2:4]
# print(a)
# del a[:]
# print(a)

# Tuples and Sequences
# t=1,2,4,'Hello!'
# print(t[0])
# t.count(1)
# u = t, (1, 2, 3, 4, 5)
# print(u)

# SETS
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print('orange' in basket)

# combs=[]
# for x in [1,2,3] :
#     for y in [3,1,4] :
#         if x!=y :
#             combs.append((x,y))


# print(combs)


# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)


# tel = {'jack': 4098, 'sape': 4139}
# print(tel)

# tel['guido'] =4127
# print(tel)
# print('guido' in tel)

# reversed method
# for i in reversed(range(1, 10, 2)):
#     print(i)




# num=[2,1,3,1,1,1,4,5,5]
# for i in sorted(num) :
#     print(i)


def fib(n) :
    if n==0 or n==1 :
        return n
    else :
        return (fib(n-1) + fib(n-2))
    


print(fib(9))