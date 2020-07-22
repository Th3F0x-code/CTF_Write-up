cipher = '¤Ä°¤ÆªÔ\x86$\xa04\x9cÌ`H\x9c¬>¼f\x9c¦@HH\xa0\x84¨\x9a\x9a¢vÐØ'


def decrypt(text):
    ret_text = ''
    for i in list(text):
        couter = text.count(i)
        ret_text += chr(int((ord(i) + len(text)) / 2))
    return ret_text


print(decrypt(cipher))
