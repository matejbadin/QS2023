#!/usr/bin/env python

import os
import numpy as np

source = "ge.vc-relax.in"

min = 75
max = 150
stp = 20

run_cmd = "mpirun -np 1 pw.x < relax.in > relax.out"

for press in np.linspace(min, max, stp):
   
    ppress = "{:5.3f}".format(press)

    print("Calculating " + ppress)
    wd = "press-" + ppress

    if not os.path.exists(wd):
        os.makedirs(wd)

    with open(source) as f:
        with open(wd + "/relax.in", "w") as fa:
            for line in f:
                fa.write(line.replace("$PRESS$",ppress))

    os.system("cd "+wd+";"+run_cmd)
