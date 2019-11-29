# Mooving Readme

## 프로젝트 목표

1) 영화 추천 사이트를 운영한다.

2) 백엔드 Django REST API 서버 와 프론트엔드 프레임워크(Vue) 분리하여 진행한다.

3) 추천 알고리즘을 통하여 사이트 내에 다른 유저가 좋아하는 영화와, 팔로우한 유저가 좋아하는 영화를 보여준다.

## 기초 Settings

## movie-front setting

```bash
$ npm install -g vue
$ npm i -g @vue/cli
$ npm i axios
$ npm i bootstrap bootstrap-vue
$ npm install -g webpack
$ npm i vue-session
$ npm i jwt-decode
$ npm i vue-loader
```

## movie-back setting

```bash
$ pip install django
$ pip install djangorestframework
$ pip install djangorestframework-jwt
$ pip install django-cors-headers
$ pip install python-decouple
$ pip install beautifulsoup4
```



## i. 팀원 정보 및 업무 분담

김혜준 : 캐릭터 디자인 및 Vue Frontend Component 관리. DB 구축

김강현 : DJango REST API 서버 구축 및 Vuejs 와 연결.



## ii. 목표 서비스 구현 및 실제 구현 정도 (가능하다면 일자별 업무 진행 정도 포함)

## 11/24 작업

1. 노트북에서 node.js 설치.
2. node.js의 path 시스템 환경 변수 편집.
3. front-end part npm 필요한거 설치.
4. back-end part django pip install.
5. axios의 get method를 통해서 django restframework로 구성된 API에서 정보 요청.
6. vue에서 API에서 제공된 정보 나타내기.

## 11/25 작업

1. 노트북에서 작업한거 컴퓨터로 가져오기.
2. Django 프로젝트에서 Movie, Review, User 모델링.
3. Vue 에서 모델링한 것 간단하게 나타내기.
4. StartCamp 때 배운 파이썬 Crawling 기법으로 Movie data DB에 저장.
5. 팝콘 캐릭터 디자인.
6. 프로젝트 네이밍 완료.

## 11/26 작업

1. 회원가입, 로그인, 로그아웃 구현.
2. About view를 MovieList, MovieListItem component로 분리 구성.
3. FindBar component로 검색 기능 구현.
4. Modal 사용해서 팝업식으로 뜨게끔 구현.

## 11/27, 28 작업

1. 추천알고리즘 구현.
2. 팔로우 기능 구현.
3. 볼래요 기능 구현.
4. Mypage에서 볼래요 한 영화 확인 가능.
5. Mypage에서 팔로우한 사람이 볼래요한 영화 확인 가능.
6. 평점 및 리뷰에 따라 보고싶은 영화 메인에 추천해주기.

## iii. 데이터베이스 모델링(ERD)

User - Movie 1:1 관계

Movie - Review 1: N 관계

User - User 팔로우 기능으로 N : N 관계

## iv. 핵심 기능

1. 사용자의 이목을 끌고 친근하게 다가오는 매력적인 디자인.
2. REST API를 통한 백엔드와 VUE를 통한 프론트엔드의 분리를 통하여 조작하기 쉬운 Single Page Application
3. 팔로우한 유저가 있다면 팔로우한 유저가 재밌게 본 영화를 추천.
4. 유저 정보가 없다면 통상적으로 다른 사용자들이 재미있게 관람한 영화를 추천.
5. 볼래요 기능으로 장바구니에 담아놓고 나중에 열람할 수 있도록 구현.

## v. 배포 서버 URL
