# 14 - ex1
import subprocess
code = subprocess.call(["g++", "Hello.cpp"])
if code == 0:
      result = subprocess.run(["./a.out"], capture_output=True, text=True)
print(result.stdout)

# 14 - ex2
#!/bin/bash 
# g++
#hello.cpp 
#./a.out

