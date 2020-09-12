#!/bin/sh
cd /home/pwn && \
timeout --foreground 300 qemu-system-x86_64 \
    -m 256M \
    -kernel ./bzImage \
    -initrd ./rootfs.cpio \
    -append "root=/dev/ram rw console=ttyS0 oops=panic panic=1 pti=off kaslr quiet" \
    -cpu kvm64,+smep \
    -monitor /dev/null \
    -nographic
