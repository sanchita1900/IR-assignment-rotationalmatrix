#NAME: SANCHITA GUPTA
#ROLL NO.: 2019BCS053

import numpy as np
import math

#position of point in frame B
point_b=[2,3,0]

#rotation around x axis is done twice by 30 degrees each time
#this can also be written as b frame is rotated around x aix by 60 degrees
rotation_x=[[1,0,0],
            [0,np.cos(60. * np.pi / 180.),-1*(np.sin(60. * np.pi / 180.))],
            [0,np.sin(60. * np.pi / 180.),np.cos(60. * np.pi / 180.)]] 

#frame b is rotated around y axis by 30 degrees
rotation_y=[[np.cos(30. * np.pi / 180.),0,np.sin(30. * np.pi / 180.)],
            [0,1,0],
            [-1*(np.sin(30. * np.pi / 180.)),0,np.cos(30. * np.pi / 180.)]]

#composite rotation matrix = (rotation_y)(rotation_x)
rotation_comp=np.matmul(rotation_y,rotation_x)

point_b = np.reshape(point_b, (3, 1),order='F')

point_a=np.matmul(rotation_comp,point_b)

print(point_a)

