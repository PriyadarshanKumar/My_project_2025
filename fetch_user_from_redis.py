import requests
import jwt
import traceback

try:
    url = 'https://apis.rmlconnect.net/wba/management/v1/registration/redis-insert?debug=True'

    url_toget_all_user_from_redis ='https://apis.rmlconnect.net/wba/reports/v1/redis_usernames'

    header = {
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGVtbyIsInVzZXJuYW1lIjoicm91dGVtb2JpbGUtc3VwZXJ1c2VyIiwiZXhwIjoxNzQ0ODgwMTYxLjAzNCwiZW1haWwiOiJha2FzcmFuamFuQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTcxMDQ4NDY0LCJjdXN0b21lcl9pZCI6IjlpcjVEZzdidnNDQSIsImlhdCI6MTcxMzc3NjE2MX0.tAHxftN-rlS6OQCYakGeoMQEMhfcXgr5qZZ_XE6-kkM'
        }
    
    redis_res = requests.get(url_toget_all_user_from_redis, headers=header)

    user_data = redis_res.json()
    users_in_redis = []
    
    for user in user_data.items():
        users_in_redis.append(user)

    username_list = users_in_redis[2][1]
    print(username_list)

    usernames_with_timezone = []
    # username = ['KCGAHD', 'RMLUAT11', 'SAPPHIREFOODS', 'SamsungUAT1', 'phfs', 'samsunghs', 'samsungsc', 'yayasan']
    
    

    for user in username_list:
        data = {
        "user_id": f"{user}",
        "username": f"{user}",
        "exp": 1886408464,
        "email": "akasranjan@gmail.com",
        "orig_iat": 1571048464,
        "customer_id": "9ir5Dg7bvsCA"
        }

        auth_token = jwt.encode(data, "RML_SECRET", algorithm="HS256")

        headers = {
                    'Authorization': auth_token
                }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            for user_data in data.items():
                if 'user_timezone' in user_data:
                    usernames_with_timezone.append(user)
                    usernames_with_timezone.append(user_data[1])
        else:
            print(f"Failed with status code {response.status_code}:")
            print(response.text)

        print("Usernames with 'user_timezone' key:")
        print(usernames_with_timezone)

except IndexError as e:
   traceback.print_exc()
