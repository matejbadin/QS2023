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
total_dos = np.loadtxt('cu.dos.pdos_tot',skiprows=1)
pdos_1s = np.loadtxt('cu.dos.pdos_atm#1(Cu)_wfc#1(s)',skiprows=1)
pdos_2p = np.loadtxt('cu.dos.pdos_atm#1(Cu)_wfc#2(p)',skiprows=1)
pdos_3d = np.loadtxt('cu.dos.pdos_atm#1(Cu)_wfc#3(d)',skiprows=1)
#pdos_4s = np.loadtxt('cu.dos.pdos_atm#1(Cu)_wfc#4(s)',skiprows=1)
#pdos_5p = np.loadtxt('cu.dos.pdos_atm#1(Cu)_wfc#5(p)',skiprows=1)


energy = total_dos[:,0]
dosup = total_dos[:,1]
dosdown = total_dos[:,2]

# find Fermi energy in non-selfconsistent calculation
#E_Fermi = float(open('cu.dos','r').readline().split()[-2])
lines = open('cu.nscf.out','r').readlines()
for line in lines:
    if 'Fermi' in line:
        E_Fermi = float(line.split()[-2])

# total dos up and down
plt.plot(energy-E_Fermi,dosup,color='red',lw=0.2,label='total spin up')
plt.plot(energy-E_Fermi,-1*dosdown,color='blue',lw=0.2,label='total spin down')

# s states
plt.plot(energy-E_Fermi,100*pdos_1s[:,1],color='red',lw=0.2,label='1s spin up')
plt.plot(energy-E_Fermi,-100*pdos_1s[:,2],color='blue',lw=0.2,label='1s spin down')

# 2p states
plt.plot(energy-E_Fermi,100*pdos_2p[:,1],color='red',lw=0.2,label='2p spin up')
plt.plot(energy-E_Fermi,-100*pdos_2p[:,2],color='blue',lw=0.2,label='2p spin down')

# 3d states
plt.plot(energy-E_Fermi,1*pdos_3d[:,1],'--',color='red',lw=0.2,label='3d spin up')
plt.plot(energy-E_Fermi,-1*pdos_3d[:,2],'--',color='blue',lw=0.2,label='3d spin down')

# 4s states
#plt.plot(energy-E_Fermi,1*pdos_4s[:,1],'-.',color='red',lw=0.2,label='4s spin up')
#plt.plot(energy-E_Fermi,-1*pdos_4s[:,2],'-.',color='blue',lw=0.2,label='4s spin down')

# 5p states
#plt.plot(energy-E_Fermi,1*pdos_2p[:,1],color='red',lw=0.2,label='5p spin up')
#plt.plot(energy-E_Fermi,-1*pdos_2p[:,2],color='blue',lw=0.2,label='5p spin down')

ylim = plt.ylim()
plt.vlines(0,ylim[0],ylim[1],colors='#66ccff',linestyles='solid',lw = 0.2)
plt.xlabel(r'$E-E_F$ [eV]')
plt.ylabel(r'density of states')
plt.legend(frameon=False,ncol=1,bbox_to_anchor=(0.99,0.99),loc='upper right',borderaxespad=0.,prop={'size': 12})
plt.savefig('pdos.pdf',bbox_inches='tight',pad_inches=1/25.4,format='pdf')
