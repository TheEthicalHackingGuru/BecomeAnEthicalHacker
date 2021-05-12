import subprocess


def run_cmd(cmd):
  ps = subprocess.run(cmd.strip(), capture_output=True, shell=True)

  out = ps.stdout.decode()
  err = ps.stderr.decode()

  if out:
    print(out)

  elif err:
    print(err)
  return

cmd = ""

while cmd.strip() != "q":
    cmd = input("Shell> ")
    if cmd != 'q':
       run_cmd(cmd.strip())
    elif cmd == 'q':
        print("bye")
        break
