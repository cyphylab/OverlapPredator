import numpy as np
import matplotlib.pyplot as plt

# data_dir = 'custom_data/curated_botanical_garden/'
data_dir = 'custom_data/normalized_botanical/'

gt_tf = np.load(data_dir+'/ground_truth.npy')
p = gt_tf[:,:3, -1]

p_sub = p[::100]

axes = ["x", "y", "z"]

plt.figure()
for i in range(3):
    plt.subplot(3,1,i+1)
    plt.plot(p[:,i])
    plt.ylabel(axes[i])

plt.figure()
plt.plot(p[:,0], p[:,1])
plt.scatter(p_sub[:, 0], p_sub[:, 1])
plt.scatter(p[0,0], p[0,1], color='red')
plt.xlabel(axes[0])
plt.ylabel(axes[1])

step_size = np.linalg.norm(np.diff(p_sub, axis=0), axis=1)

plt.figure()
plt.title("Step Size")
plt.plot(step_size)

plt.show()