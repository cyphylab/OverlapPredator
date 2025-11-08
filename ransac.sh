#!/bin/bash

for N_POINTS in 250 500 1000 2500 5000
do
  python scripts/evaluate_predator.py --source_path snapshot/indoor/3DMatch --n_points $N_POINTS --benchmark 3DMatch --exp_dir snapshot/indoor/est_traj --sampling prob
done