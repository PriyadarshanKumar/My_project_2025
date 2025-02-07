import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# Fetch all WABA ID mappings from Redis
waba_mapping = r.hgetall("WABA_ID_MAPPING")

# Convert bytes to string (Redis stores data as bytes)
waba_mapping = {k.decode(): v.decode() for k, v in waba_mapping.items()}

reverse_mapping = {}

for username, waba_id in waba_mapping.items():
    if waba_id in reverse_mapping:
        reverse_mapping[waba_id].append(username)
    else:
        reverse_mapping[waba_id] = [username]

print(reverse_mapping)
