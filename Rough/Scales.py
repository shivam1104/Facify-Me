import numpy as np
factor_count=0
total_boxes=np.empty((0,9))
points=np.empty(0)
'''
h=img.shape[0]
w=img.shape[1]
'''
factor=1
minsize=20
h=1200
w=1300
minl=np.amin([h, w])
m=12.0/minsize
minl=minl*m
# creat scale pyramid
scales=[]
while minl>=12:
    scales += [m*np.power(factor, factor_count)]
    print(scales)
    print(m)
    print(factor)
    print(factor_count)
    minl = minl*factor
    factor_count += 1


print(scales)