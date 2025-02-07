import redis
import json

# Path to your JSON file
json_file_path = '/home/priyadarshan.kumar/RMLUAT11_hashmap.json'

# Read and parse the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Name of the Redis hash
hash_name = 'WA_USER_DETAILS:RMLUAT11'

# Save each key-value pair to the Redis hash
for key, value in data.items():
    r.hset(hash_name, key, value)

# Verify the saved data
saved_data = r.hgetall(hash_name)
print(saved_data)
