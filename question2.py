import hashlib
HASH_OBJ = hashlib.sha1(b'Hi Harsh ')
hex_dig = HASH_OBJ.hexdigest()
print(hex_dig)

HASH_OBJ = hashlib.sha224(b'Hi Harsh')
hex_dig = HASH_OBJ.hexdigest()
print(hex_dig)

HASH_OBJ = hashlib.blake2b(b'Hi Harsh')
hex_dig = HASH_OBJ.hexdigest()
print(hex_dig)