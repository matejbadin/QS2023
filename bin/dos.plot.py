#!/usr/bin/env python

import sys
import numpy as np
import matplotlib as mlt
mlt.use('Agg')
from matplotlib import pyplot as plt

E, N = np.loadtxt(sys.argv[1], usecols = (0,1), unpack = True)

plt.plot(E, N)

try:
    plt.plot([float(sys.argv[2])] * 2, [max(N),0.0],"r-")
except:
    pass

plt.xlim([min(E),max(E)])
plt.ylim([0.0,max(N)])

plt.plot(plt.xlim(),[0.0]*2,"k-")

plt.savefig(sys.argv[1].replace("dos","png"))
