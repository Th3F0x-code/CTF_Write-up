import os

os.system("unzip -j 1000.zip")

for i in range(999, -1, -1):
    os.system(f"unzip -j {i}.zip")
    os.system(f"rm {i}.zip")
