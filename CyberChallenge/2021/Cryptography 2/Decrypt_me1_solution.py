n = 5582983442520038683
e = 65537
c = [4241158327675851879, 4241158327675851879, 5354489610922786464, 4550738158389426310, 4665662406419402733,
     3736594563003291531, 323653105751856648, 4703388441175874733, 5363019606146104279, 3143962585538422543,
     3488820451902874497, 123964607634809096, 747696344002322146, 296392603807014516, 5363019606146104279,
     747696344002322146, 2760000353975742240, 5363019606146104279, 1022394867374906972, 123964607634809096,
     323653105751856648, 4183060581760535428, 296392603807014516, 5363019606146104279, 4703388441175874733,
     323653105751856648, 747696344002322146, 3082072561190179323, 323653105751856648, 324335115885569813,
     3685077408869721674]


# function used to find the prime numbers (p,q)
def print_divisors(number):
    for _ in range(1, int(number ** 0.5)):
        if number % _ == 0:
            print(_)


p = 2357345743
q = 2368334581
tot = (p - 1) * (q - 1)
d = pow(e, -1, tot)
for i in range(len(c)):
    m = ''.join(chr(pow(el, d, n)) for el in c)
print("Flag: " + m)

# FLAG --> CCIT{d3crypt_0r_brut3f0rc3_m3?}