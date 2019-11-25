import requests
from pprint import pprint
import csv
import time
from decouple import config

BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
HEADERS = {
    'X-Naver-Client-id': CLIENT_ID,
    'X-Naver-Client-Secret': CLIENT_SECRET,
}

movie_list = []
query = '겨울왕국'
API_URL = f'{BASE_URL}?query={query}'
response = requests.get(API_URL, headers=HEADERS).json()
pprint(response)
# items_list = response.get('items')


# with open('movie.csv', 'r', newline='', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         query = row['영화명(국문)']
#         year = row['개봉연도'][0:4]
#         movieCD = row['영화 대표코드']
#         API_URL = f'{BASE_URL}?query={query}'
#         response = requests.get(API_URL, headers=HEADERS).json()
#         items_list = response.get('items')
#         for i in items_list:
#             if i.get('pubDate') == year and float(i.get('userRating')) > 1:
#                 temp_dict = {'영화 대표코드': movieCD, '영화명': query, '하이퍼텍스트 link': i.get('link'),'이미지의 URL': i.get('image'), '유저 평점': i.get('userRating')}
#                 movie_list.append(temp_dict)
#                 time.sleep(0.1)
                
# with open('movie_naver.csv', 'w', newline='', encoding='utf-8') as f:
#     fieldnames = ('영화 대표코드', '영화명', '하이퍼텍스트 link', '이미지의 URL', '유저 평점')
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     for movie in movie_list:
#         writer.writerow(movie)