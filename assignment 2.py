'''sum of all elements in  the list'''
list=[20,10,15,50]
total=sum(list)
print("sum of all elements in given list:", total)


'''max'''
l=[1,2,3,4,5]
m=max(l)
print(m)

'''min'''
l=[1,2,3,4,5]
m=min(l)
print(m)

'''average'''
list1 = [10,20,30]
sum_of_elements = sum(list1)
len_of_list1 = len(list1)
avg = sum_of_elements/len_of_list1
print("average of given numbers in list is:",avg)


'''A set is a subset of another set'''
A = set ([1,2,3,4,5])
B = set ([1,2,3])
if(B.issubset(A)):
    print("true")
else:
    print("False")


'''symmetric difference And set difference'''
setA={1,3,4,5,7}  
setB={0,2,4,5,6}
print(setA.symmetric_difference(setB))
setC=setA-setB
print(setC)

   
'''17'''
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)


'''18'''
def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result

nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print ("Original Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))

nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print ("\nOriginal Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n",average_tuple(nums))


'''19'''
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")