
import base64
import tempfile
import subprocess
import json
import multiprocessing
import sys
from random import getrandbits
import binascii
import codecs
import sha3
import hashlib

challenge, difficulty = sys.argv[1:]


if difficulty.startswith("0x"):
  difficulty = difficulty[2:]

difficulty = difficulty.zfill(64) # 

if challenge.startswith("0x"):
  challenge = challenge[2:]

account = "0x5294b9f7a71a97b703fa04ba3a415c8a136bdeb1"
if account.startswith("0x"):
  account = account[2:]

inputs = [challenge, account]
input_prefix = [ codecs.decode(x,'hex_codec') for x in inputs ]
input_prefix = b"".join(input_prefix) # binary sent to stdin


from binascii import unhexlify, b2a_base64

nonce = unhexlify(sys.stdin.read().strip())
import sha3
hash1 = sha3.keccak_256(input_prefix+nonce).hexdigest()
print('challenge',hash1)
