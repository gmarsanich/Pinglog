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


# Ping function


def ping(t: str, n: int) -> None:
    logfile = f"pinglog_{t}_{time.time()}.log"
    os.system(f"ping -n {n} {t} > {logfile}")
    os.system(
        f"powershell.exe New-BurntToastNotification -Text 'Done!', 'Saved to {os.getcwd()}\\{logfile}' -AppLogo img\\PowerShell_Core_6.0_icon.png"
    )
    print(f"Saved log to file {logfile} in {os.getcwd()}")


# Running command

with alive_bar(title=f"Pinging {target} {n} times") as bar:
    if target.endswith(".txt"):
        file = open(target, "r")
        content = file.readlines()
        file.close()
        target = [s.strip() for s in content]
        print(target)
        for t in target:
            ping(t, n)
        bar()
    else:
        ping(target, n)
        bar()
