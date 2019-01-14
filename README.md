# Requirements List
- Python 3.5.2
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
pipenv --three
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
pipenv install django==1.11.3py
pip install django-tagging  
pip install django-multiselectfield  
pip install pillow  
pip install pilkit  
pip install django-imagekit  
~~~
