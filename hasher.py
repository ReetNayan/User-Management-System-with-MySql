import hashlib


def sha256(text,salt):

    unhash = text+salt
    result = hashlib.sha256(unhash.encode())
    hashedStr = result.hexdigest()

    return hashedStr