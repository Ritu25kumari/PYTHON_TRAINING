'''sum of list'''
l1=['m','n']
n=3
new_list = ['{}{}'.format(x,y) for y in range(1,n+1) for x in l1]
print(new_list)
