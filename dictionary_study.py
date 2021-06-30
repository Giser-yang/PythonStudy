# list1 = [1, 2, 'a', [4, 'ss']]
# import copy
#
# list2 = copy.copy(list1)
# print(list2)  # [1, 2, 'a', [4, 'ss']]
# list1.append('c')
# print(list1, list2)  #[1, 2, 'a', [4, 'ss'], 'c'] [1, 2, 'a', [4, 'ss']]
# list1[3].append(5)
# print(list1,list2)  #里面的子对象被改变了[1, 2, 'a', [4, 'ss', 5], 'c'] [1, 2, 'a', [4, 'ss', 5]]
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
dict1 = dict(zip(list2, list1))
print(dict1)
for i in range(4):
    a = dict1.popitem()
    print(a)
    print(dict1)
