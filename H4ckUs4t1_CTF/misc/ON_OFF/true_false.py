import binascii
f = open("chall.txt",'r')
binary=''
for i in range(0,144):
    linea = f.readline()
    if linea == "false\n":
        binary+='0'
    elif linea == "true\n":
        binary+='1'
print(binary)
#convert binary to ascii 
print(binascii.unhexlify('%x' % int(binary, 2)))

#ITT{tru3_0r_f4ls3}
#01001001 01010100 01010100 01111011 01110100 01110010 01110101 00110011 01011111 00110000 01110010 01011111 01100110 00110100 01101100 01110011 00110011 01111101