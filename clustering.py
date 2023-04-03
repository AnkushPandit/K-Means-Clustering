from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import interactive

interactive(True)
center_1 = np.array([1,1])
center_2 = np.array([5,5])
center_3 = np.array([8,1])
data_1 = np.random.randn(200, 2) + center_1
data_2 = np.random.randn(200,2) + center_2
data_3 = np.random.randn(200,2) + center_3
data = np.concatenate((data_1, data_2, data_3), axis = 0)

print(data.shape)
# Number of clusters
k = 3
# Number of training data
n = data.shape[0]
print(n)
# Number of features in the data
c = data.shape[1]
print(c)

# Generate random centers, here we use sigma and mean to ensure it represent the whole data
mean = np.mean(data, axis = 0)
std = np.std(data, axis = 0)
centers = np.random.randn(k,c)*std + mean

centers_old = np.zeros(centers.shape) # to store old centers
centers_new = deepcopy(centers) # Store new centers

data.shape
clusters = np.zeros(n)
distances = np.zeros((n,k))

error = np.linalg.norm(centers_new - centers_old)

# When, after an update, the estimate of that center stays the same, exit loop
while error != 0:
    # Measure the distance to every center
    for i in range(k):
        distances[:,i] = np.linalg.norm(data - centers[i], axis=1)
    # Assign all training data to closest center
    clusters = np.argmin(distances, axis = 1)
    
    centers_old = deepcopy(centers_new)
    # Calculate mean for every cluster and update the center
    for i in range(k):
        centers_new[i] = np.mean(data[clusters == i], axis=0)
    error = np.linalg.norm(centers_new - centers_old)

plt.scatter(data[:,0], data[:,1], s=7,c='c')
plt.scatter(centers_new[:,0], centers_new[:,1], marker='*', c='g', s=150)
#plt.savefig('a.png')

plt.scatter(data_1[:,0], data_1[:,1], s=7,c='r')
plt.scatter(data_2[:,0], data_2[:,1], s=7,c='b')
plt.scatter(data_3[:,0], data_3[:,1], s=7,c='y')
plt.scatter(centers_new[:,0], centers_new[:,1], marker='*', c='g', s=150)
plt.show()
#plt.savefig('b.png')
