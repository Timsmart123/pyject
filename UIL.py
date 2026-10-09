def teLoop(inp, datatype = str):
    while True:
        try:
            question = datatype(input(inp))

            if datatype == str and not question.strip():
                raise ValueError

            return question

        except ValueError:
            print("Not Valid")


# Harley pass hashing
import hashlib as hash
import os

import datetime as dt

def basic_validation(ipt):
    if ipt != KeyboardInterrupt and len(ipt) >= 1:
        return ipt
    else:
        return None

def hash_password(unhashed_password, **kwargs):
    salt = kwargs.get("salt", os.urandom(32)) # if no salt defined generate a random one

    key = hash.pbkdf2_hmac(
        "sha256", # hash algorithum
        unhashed_password.encode("utf-8"),
        salt,
        10000, # no. iterations (brute force prevention)
        dklen=128, # length of detrived key
    )

    return key