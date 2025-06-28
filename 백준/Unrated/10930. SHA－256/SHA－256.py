import hashlib

data = input()

hash_object = hashlib.sha256()

hash_object.update(data.encode())

hash_value = hash_object.hexdigest()

print(hash_value)