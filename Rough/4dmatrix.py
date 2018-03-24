import numpy as np

img_x = np.arange(192).reshape(4,3,4,4)
print(img_x)

img_y = np.transpose(img_x, (0,2,1,3))

print ("YAHA SE \n ")
print(img_y) 
