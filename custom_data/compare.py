import numpy as np
import matplotlib.pyplot as plt
import json

data_dir = "custom_data/normalized_botanical"
FACTOR = 25

with open(data_dir+"/idx_info.json", "r") as f:
    idx_info = json.load(f)

gt = np.load(data_dir+"/ground_truth.npy")
gt = gt[idx_info["offset"]::idx_info["step"]]

N = gt.shape[0]-1

rel_pose = np.zeros((N, 4, 4))

for i in range(N):
    rel_pose[i] = np.linalg.inv(gt[i+1]) @ gt[i]
# p = rel_pose[:, :3, -1]

pred = np.load(data_dir+"/pred_op.npy")

axes = ["x", "y", "z"]

plt.figure()
for i in range(3):
    plt.subplot(3, 1, i+1)
    plt.plot(rel_pose[:, i, -1]*FACTOR, label="Ground Truth")
    plt.plot(pred[:, i, -1]*FACTOR, label="Predator")
    plt.ylabel(axes[i])
    plt.legend()



plt.show()
