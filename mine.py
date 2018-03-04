
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


tmpfilename = "myfile"
tmpf = open(tmpfilename, 'wb')
tmpf.write(input_prefix)
tmpf.close()

difficulty_filename = 'difficulty_filename'
cf = open(difficulty_filename, 'wb')
difficulty_raw = codecs.decode(difficulty, 'hex_codec')
cf.write(difficulty_raw)
cf.close()


subprocess.call(["./sha3", tmpfilename, difficulty_filename])
hashme = open('out.binary','rb').read()
print(repr(base64.b16encode(hashme[-32:]))[2:-1])
