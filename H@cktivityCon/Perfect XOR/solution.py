import base64

cipher_b64 = b"MTE0LDg0LDQzNyw4MDk1LDMzNTUwNDM0LDg1ODk4NjkxNzAsMTM3NDM4NjkxMzc2LDIzMDU4NDMwMDgxMzk5NTIyMzUsMjY1ODQ1NTk5MTU2OTgzMTc0NDY1NDY5MjYxNTk1Mzg0MjI0NSwxOTE1NjE5NDI2MDgyMzYxMDcyOTQ3OTMzNzgwODQzMDM2MzgxMzA5OTczMjE1NDgxNjkyOTQsMTMxNjQwMzY0NTg1Njk2NDgzMzcyMzk3NTM0NjA0NTg3MjI5MTAyMjM0NzIzMTgzODY5NDMxMTc3ODM3MjgyMjMsMTQ0NzQwMTExNTQ2NjQ1MjQ0Mjc5NDYzNzMxMjYwODU5ODg0ODE1NzM2Nzc0OTE0NzQ4MzU4ODkwNjYzNTQzNDkxMzExOTkxNTIyMTYsMjM1NjI3MjM0NTcyNjczNDcwNjU3ODk1NDg5OTY3MDk5MDQ5ODg0Nzc1NDc4NTgzOTI2MDA3MTAxNDMwMjc1OTc1MDYzMzcyODMxNzg2MjIyMzk3MzAzNjU1Mzk2MDI2MDA1NjEzNjAyNTU1NjY0NjI1MDMyNzAxNzUwNTI4OTI1NzgwNDMyMTU1NDMzODI0OTg0Mjg3NzcxNTI0MjcwMTAzOTQ0OTY5MTg2NjQwMjg2NDQ1MzQxMjgwMzM4MzE0Mzk3OTAyMzY4Mzg2MjQwMzMxNzE0MzU5MjIzNTY2NDMyMTk3MDMxMDE3MjA3MTMxNjM1Mjc0ODcyOTg3NDc0MDA2NDc4MDE5Mzk1ODcxNjU5MzY0MDEwODc0MTkzNzU2NDkwNTc5MTg1NDk0OTIxNjA1NTU2NDcwODcsMTQxMDUzNzgzNzA2NzEyMDY5MDYzMjA3OTU4MDg2MDYzMTg5ODgxNDg2NzQzNTE0NzE1NjY3ODM4ODM4Njc1OTk5OTU0ODY3NzQyNjUyMzgwMTE0MTA0MTkzMzI5MDM3NjkwMjUxNTYxOTUwNTY4NzA5ODI5MzI3MTY0MDg3NzI0MzY2MzcwMDg3MTE2NzMxMjY4MTU5MzEzNjUyNDg3NDUwNjUyNDM5ODA1ODc3Mjk2MjA3Mjk3NDQ2NzIzMjk1MTY2NjU4MjI4ODQ2OTI2ODA3Nzg2NjUyODcwMTg4OTIwODY3ODc5NDUxNDc4MzY0NTY5MzEzOTIyMDYwMzcwNjk1MDY0NzM2MDczNTcyMzc4Njk1MTc2NDczMDU1MjY2ODI2MjUzMjg0ODg2MzgzNzE1MDcyOTc0MzI0NDYzODM1MzAwMDUzMTM4NDI5NDYwMjk2NTc1MTQzMzY4MDY1NTcwNzU5NTM3MzI4MjQy"

perfect_numbers = [
    6,
    28,
    496,
    8128,
    33550336,
    8589869056,
    137438691328,
    2305843008139952128,
    2658455991569831744654692615953842176,
    191561942608236107294793378084303638130997321548169216,
    13164036458569648337239753460458722910223472318386943117783728128,
    14474011154664524427946373126085988481573677491474835889066354349131199152128,
    23562723457267347065789548996709904988477547858392600710143027597506337283178622239730365539602600561360255566462503270175052892578043215543382498428777152427010394496918664028644534128033831439790236838624033171435922356643219703101720713163527487298747400647801939587165936401087419375649057918549492160555646976,
    141053783706712069063207958086063189881486743514715667838838675999954867742652380114104193329037690251561950568709829327164087724366370087116731268159313652487450652439805877296207297446723295166658228846926807786652870188920867879451478364569313922060370695064736073572378695176473055266826253284886383715072974324463835300053138429460296575143368065570759537328128
]


def solve():
    i = 0
    flag = "flag{"
    cipher = [int(v) for v in base64.b64decode(cipher_b64).decode().split(",")]
    while i < len(cipher):
        flag += chr(int(cipher[i]) ^ perfect_numbers[i])
        i += 1
    flag += "}"
    return flag


print(solve())

# FLAG --> flag{tHE_br0kEN_Xor}
