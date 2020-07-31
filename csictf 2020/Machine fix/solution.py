def count3(n):
    sum = 0
    while n > 0:
        sum += n
        n //= 3
    return sum


print("csictf{" + str(count3(523693181734689806809285195318)) + "}")

# FLAG --> csictf{785539772602034710213927792950}
