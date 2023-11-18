'''remove duplicate item '''
my_list = [1,2,3,0,1,1,4,5,2,3]
myFinallist = []
for i in my_list:
    if i not in myFinallist:
       myFinallist.append(i)
print(list(myFinallist))