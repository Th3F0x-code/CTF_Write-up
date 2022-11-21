a = "TTI"
b = "3r"
c = "1s"
d = "_gn"
e = "s1"

inp = input("> ")

if len(inp) != 22:
    print("Wrong size. Check better next time")
    exit()

if (inp[0] == a[2] and inp[1] == a[1] and inp[2] == a[0]) and inp[3] == "{" and \
        ((inp[4] + inp[5]) == b[::-1]) and (inp[6] == "v" and inp[7] == "3" and inp[8] == chr(114)) and \
        (inp[9] + inp[10] == c[::-1]) and (inp[11] + inp[12] + inp[13] == d[::-1]) and (
        inp[14] + inp[15] == e[::-1]) and \
        (inp[16] == chr(95) and (inp[17] + inp[18] == b[0] + chr(97)) and (inp[19] + inp[20] == c[1] + "y") and (
                inp[21] == "}")):
    print("Awesome! Now submit!")
else:
    print("Flag is incorrect. Try again")
