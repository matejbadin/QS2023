#!/usr/bin/env python

import sys
import numpy as np
import matplotlib as mlt
mlt.use('Agg')
from matplotlib import pyplot as plt

E, Ndown, Nup = np.loadtxt(sys.argv[1], usecols = (0,1,2), unpack = True)

plt.plot(E, -Ndown,label="down")
plt.plot(E,    Nup,label="up"  )

try:
    plt.plot([float(sys.argv[2])] * 2, [max(Nup),-max(Ndown)],"r-")
except:
    pass

plt.xlim([min(E),max(E)])
plt.ylim([-max(Ndown),max(Nup)])

plt.plot(plt.xlim(),[0.0]*2,"k-")

plt.legend()
plt.tight_layout()
plt.savefig(sys.argv[1] + ".png")
