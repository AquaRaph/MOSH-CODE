import subprocess

# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

completed = subprocess.run(["ls", "-ls"])
print("args", completed.args)
print("returncode", completed.returncode)
print("stderr", completed.stderr)
#print("stdout", completed.stdout)