#!/usr/bin/env python

import os
import numpy as np

calc_script = 'si.vc-relax.in'

# pressure in GPa
min_press = 0
max_press = 20
stp_press = 21

run_cmd = 'mpirun -np 2 /nfs/raid2/software/QE-7.1/pw.x < vc-relax.in > vc.relax.out'

for press in np.linspace(min_press, max_press, stp_press):
    
    press = "{:5.3f}".format(10*press)                     # format energy cutoff string

    print("Calculating {} kBar structure".format(press))
    wd = "vc-relax-" + press

    if not os.path.exists(wd):                          # create directory for calculation
        os.makedirs(wd)

    with open(calc_script) as f:                        # create QE script in final directory
        with open(wd + "/vc-relax.in", "w") as fa:
            for line in f:
                fa.write(line.replace("$PRESS$",press)) # replace $KATOF$ with actual value
    
    os.system("cd "+wd+";"+run_cmd)                     # run calculation with PBS
