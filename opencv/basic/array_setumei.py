import numpy as np

x=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])

print(x)

a = x[2,3]

print(a)

b = x[0:3, 0:2]

print(b)

c = x[2:, :1]

print(c)

y = np.array([[1,2,3],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]) 
# ->show problem