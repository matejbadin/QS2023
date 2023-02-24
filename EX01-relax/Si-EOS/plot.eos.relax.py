#!/usr/bin/env python

import matplotlib
matplotlib.use('Agg')

import os
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def eos(V,b,bd):
    V0_m = V[0]*np.ones(len(V))
    return 3/2*b*(np.power(V0_m/V,7/3)-np.power(V0_m/V,5/3))*(1+3/4*(bd-4)*(np.power(V0_m/V,2/3)-1))

def get_p_V():
    pV = []
    for root, directories, files in os.walk("."):
        for directory in sorted(directories):
            if "vc-relax-" in directory:
                try:
                    p = float(directory[9:])

                    fo = open(os.getcwd()+"/"+directory+"/vc-relax.out", 'r')
                    lines = fo.readlines()
                    fo.close()

                    V = 0

                    for line in lines:
                        if 'new unit-cell volume' in line:
                            V = float(line.split()[7])

                    pV.append([p,V])

                except:
                    print('error')
                    pass

    return np.array(sorted(pV, key=lambda x: x[0]))

pV = get_p_V()
p = pV[:,0]/10  # GPa
V = pV[:,1]     # A^3

popt, pcov = curve_fit(eos,V,p,bounds=(0,[1000.0,100.0]))
print('Bulk modulus:\t{} GPa'.format(popt[0]))
print('Derivative of bulk modulus at p=0:\t{}'.format(popt[1]))

v_calc = np.linspace(V[0],V[-1],101)
p_calc = eos(v_calc,*popt)

plt.plot(p,V,'bo',label='relax. data')
plt.plot(p_calc,v_calc,'r-',label='fit: K={:.3f}, K0={:.3f}'.format(*popt))
plt.xlabel('Pressure [GPa]')
plt.ylabel('Volume [A^3]')
plt.legend()
plt.tight_layout()
plt.savefig("bulk-fit.png")
