from __future__ import print_function

import glob
import os
import os.path
import os.path
import subprocess
from shutil import copyfile, move
from threading import Thread
from time import sleep

import pefile

current_flag = []
# Guess there are 50 characters
curr_flag = "m" * 50
for i in range(50):
    try:
        current_flag.append(curr_flag[i])
    except:
        current_flag.append("A")


def find_entry_point_section(pe, eop_rva):
    for section in pe.sections:
        if section.contains_rva(eop_rva):
            return section

    return None


def capture_tmp_file(filename):
    copied = False
    while not copied:
        for file in glob.glob("*.tmp"):
            size = os.path.getsize(file)
            # print(f"Current size: {size}: {type(size)}")
            if size > 200:
                copyfile(file, filename)
                # print(f"Copied file {file}")
                copied = True
                break


def get_index(file_path):
    current_index = 0
    pe = pefile.PE(file_path, fast_load=True)

    # Acquire entrypoint for PE
    eop = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    code_section = find_entry_point_section(pe, eop)
    if not code_section:
        return

    length = 0x402051 - 0x402020 + 1

    # Get bytes including index
    code_at_oep = code_section.get_data(eop, length)

    # Get last opcode (it contains the index)
    current_index = code_at_oep[-1:]
    current_index = int.from_bytes(current_index, "big") - 1
    print(f"Index: {current_index}", end="")
    pe.close()

    return current_index


def get_first_opcode(file_path):
    bad_opcode = 0
    pe = pefile.PE(file_path, fast_load=True)

    # Acquire entrypoint for PE
    eop = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    code_section = find_entry_point_section(pe, eop)
    if not code_section:
        return

    length = 1
    # get first 10 bytes at entry point and dump them
    code_at_oep = code_section.get_data(eop, length)

    # Get first opcode
    bad_opcode = code_at_oep[0]
    print(f", First opcode: {bad_opcode}")
    pe.close()

    return bad_opcode


def main():
    capture_file_thread = Thread(target=capture_tmp_file, args=("check_flag.exe",))
    capture_file_thread.start()

    subprocess.call(["d", ''.join(current_flag)],
                    executable="/home/alessio/Scrivania/tools/CTFs/CSCML CTF 2020/Roulette/roulette.exe",
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    sleep(0.5)
    try:
        while True:
            # Get index of current character
            file_path = "check_flag.exe"
            current_index = get_index(file_path)

            # Wait for .tmp to start popping up and copy it to "something.exe"
            capture_file_thread = Thread(target=capture_tmp_file, args=("something.exe",))
            capture_file_thread.start()

            # Call current exe file
            subprocess.call(["d", ''.join(current_flag)], executable="check_flag.exe")

            # Acquire first opcode from start function
            file_path = "something.exe"
            bad_opcode = get_first_opcode(file_path)
            os.remove("something.exe")

            sleep(0.5)

            # Calculate character to get proper `push ebp; mov ebp, esp` prolog
            good_char = chr(bad_opcode ^ 0x55 ^ ord(current_flag[current_index]))
            print(f"Replacing flag[{current_index}]={current_flag[current_index]} with {good_char}")
            current_flag[current_index] = good_char

            print(f"Current flag: {''.join(current_flag)}")
            print()
            capture_file_thread = Thread(target=capture_tmp_file, args=("_check_flag.exe",))
            capture_file_thread.start()

            subprocess.call(["d", ''.join(current_flag)], executable="check_flag.exe")
            # sleep(0.5)
            move("_check_flag.exe", "check_flag.exe")
            sleep(0.5)
    except Exception as e:
        print(e)
        print(f"\n\nFinished: {''.join(current_flag)}")


if __name__ == '__main__':
    main()
