import os
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

results = []

for d, dn, fn in os.walk("."):
    for dir in sorted(dn):
        if "scf-" in dir:
            try:
                E = 0
                with open(d+"/"+dir+"/scf.out") as f:
                    for line in f:
                        if "!" in line:
                             E = float(line.split()[4])
                results.append([float(dir.split("-")[1]), float(dir.split("-")[2]), E])
            except:
                pass

X, Y, Z = np.array(results).T
print(X)
print(Y)
print(Z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X,Y,Z)
