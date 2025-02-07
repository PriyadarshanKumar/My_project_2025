import requests
import redis

# API URL
api_url = "https://apis.rmlconnect.net/wba/management/v1/registration/redis-insert?debug=True"

# Authorization Token
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtbyIsInVzZXJuYW1lIjoiUkNXQlMiLCJleHAiOjIwNDk2MDM5MTcuNzcyLCJlbWFpbCI6ImFrYXNyYW5qYW5AZ21haWwuY29tIiwib3JpZ19pYXQiOjE1NzEwNDg0NjQsImN1c3RvbWVyX2lkIjoiOWlyNURnN2J2c0NBIiwiaWF0IjoxNzM4NTYzOTE3fQ.lvDQA6Sro3VB0aORJ1roBvxsBfDe7hkVsHXUFHMl3PY"
}

# Connect to local Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Define Hashmap name
hashmap_name = "WA_USER_DETAILS:919717079315"

try:
    # Fetch data from the API
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # Raise error for HTTP failures

    data = response.json()  # Convert response to JSON

    # Insert data into Redis hashmap
    for key, value in data.items():
        if isinstance(value, (dict, list)):
            value = str(value)  # Convert to a readable string
        elif isinstance(value, str):
            value = value.strip('"')  # Remove surrounding quotes if present
        
        r.hset(hashmap_name, key, value)

    print(f"Data successfully stored in Redis hashmap '{hashmap_name}'!")

    # Verify data insertion
    print(r.hgetall(hashmap_name))

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
