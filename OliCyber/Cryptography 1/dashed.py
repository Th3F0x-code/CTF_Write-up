import base64

morse = {
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-.-.-': '.',
    '--..--': ',',
    '---...': ':',
    '..--..': '?',
    '.----.': '\'',
    '-....-': '-',
    '-..-.': '/',
    '.-..-.': '"',
    '.--.-.': '@',
    '-...-': '=',
    '---.': '!'
}

text = '----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- .---- --..-- ----- -..- ...-- ----- --..-- ----- -..- ...-- .----'

text = text.split(' ')
flag = ''

for char in text:
    flag += morse[char]

flag = flag.split(',')

h = {
    '0x30': '0',
    '0x31': '1'
}

plaintext = ''

for char in flag:
    plaintext += h[char]

print(base64.b64decode(
    ''.join(chr(int(plaintext[i * 8: i * 8 + 8], 2)) for i in range(len(plaintext) // 8)).encode()).decode())