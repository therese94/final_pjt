from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Genre, Review, StarRate
from .serializers import MovieSerializer, MoviesSerializer
User = get_user_model()

import requests, csv
from datetime import datetime, timedelta
from decouple import config
from pprint import pprint
import bs4


@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(instance=movie)
    return Response(serializer.data)


def make_db(request):
    title_dict = {}
    for i in range(20):
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

            BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
            CLIENT_ID = 'm0YexGybNHVSbIufIkoM'
            CLIENT_SECRET = 'Wf5J1MVe_H'
            HEADERS = {
                'X-Naver-Client-id': CLIENT_ID,
                'X-Naver-Client-Secret': CLIENT_SECRET,
            }

            movie_list = []
            query = data['movieNm']
            # 이미 DB에 저장했다면 저장하지 않는다.
            if title_dict.get(query) == 1:
                continue

            API_URL = f'{BASE_URL}?query={query}'

            response = requests.get(API_URL, headers=HEADERS).json()
            
            try:
                response_items = response['items'][0]
            except IndexError:
                pass
            
            if response_items:
                # movie.poster_url = response_items.get('image')
                temp_link = response_items.get('link')
            # print(movie.poster_url)
            movie.title = data['movieNm']
            movie.audiAcc = data['audiAcc']
            title_dict[data['movieNm']] = 1

            new_response = requests.get(temp_link)
            html = new_response.text
            soup = bs4.BeautifulSoup(html, 'html.parser')
            
            poster_temp = soup.select('.poster img')[0]['src'].split('?')[0]
            movie.poster_url = poster_temp

            detail_content = soup.select('.con_tx')
            detail_content = detail_content[0].getText()
            movie.description = detail_content
            print(movie.poster_url)
            # print(movie.description)
            movie.save()

    return