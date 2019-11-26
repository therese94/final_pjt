import requests, csv
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
from movies.models import Movie

   
for i in range(10):

    targetDt = datetime(2019, 11, 24) - timedelta(weeks=(i))
    targetDt = targetDt.strftime('%Y%m%d')

    key = 'cd2c190ee91d7749d95cc37fe488e4b3'
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
    api_url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb=0'

    response = requests.get(api_url)
    datas = response.json()

    datas = datas['boxOfficeResult']['weeklyBoxOfficeList']

    for data in datas:
        movie = Movie()
        movie.title = data['movieNm']
        movie.audiAcc = data['audiAcc']
        movie.save()
        # temp = Movie(
        #     title = data['movieNm']
        #     audiAcc = data['audiAcc']
        # )
        # temp.save()
        # if data['movieCd'] in movieCd_list:
        #     continue
        # else:   
        #     writer.writerow(data_dict)    
        # movieCd_list.append(data['movieCd'])  
