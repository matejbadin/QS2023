#!/usr/bin/env python

import os
import numpy as np

source = "si.scf.in"

min_scf = 8
max_scf = 45
stp_scf = 25

run_cmd = "mpirun -np 1 pw.x < scf.in > scf.out"

for scf in np.linspace(min_scf, max_scf, stp_scf):
   
    sscf = "{:5.3f}".format(scf)

    print("Calculating " + sscf)
    wd = "scf-" + sscf

    if not os.path.exists(wd):
        os.makedirs(wd)

    with open(source) as f:
        with open(wd + "/scf.in", "w") as fa:
            for line in f:
                fa.write(line.replace("$KATOF$",sscf))

    os.system("cd "+wd+";"+run_cmd)
