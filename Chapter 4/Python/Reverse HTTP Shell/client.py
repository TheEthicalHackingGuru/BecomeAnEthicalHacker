import requests
import time
import subprocess
import os


def run_cmd(cmd):
  ps = subprocess.run(cmd.strip(), capture_output=True, shell=True)

  out = ps.stdout.decode()
  err = ps.stderr.decode()

  if out:
     post_req= requests.post(url='http://127.0.0.1', data=cmd.strip() + " >> " + out)
     print(out)
  elif err:
     post_req= requests.post(url='http://127.0.0.1', data=cmd.strip() + " >> " + err)
     print(err)

cmd = ""

while cmd.strip() != "q":
    cmd = input("Shell> ")
    if cmd != 'q':  
       run_cmd(cmd)
    elif cmd == 'q':
        print("bye.n")
        break
