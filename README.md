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

# 16.04에서 python 3.6이 없을 경우
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
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
pip install django-tagging  
pip install django-multiselectfield  
pip install pillow pilkit django-imagekit  
~~~
