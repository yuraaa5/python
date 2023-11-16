'''
kakaku = 1000
nebikiritu= 15
kakaku = kakaku*(100-nebikiritu)/100
print(kakaku)
'''
'''
a = 5
b = 6
a, b = b, a
print(a, b)
'''
'''
n = list(range(5))
print(type(n), n)
'''
'''
a = [0,1,2,3,4,5,6,7]
b = a[2:5]
print(b)
'''
'''
a = [1,2,3,4]
b = [5,6,7]
c = [8,9,10]
a.extend(b)
b.append(c)
print(a, b)
'''
'''
a = [[1,2], [3,4]]
b = a.copy()
b.append([5,6])
print(a)
print(b)
print(id(a[0]), id(b[0]))
'''
'''
a = (1, 2)
(b, c) = a
print(b, c)
'''