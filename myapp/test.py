

import subprocess
import os
import urllib
import ptyprocess


# def ping(host):
#     command=['ping','-c','2',host]
#     return subprocess.call(command)


# host='www.google.com'
# print(ping(host))



# Run the pip install command for binwalk


# print("you have install",subprocess.run(['pip', 'list']))


tools=os.popen('pip install nmap ').read() 


 

print("list of your tools installed ",tools)




# Spawn a new shell process
# ptyprocess.PtyProcess.spawn('pip list | seashells').read()

# Read output from the shell process and write it to a file-like object 
# output = shell.read()
# print(output)


