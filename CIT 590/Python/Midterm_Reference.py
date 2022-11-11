#LISTS:

list1 = ['1', 'dog', 'cat', 789]

index = list1.index('dog')
list1.append('hello')
list1.pop(1)
list1.insert(2, 'inserted item')
print('dog' in list1)

ls1 = [2, 3, 4]
ls2 = [7, 8, 9]
ls3 = ls1 + ls2
ls4 = ls3*3
ls1.extend(ls2)
lst5 = ls1.copy()

lst4 = []
for i in ls1:
    lst4.append(l)

import copy
complex_lst= [1, [2, 3], -1]
complex_lst2 = copy.deepcopy(complex_lst)
complex_lst[1][1] = 4



