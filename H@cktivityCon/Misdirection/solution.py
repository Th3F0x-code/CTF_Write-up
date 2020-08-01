import requests

host = "http://jh2i.com:50011"
default = host + "/site/flag.php"

r = requests.get(default, allow_redirects=False)

flag = ''

while not flag or flag[len(flag) - 1] != '}':
    r = requests.get(host + r.headers["Location"], allow_redirects=False)

    if int(r.headers['Content-Length']) > 0:
        flag += r.text.split('flag is ')[1].strip()
    print(flag)

# FLAG --> flag{http_302_point_you_in_the_right_redirection}
