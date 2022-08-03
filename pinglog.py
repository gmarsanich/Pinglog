import os
import time
import argparse as ap
from alive_progress import alive_bar

# Getting terminal inputs

parser = ap.ArgumentParser("Example")
parser.add_argument("-t", dest="target", help="target of ping", type=str)
parser.add_argument("-n", dest="n", help="number of times to ping target", type=int)
args = parser.parse_args()

pargs = vars(args)
target = pargs["target"]
n = pargs["n"]


# Creating logfile name

logfile = f"pinglog_{target}_{time.time()}.log"

# Running command

with alive_bar(title=f"Pinging {target} {n} times") as bar:
    os.system(f"ping -n {n} {target} > {logfile}")
    os.system(
        f"powershell.exe New-BurntToastNotification -Text 'Done!', 'Saved to {os.getcwd()}\\{logfile}' -AppLogo img\\PowerShell_Core_6.0_icon.png"
    )
    bar()
print(f"Saved log to file {logfile} in {os.getcwd()}")
