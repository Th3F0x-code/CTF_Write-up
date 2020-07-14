import binascii
import hashlib
import string

from pwn import *

r = remote('76.74.178.201', 8002)

# Receive and solve the PoW challenge
challenge = r.recv().split()
algo = challenge[8].split("(")[0]
suff = challenge[10]
size = int(challenge[14])
print(algo, suff, size)
s = iters.mbruteforce(lambda x: getattr(hashlib, algo)(x).hexdigest().endswith(suff), string.printable + string.digits,
                      size, 'fixed')
r.send(s + "\n")

# Print the assignment
print(r.recvline().strip())
print(r.recvline().strip())
print(r.recvline().strip())
print(r.recvline().strip())
print(r.recvline().strip())
print(r.recvline().strip())

while True:

    msg = r.recvline().strip()
    print(msg)

    # Parse the number
    msg_parts = msg.split()
    if msg_parts[1] == "whats":
        num = int(msg_parts[6])
    else:
        break

    # Convert to hex
    h = hex(num)[2:]
    if h.endswith("L"):
        h = h[:-1]
    if len(h) % 2 == 1:
        h = '0' + h

    b = bytearray.fromhex(h)
    b_low = bytearray()
    b_high = bytearray()

    nearest_num = num

    # Go through the string
    for x in range(len(b)):
        c = b[x]

        # Find the first nonprintable character
        if not (chr(c) in string.printable):

            # Find closest lower and higher printable characters
            low = c
            low_threshold_crossed = False
            while not (chr(low) in string.printable):
                low = (low - 1) & 0xFF
                if low == 0:
                    low_threshold_crossed = True

            high = c
            high_threshold_crossed = False
            while not (chr(high) in string.printable):
                high = (high + 1) & 0xFF
                if high == 0:
                    high_threshold_crossed = True

            b_low[:] = b[:]
            b_high[:] = b[:]

            # Build lower and higher numbers 
            b_low[x] = low
            if low_threshold_crossed and x != 0:
                b_low[x - 1] -= 1
            for i in range(x + 1, len(b_low)):
                b_low[i] = 0x7e

            low_num = int(binascii.hexlify(b_low), 16)

            b_high[x] = high
            if high_threshold_crossed and x != 0:
                b_high[x - 1] += 1
            for i in range(x + 1, len(b_high)):
                b_high[i] = 0x9

            high_num = int(binascii.hexlify(b_high), 16)

            # Decide which number is closer to the original
            if abs(num - low_num) > abs(num - high_num):
                nearest_num = high_num
            else:
                nearest_num = low_num
            print(nearest_num)
            break

    # Send the answer
    r.send(str(nearest_num) + "\n")

    msg = r.recvline().strip()
    print(msg)

    # Exit if we see the flag
    if "flag" in msg:
        break

r.interactive()

# FLAG --> ASIS{jus7_simpl3_and_w4rmuP__PPC__ch41LEn93}
