import requests
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
import csv
# datetime이라는 것을 또 import 해옴
# targetDt = datetime(2019, 7, 13) - timedelta(weeks=50)
# targetDt = targetDt.strftime('%Y%m%d') #yyyymmdd

key = 'cd2c190ee91d7749d95cc37fe488e4b3'
base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
movie_list = []

for j in range(50):
    targetDt = datetime(2019, 11, 24) - timedelta(weeks=j)
    targetDt = targetDt.strftime('%Y%m%d')
    api_url = f'{base_url}?key={key}&targetDt={targetDt}'

    response = requests.get(api_url)
    data = response.json()

    for i in range(10):
        # 여기서 나오는 정보를 사용하기 좋은 list나 dictionary 형태로 변형시켜줘야한다.
        dict_movie = {'movieCd' : data['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieCd'], 'movieNm': data['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieNm'], 'audiAcc': data['boxOfficeResult']['weeklyBoxOfficeList'][i]['audiAcc']}
        
        # 메인 리스트에서 for문을 돌려 새로 만든 dictionary와 value?
        for k in movie_list:
            if k['movieCd'] == dict_movie['movieCd']:
                movie_list.remove(k)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                # 하...... 이 쉬운걸 이제서야 했네.

        movie_list.append(dict_movie)

pprint(movie_list)

with open('movie2.csv', 'w', newline='', encoding='utf-8') as f:
    # 저장할 필드의 이름을 미리 지정한다.
    fieldnames  = ('movieCd', 'movieNm', 'audiAcc')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # 필드 이름을 csv 파일 최상단에 작성한다.
    writer.writeheader()

    # Dictionary 를 순회하며 key 값에 맞는 value를 한줄씩 작성한다.
    for movie in movie_list:
        writer.writerow(movie)