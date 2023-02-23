#!/usr/bin/env python

import os
import numpy as np

source = "N2.scf.in"

min_a = 1.0
max_a = 1.2
stp_a = 15

run_cmd = "mpirun -np 1 /nfs/raid2/software/QE-7.1/bin/pw.x < scf.in > scf.out"

for a in np.linspace(min_a, max_a, stp_a):
   
    sa = "{:5.3f}".format(a)

    print("Calculating " + sa)
    wd = "scf-" + sa

    if not os.path.exists(wd):
        os.makedirs(wd)

    with open(source) as f:
        with open(wd + "/scf.in", "w") as fa:
            for line in f:
                fa.write(line.replace("$A$",sa))

    os.system("cd "+wd+";"+run_cmd)
