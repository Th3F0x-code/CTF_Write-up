def get_plain(ct, key):
    plain = ''
    key = ''.join(key[i % len(key)] for i in range(len(ct)))
    for i in range(len(ct)):
        if ct[i] == '_':
            plain += ct[i]
            continue
        c = ord(ct[i]) - 97
        k = ord(key[i]) - 97
        if c > k:
            plain += chr(c - k + 97)
        elif c < k:
            plain += chr(26 - k + c + 97)
        else:
            plain += chr(c + 97)
    return plain


psuedo_key = "iigesssaemk"
ct = "z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut"

i = ['e', 'r']
g = ['d', 'q']
e = ['c', 'p']
s = ['j', 'w']
a = ['a', 'n']
m = ['g', 't']
k = ['f', 's']
possible_keys = []

for ii in i:
    for ii2 in i:
        for gg in g:
            for ee in e:
                for ss in s:
                    for ss2 in s:
                        for ss3 in s:
                            for aa in a:
                                for ee2 in e:
                                    for mm in m:
                                        for kk in k:
                                            test = ii + ii2 + gg + ee + ss + ss2 + ss3 + aa + ee2 + mm + kk
                                            possible_keys.append(test)

for key in possible_keys:
    plain = get_plain(ct, key)
    print(plain)

# FLAG --> flag{i_guess_pseudo_keys_are_pseudo_secure}
