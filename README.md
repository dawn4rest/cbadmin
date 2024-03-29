# Requirements List(개발 당시 버전)
- Python 3.6.4
- Django 1.11.3
- pipenv
- pillow
- pilkit
- django-imagekit
- django-tagging
- django-multiselectfield

# AWS 구축
~~~
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
pip3 install pipenv
~~~

우분투 실행 경로에 pipenv 추가
~~~
vi ~/.profile

if [ -d "$HOME/.local/bin" ] ; then
    PATH="$PATH:$HOME/.local/bin"
fi
~~~

# Pipenv로 가상환경 관리
~~~
mkdir chatterbox
cd chatterbox
pipenv --python 3.6
pipenv shell
~~~

# 가상환경에서 프로젝트 clone
~~~
git clone http://github.com/dawn4rest/cbadmin.git
mv cbadmin src
cd src
~~~

# Django Requirements 설치
~~~
pipenv install django==1.11.3
pip install django-tagging django-multiselectfield pillow pilkit django-imagekit  
~~~

# Nginx & uWSGI 배포
> https://rainsound-k.github.io/deploy/2018/05/02/instance-setting-and-django-deploy-part2.html  
> 매우 큰 도움. 감사 설명들 친절한.

pipenv venv path 문제로 포기  
pyenv virtualenv 로 다시 진행  

# HTTPS SSL 설정
> http://blog.kimgihong.com/devlog/AWS_EC2_letsencrypt_SSL  
certbot 이 아니라 letsencrypt 로 SSL 관리, 자동 연장

# Allauth Social Login 연동
> Allauth 공식 문서: https://django-allauth.readthedocs.io/en/latest/providers.html#facebook  
> 가장 친절했던 설명: https://github.com/YeongBaeeee/practice/wiki/26-OAuth-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EA%B3%BC-%EB%8F%99%EC%8B%9C%EC%97%90-%EB%A1%9C%EA%B7%B8%EC%9D%B8. 
페이스북 콜백 URL 개 까탈스러움 후  
  
차단된 리디렉션 URI가 앱의 클라이언트 OAuth 설정의 화이트리스트에 없으므로 리디렉션하지 못했습니다.  
클라이언트 및 웹 OAuth 로그인이 설정되었는지 확인하고 모든 앱 도메인을 유효한 OAuth 리디렉션 URI로 추가하세요.  
  
괜히 화이트리스트 IP 헷갈려서 고치지 말자. 그냥 콜백 URL이 정확하지 않은 것. 
https://chatterboxes.kr/accounts/facebook/login/callback 이거로 해결.

# [중요] 쿼리셋 최적화
> https://blog.leop0ld.org/posts/django-query-optimization/  
게시물 5개에서 유사 및 중복 쿼리 508개 나옴  
게시물 목록 / 게시물 상세 / 유저 로그  
이 3개 뷰는 최적화가 필요해보이는데 시간 부족으로 최적화는 건드리지 못함  
일단 입사 후 짬이 나면 수정하거나 Node React로 이전 고려 중
