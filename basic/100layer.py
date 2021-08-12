from pwn import *
import json
import base64
import codecs
import random
from Crypto.Util.number import bytes_to_long, long_to_bytes
from binascii import unhexlify


#0x646973706c617965645f68656c6c6f5f68756e74696e67746f6e
r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)
    
def make_string(s):
    output = ""
    return(output.join(s))
    

def decode_it(estring,estringtype):
        encoding = estringtype
        if encoding == "base64":
           encoded = base64.b64decode(estring).decode('utf8').replace("'", '"')
           print(encoded)
        elif encoding == "hex":
            encoded = (unhexlify(estring)).decode('utf8').replace("'", '"')
            print(encoded)
        elif encoding == "rot13":
            encoded = codecs.decode(estring, 'rot_13')
            print(encoded)
        elif encoding == "bigint":
            encoded =  unhexlify(estring.replace("0x", "")).decode('utf8').replace("'", '"')
            print(encoded)
        elif encoding == "utf-8":
            encoded = make_string([chr(b) for b in estring])

            print(encoded)

        return encoded



r = json_recv()

print("Received type: ")
print(r["type"])
print("Received encoded value: ")
print(r["encoded"])




to_send = {
    "decoded": decode_it(r["encoded"],r["type"])
}
json_send(to_send)

json_recv()
