# setup backend for matplotlib
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

# LaTeX text rendering
font = {'family' : 'serif',
        'size'   : 15}
plt.rc('font', **font)
plt.rc('text', usetex=True)
plt.figure(num=None, figsize=(6.4, 4.8), dpi=600, facecolor='w', edgecolor='k')

# load DOS data
carbon_diamond_1st_atom_2s = np.loadtxt('carbon-diamond.pdos_atm#1(C)_wfc#1(s)',skiprows=1)
carbon_diamond_1st_atom_2p = np.loadtxt('carbon-diamond.pdos_atm#1(C)_wfc#2(p)',skiprows=1)
carbon_diamond_2nd_atom_2s = np.loadtxt('carbon-diamond.pdos_atm#2(C)_wfc#1(s)',skiprows=1)
carbon_diamond_2nd_atom_2p = np.loadtxt('carbon-diamond.pdos_atm#2(C)_wfc#2(p)',skiprows=1)

energy = carbon_diamond_1st_atom_2s[:,0]

lines = open('carbon-diamond.nscf.out','r').readlines()
for line in lines:
    if 'Fermi' in line:
        E_Fermi = float(line.split()[-2])

diamond_2s  = carbon_diamond_1st_atom_2s[:,1] + carbon_diamond_2nd_atom_2s[:,1]
diamond_2pz = carbon_diamond_1st_atom_2p[:,2] + carbon_diamond_2nd_atom_2p[:,2]
diamond_2px = carbon_diamond_1st_atom_2p[:,3] + carbon_diamond_2nd_atom_2p[:,3]
diamond_2py = carbon_diamond_1st_atom_2p[:,4] + carbon_diamond_2nd_atom_2p[:,4]

plt.plot(energy - E_Fermi,diamond_2s,  color='black', lw = 1.0, label = r'$2s$')
plt.plot(energy - E_Fermi,diamond_2pz, color='blue',  lw = 1.0, label = r'$2p_z$')
plt.plot(energy - E_Fermi,diamond_2px, color='red',   lw = 1.0, label=r'$2p_x$')
plt.plot(energy - E_Fermi,diamond_2py, color='green', lw = 1.0, label=r'$2p_y$')


ylim = plt.ylim()
plt.vlines(0,ylim[0],ylim[1],colors='#66ccff',linestyles='solid',lw = 0.2)
plt.xlabel(r'$E$ [eV]')
plt.ylabel(r'density of states')
plt.legend(frameon=False,ncol=1,bbox_to_anchor=(0.99,0.99),loc='upper right',borderaxespad=0.,prop={'size': 12})
plt.savefig('pdos_diamond.pdf',bbox_inches='tight',pad_inches=1/25.4,format='pdf')

#### Graphene

carbon_graphene_1st_atom_2s = np.loadtxt('carbon-graphene.pdos_atm#1(C)_wfc#1(s)',skiprows=1)
carbon_graphene_1st_atom_2p = np.loadtxt('carbon-graphene.pdos_atm#1(C)_wfc#2(p)',skiprows=1)
carbon_graphene_2nd_atom_2s = np.loadtxt('carbon-graphene.pdos_atm#2(C)_wfc#1(s)',skiprows=1)
carbon_graphene_2nd_atom_2p = np.loadtxt('carbon-graphene.pdos_atm#2(C)_wfc#2(p)',skiprows=1)

energy = carbon_graphene_1st_atom_2s[:,0]

lines = open('carbon-graphene.nscf.out','r').readlines()
for line in lines:
    if 'Fermi' in line:
        E_Fermi = float(line.split()[-2])

graphene_2s  = carbon_graphene_1st_atom_2s[:,1] + carbon_graphene_2nd_atom_2s[:,1]
graphene_2pz = carbon_graphene_1st_atom_2p[:,2] + carbon_graphene_2nd_atom_2p[:,2]
graphene_2px = carbon_graphene_1st_atom_2p[:,3] + carbon_graphene_2nd_atom_2p[:,3]
graphene_2py = carbon_graphene_1st_atom_2p[:,4] + carbon_graphene_2nd_atom_2p[:,4]

plt.figure(num=None, figsize=(6.4, 4.8), dpi=600, facecolor='w', edgecolor='k')

plt.plot(energy - E_Fermi,graphene_2s,  color='black', lw = 1.0, label = r'$2s$')
plt.plot(energy - E_Fermi,graphene_2pz, color='blue',  lw = 1.0, label = r'$2p_z$')
plt.plot(energy - E_Fermi,graphene_2px, color='red',   lw = 1.0, label=r'$2p_x$')
plt.plot(energy - E_Fermi,graphene_2py, color='green', lw = 1.0, label=r'$2p_y$')


ylim = plt.ylim()
plt.vlines(0,ylim[0],ylim[1],colors='#66ccff',linestyles='solid',lw = 0.2)
plt.xlabel(r'$E$ [eV]')
plt.ylabel(r'density of states')
plt.legend(frameon=False,ncol=1,bbox_to_anchor=(0.99,0.99),loc='upper right',borderaxespad=0.,prop={'size': 12})
plt.savefig('pdos_graphene.pdf',bbox_inches='tight',pad_inches=1/25.4,format='pdf')
