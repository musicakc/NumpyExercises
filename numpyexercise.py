import numpy as np

#print numpy version and configuration
print(np.__version__)
np.__config__.show()

#create a null vector of size 10
z = np.zeros(10)
print z

#create a null vector of size 10 but fifth value is 1
m = np.zeros(10)
m[4] = 1
print m

#create a vector with values ranging from 10 to 49
k = np.arange(10,50)
