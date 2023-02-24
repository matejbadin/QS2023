#!/usr/bin/env python

import sys
import numpy as np
import matplotlib as mlt
mlt.use('Agg')
from matplotlib import pyplot as plt

## omega [cm^(-1)]
#

energy_alpha_tin =  -630.63 * 13.605698066 / 2.0
energy_beta_tin   = -1262.04 * 13.605698066 / 4.0

omega_alpha, g_alpha = np.loadtxt('alpha-tin-phonon-dos/ge.dos', usecols = (0,1), unpack = True)
omega_beta,  g_beta  = np.loadtxt('beta-tin-phonon-dos/ge.dos', usecols = (0,1), unpack = True)

delta_omega_alpha = omega_beta[1] - omega_beta[0]

# T in Kelvins, omega [cm^-1]
def bose_einstein_occ_function(omega, T):
    conv_factor = 0.03666
    return 1.0/(np.exp(conv_factor*omega/T) - 1.0)

def entropy_oscillator(omega, T):
    n = bose_einstein_occ_function(omega, T)
    return (n + 1.0)*np.log(n + 1.0) - n*np.log(n)

# omega is array
# dos   is array
def entropy(omega, dos, T):
    delta_omega = omega[1] - omega[0]

    # Factor (n + 1) ln (n + 1) - n ln n
    entropy_factor  = entropy_oscillator(omega, T)
    integrant = entropy_factor * dos
    return np.sum(integrant * delta_omega)

def free_energy(energy, omega, dos, T):
    return energy - 3.0*(8.617333e-5)*T*entropy(omega, dos, T)


T = np.linspace(0,100,1000)

free_energy_alpha_tin = free_energy(energy_alpha_tin, omega_alpha, g_alpha, T)
free_energy_beta_tin  = free_energy(energy_beta_tin, omega_beta, g_beta, T)


plt.plot(T, free_energy_alpha_tin, linewidth = 1, color='r')
plt.plot(T, free_energy_beta_tin, linewidth = 1, color='b')

plt.xlabel("Temperature (K)")
plt.ylabel("Energy/atom (eV)")
plt.savefig('plot.png', dpi = 300)
