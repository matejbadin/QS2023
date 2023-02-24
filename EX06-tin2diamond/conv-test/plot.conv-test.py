#!/usr/bin/env python

import os
import numpy as np
import matplotlib as mlt
mlt.use('Agg')
from matplotlib import pyplot as plt

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
                results.append([float(dir[4:]), E])
            except:
                pass

results = sorted(results, key=lambda x: x[0])
results = np.array(results).T
plt.plot(results[0],results[1], linewidth=2)
plt.savefig("plot.png")
