import libnacl

from hashlib import sha256
from base64 import b32encode

class Onion:    
    def generate(self):
        version = b'\x03'
        
        private_key = libnacl.randombytes_buf(libnacl.crypto_scalarmult_SCALARBYTES)
        public_key = libnacl.crypto_scalarmult_base(private_key)

        checksum = sha256(b'.onion checksum' + public_key + version).digest()[:2]
        onion = b'http://' + b32encode(public_key + checksum + version).lower() + b'.onion'

        return onion.decode()