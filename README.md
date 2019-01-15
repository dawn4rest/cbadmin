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
pyenv virtualenv로 다시 진행  

