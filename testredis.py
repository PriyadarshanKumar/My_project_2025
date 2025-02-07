import redis

client = redis.StrictRedis(host='localhost', port=6379, db=0)
# Use pipelining to send multiple commands in a single go
pipeline = client.pipeline()
pipeline.hgetall('WA_USER_DETAILS:RMLUAT11')
pipeline.hgetall('WA_USER_DETAILS:zarfwbs')
results = pipeline.execute()

# hash1_data, hash2_data = results

print(results)
# print(hash1_data)
# print(hash2_data)