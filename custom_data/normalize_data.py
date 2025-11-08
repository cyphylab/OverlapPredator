import numpy as np
import os

data_dir = "custom_data/curated_botanical_garden"
op_dir = "custom_data/normalized_botanical"

FACTOR = 25

contents = os.listdir(data_dir+"/couds")

count = 0
for file in contents:
    if file.startswith("cloud_") and os.path.isfile(os.path.join(data_dir, file)):
        cloud = np.load(data_dir+"/"+file)/FACTOR
        np.save(op_dir+"/clouds/cloud_"+str(count)+".npy", cloud)
        count += 1
        print(f"Completed cloud {count}")

gt = np.load(data_dir+"/"+"ground_truth.npy")
gt[:,:3,-1] = gt[:,:3,-1]/FACTOR
np.save(op_dir+"/ground_truth.npy", gt)

print("Total clouds :",count)
