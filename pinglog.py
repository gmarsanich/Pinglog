import os
import time

target = str(input("Ping target: "))
n = int(input("Ping how many times: "))
logfile = f"pinglog_{target}_{time.time()}.log"
print(f"Pinging {target} {n} times...")

os.system(f"ping -n {n} {target} > {logfile}")
os.system(
    f"powershell.exe New-BurntToastNotification -Text 'Done!', 'Saved to {os.getcwd()}\\{logfile}' -AppLogo img\\PowerShell_Core_6.0_icon.png"
)
print(f"Saved log to file {logfile} in {os.getcwd()}")
