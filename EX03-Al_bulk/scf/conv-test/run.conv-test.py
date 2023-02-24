import os
import numpy as np

source = "al.scf.in"

CO_min = 18
CO_max = 20
CO_stp = 3

KP_min = 10
KP_max = 20
KP_stp = 3

for kp in np.linspace(KP_min, KP_max, KP_stp):
    kp = int(kp)
    for scf in np.linspace(CO_min, CO_max, CO_stp):
        print("Calculating " + str(scf))
        print("Calculating KP = {:3d}".format(kp))
        wd = "scf-" + str(scf) + "-" + str(kp)
        if not os.path.exists(wd):
            os.makedirs(wd)
        with open(source) as f:
            os.system("rm -rf "+wd+"/scf.in")
            for line in f:
                with open(wd + "/scf.in", "a") as fa:
                    line = line.replace("$CUTOFF$",str(scf))
                    line = line.replace("$KP$","{:3d}{:3d}{:3d}".format(kp,kp,kp))
                    fa.write(line)
            os.system("cd "+wd+"; pw.x < scf.in > scf.out")
