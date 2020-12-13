import requests
from requests.api import head
import pprint
import pandas as pd
api_key = 'a409e4fb6fc1046e53df601d78fcb68b'
api_key_v4 = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNDA5ZTRmYjZmYzEwNDZlNTNkZjYwMWQ3OGZjYjY4YiIsInN1YiI6IjVmY2Y3N2MzZmJhNjI1MDAzZTdkNDk3NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jO4AaXE7grRC16BeB8Fjv1Lg39uvAS0Sn19MrRtUjcQ'

movie_id = 500
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/movie/{movie_id}'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}'

# print(endpoint)
# r = requests.get(endpoint)
# print(r.status_code)
# print(r.text)


# using v4
movie_id = 500
api_version = 4
api_base_url = f'https://api.themoviedb.org/{api_version}'

endpoint_path = f'/movie/{movie_id}'

endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}'
headers = {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8',
}
# print(endpoint)
# r = requests.get(endpoint, headers=headers)
# print(r.status_code)
# print(r.text)


api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = '/search/movie'
search_query = 'The Matrix'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}'
r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        # print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            print(result['title'], _id)
            movie_ids.add(_id)
        # print(print(movie_ids))

for movie_id in movie_ids:
    api_version = 3
    api_base_url = f'https://api.themoviedb.org/{api_version}'
    endpoint_path = f'/movie/{movie_id}'
    endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}'
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)
    print(r.json())
