#!/usr/bin/python
import subprocess
import os
print("[*] Installing requirements.txt...")
subprocess.Popen("pip3 install -r requirements.txt", shell=True).wait()
os.system("sudo apt install netcat")
os.system("clear")
print("[*] Finished.")
