import os

os.system(f"mkdir 0")
os.system(f"zip 0 flag.txt")
os.system(f"mv 0.zip 0")

for i in range(0, 1000):
    os.system(f"mkdir {i+1}")
    os.system(f"zip -r {i+1} {i}")
    os.system(f"mv {i+1}.zip {i+1}")
    os.system(f"rm -r {i}")

os.system(f"mv 1000/1000.zip .")
os.system(f"rm -r 1000")