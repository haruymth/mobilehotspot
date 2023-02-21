import time
import subprocess
import sys
def command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
        for line in result.stdout.splitlines():
            yield line
    except subprocess.CalledProcessError:
        print('Command [' + cmd + '] was failed.', file=sys.stderr)
        sys.exit(1)
while True :
    subprocess.run("powershell -executionpolicy bypass -File TurnOnMobileHotSpot.ps1")
    time.sleep(1)