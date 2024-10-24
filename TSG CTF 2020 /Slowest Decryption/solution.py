import json
from math import gcd

from rich.progress import track

MOD = 69366296890289401502186466714324091327187023250181223675242511147337714372850256205482719088016822121023725770514726086328879208694006471882354415627744263559950687914692211431491359503896279403796581365981225023065749656346527652480289235008956593933928571457700779656030733229310882472880060831832351425517


def solve(c):
    N = len(c)
    dp = [0] * N
    dp[0] = 1
    for i in range(N - 1, 0, -1):
        u = (N - 1) // i + 1
        dp[i] = pow(u, N - 1, MOD) - dp[0]
        for j in range(i + i, N, i):
            dp[i] -= dp[j]
        dp[i] %= MOD
    res = 0
    for i in track(range(N)):
        s = 0
        for g in range(N):
            s += dp[g] * gcd(g, i) % MOD
            if s >= MOD:
                s -= MOD
        res += c[i] * s % MOD
        if res >= MOD:
            res -= MOD
    return res * (N * (N - 1) // 2) % MOD


with open('encrypted.json') as f:
    encrypted = json.load(f)
flag = solve(encrypted)
print(flag.to_bytes((flag.bit_length() + 7) // 8, byteorder='big').decode())

# FLAG --> TSGCTF{GRE4T!_y0u_Found_n1c3_decription_Alg0r1thm_or_you_h4ve_aston1shing_Fa5t_c4lcul4t0r}
