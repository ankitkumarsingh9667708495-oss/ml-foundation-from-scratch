import numpy as np

# Declare 1D vector
a = np.array([1,2,3,4])
print(a)

# Reshape to 2D

b = a.reshape(2,2)
print(b)

# Matrix multiplication using @

c = np.array([[1,2],
             [2,3]])
d = np.array([[5,6],
             [7,8]])

result = c@d
print("Matrix multiplication\n",result)

#Transpose of matix

T = np.transpose(d)
print(T)

#Compute mean along axis 0 and axis 1

mean1 = np.mean(c, axis= 0)
mean2 = np.mean(d, axis = 1)
print("Column wise mean: ", mean1)
print("Row wise mean: ", mean2)

#Creating broadcasting example

a1 = np.array([1,2,3,4])
a2 = np.array([5,6,7,8])

c = a1+a2
d = a1+10
print("Broadcasting1: ",c)
print("Broadcasting2: ",d)