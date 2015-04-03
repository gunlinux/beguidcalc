import hashlib


def get_beguid(steamid):
    temp = "BE"
    for _ in range(8):
        temp += chr((steamid & 0xFF))
        steamid >>= 8
    return hashlib.md5(temp).hexdigest()
