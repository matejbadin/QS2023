#!/usr/bin/env python

import os
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt

from scipy.optimize import curve_fit

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

def func(x, a, b):
    return 0.5 * a * (x - b)**2

popt, pcov = curve_fit(func, results[0,2:7], results[1,2:7] - np.min(results[1,2:7]))

energy_fit = func(results[0], popt[0], popt[1])

print(str(popt[0]) + ' [Ry/A^2]')
print(popt[1])

# Parameters for plots
sz = 15
lw = 2
wd = 8.6
hg = 8.6

fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize=(wd,hg))
plt.clf()

ax = fig.add_axes([0.155, 0.125, 0.9475 - 0.155, 0.90 - 0.125])

ax.tick_params(which = 'major', axis = 'both', labelsize = sz, direction = 'in', length = 10, pad = 7.5)
ax.tick_params(which = 'minor', axis = 'both', labelsize = sz, direction = 'in', length = 5, pad = 7.5)

ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')

ax.plot(results[0], results[1], linewidth = lw, color = 'black')
ax.plot(results[0], energy_fit + np.min(results[1,2:7]), linewidth = 0.5*lw, color = 'blue')

ax.set_xlabel(r'Interatomic distance - $[\mathrm{\AA}]$', fontsize = sz)
ax.set_ylabel(r'Energy $[\mathrm{Ry}]$', fontsize = sz)

ax.set_ylim(np.min(results[1]), np.max(results[1]))

plt.savefig("plot.png")
plt.close()
