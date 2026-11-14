#lists
#deepcopy
import copy
a=[[10,11],[12,13],[14,15]]
c=copy.deepcopy(a)
c[0][1]=99
c[2][0]=100
print(c)
print(a)