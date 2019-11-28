from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Review, StarRate
from .serializers import MovieSerializer, MoviesSerializer, ReviewSerializer
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

@api_view(['POST'])
def create_review(request, movie_id, user_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = get_object_or_404(User, pk=user_id)
    reviews = movie.reviews.all()
    for review in reviews:
        if str(review.user) == user.username:
            return Response({'message':'Comment is existed'})
    review = Review()
    review.movie = movie
    review.user = user
    review.score = request.data['score']
    review.content = request.data['content']
    review.save()
    serializer = ReviewSerializer(instance = review)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return Response(status=204)

@api_view(['GET'])
def review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = movie.reviews.all()
    serializer = ReviewSerializer(instance=reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    serializer = ReviewSerializer(instance=review)
    return Response(serializer.data)
    
def make_db(request):
    title_dict = {}
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
                temp_link = response_items.get('link')
            movie.title = data['movieNm']
            movie.audiAcc = data['audiAcc']
            title_dict[data['movieNm']] = 1

            new_response = requests.get(temp_link)
            html = new_response.text
            soup = bs4.BeautifulSoup(html, 'html.parser')


            detail_content = soup.select('.con_tx')
            detail_content = detail_content[0].getText()

            temp_rating = soup.select('.st_on')[0].getText()[-5:-1]
            temp_genres = soup.select('.info_spec')[1].find('span').find('a').getText()
          

            poster_temp = soup.select('.poster img')[0]['src'].split('?')[0]
            movie.description = detail_content
            movie.poster_url = poster_temp
            movie.audiRating = float(temp_rating)
            movie.genres = temp_genres

            # print(detail_content)
            # print(poster_temp)
            # print(temp_rating)
            print(temp_genres)
            movie.save()
            

            # ########################################################
            # flag = 0
            # genres = Genre.objects.all()
            # for g in genres:
            #     if str(g.name) == temp_genres:
            #         genre = get_object_or_404(Genre,name=temp_genres)
            #         flag = 1
            #         break

            # if flag == 0:
            #     genre = Genre()
            #     genre.name = temp_genres
            #     genre.save()    
            # print(genre)
            # movie.save()
            # movie.genres.add(genre)
            # print(movie.genres)
            ##############################################################

        

    return