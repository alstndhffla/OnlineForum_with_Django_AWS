-------------------------------------------------------------------------------

서버 프로그래밍 언어
Python 3
프레임워크
Django
데이터베이스
PostgreSQL
프론트엔드
JQuery
Bootstrap 4
OS
Ubuntu
웹서버
Nginx
WSGI 서버
Gunicorn
호스팅
AWS-Lightsail

-------------------------------------------------------------------------------

- 명령 프롬프트에서 'mysite' 입력하면 장고 가상환경으로 자동 연결(배치파일 환경변수 등록함)

- 부트스트랩 4.5.3 버전 다운로드: getbootstrap.com/docs/4.5/getting-started/download 사용. 버전5 x
파일의 압축을 해제 후, 이 중에서 bootstrap.min.css 파일만 복사해 mysite/static 디렉터리에 저장.

- 부트스트랩에 필요한 파일 추가 - 제이쿼리
C:/projects/mysite/static/jquery-3.6.0.min.js

-------------------------------------------------------------------------------

- 장고 ORM을 이용해 데이터베이스를 제어

- 부트스트랩, 제이쿼리 등 사용

- 상용게시판 수준
마크다운
로그인/로그아웃
회원가입
게시물 수정삭제
검색, 정렬
좋아요 기능
네비게이션 바 
게시물 수정삭제
게시판 페이징
스크롤 초기화(앵커엘리먼트)

-------------------------------------------------------------------------------

- 깃으로 소스 관리

- AWS 라이트세일로 서비스 배포
	인스턴스 생성 - 리눅스(우분투20.04LTS) - Ubuntn-1	

------------------------------------------------------------------------------

- AWS 서버 관리 (ubuntu@ip-172-26-14-116:~$ 프롬프트에서 '~'는 홈 디렉터리인 /home/ubuntu를 의미)

****서비스에 필요한 설정, 서버 실행

1. date 입력시 현재 서버의 시각이 호출
2. 한국 시간으로 서버 시간 수정
sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
3. python 입력으로 설치되어있는지 확인 -> 이후 python3 입력하면 
파이썬 셸이 실행되면서 '>>>' 나타남(파이썬이 정상적으로 설치되었다는 의미) -> exit() 로 종료
4. 가상환경 설정 패키지 설치 전 sudo apt update 입력으로 우분투 패키지 최신화
5. 가상환경 사용할 수 있도록 sudo apt install python3-venv 입력.
6. 홈 디렉터리 하위에 projects, venvs 디렉터리 생성
	mkdir projects
	mkdir venvs
	ls	(홈 하위에 있는 디렉터리 확인 명령어)
7. cd venvs 입력 (venvs 디렉터리로 이동해 장고 가상 환경을 생성하기 위함)
	이후 python3 -m venv mysite 입력(가상환경 생성)
	이후 cd mysite 입력(가상환경으로 진입)
	*** (/home/ubuntu/venvs/mysite/bin 이동 후 '. activate' 을 입력하면 가상환경으로 진입할 수 있다.)
	cd bin 입력
	. activate 입력
8. 가상환경 진입 완료 상태 확인
	(mysite) ubuntu@ip-172-26-14-116:~/venvs/mysite/bin$

9. wheel 패키지를 먼저 설치 - 서버환경에서 pip 으로 프로젝트 관련 패키지 설치시 해당
	패키지 관련 오류 발생함.
	pip install wheel 입력
	(mysite) ubuntu@ip-172-26-14-116:~/venvs/mysite/bin$ pip install wheel

10. django 에 필요한 패키지 2개 설치	
	pip install django==3.1.3
	pip install markdown

11. 깃허브 저장소를 가져오기 위해 projects 디렉터리로 이동(원격 저장소의 파일 받기)
	(mysite) ubuntu@ip-172-26-14-116:~/venvs/mysite/bin$ cd ~/projects

12. https://github.com/alstndhffla/OnlineForum_with_Django_AWS.git(깃헙 주소)
	(mysite) ubuntu@ip-172-26-14-116:~/projects$ git clone 깃헙 주소 mysite
	*mysite 를 뒤에 꼭 입력해줘야 해당 이름으로 폴더가 생성되며 그 안에 파일들이
	 들어간다

13. (mysite) ubuntu@ip-172-26-14-116:~/projects$ ls 입력해 mysite 디렉터리가 생성됐
	는지 확인한다.

14. mysite 디렉터리에 진입해 장고 서버를 실행.
	(mysite) ubuntu@ip-172-26-14-116:~/projects$ cd mysite
	(mysite) ubuntu@ip-172-26-14-116:~/projects/mysite$ python manage.py runserver

15. 장고 서버는 실행되도 python manage.py migrate 명령을 수행하라는 메시지를 볼 수도
	 있다. ctrl+c 로 서버를 종료하고 위 명령어를 입력해 apply 시킨 후 다시
	서버를 실행시켜라.
	 
**** 고정 IP 생성(포럼에 접속하려면 필요함)
1. 네트워킹 탭 - 고정 IP 생성 - 인스턴스에 연결(ex. Ubuntu-1) - 생성
	3.34.54.66 (퍼블릭 고정 IP 주소가 생성됨)

**** 방화벽 설정(외부에서 접근하려면 해제해줘야한다)
1. 인스턴스에서 해당 서버(Ubuntu-1) 클릭.
2. 네트워킹 탭 - 아래 IPv6 방화벽 섹터에 '규칙추가' 클릭
3. forum 서버는 포트번호 8000번이므로 포트 또는 범위에 8000 입력 후 '생성' 클릭
4. 장고서버 다시 구동 (ex. cd .. 직전 경로가기)
	ubuntu@ip-172-26-14-116:~$ cd ~/venvs/mysite/bin
	ubuntu@ip-172-26-14-116:~/venvs/mysite/bin$ . activate
	(mysite) ubuntu@ip-172-26-14-116:~/venvs/mysite$ cd ~/projects/mysite
	(mysite) ubuntu@ip-172-26-14-116:~/projects/mysite$

	**** 장고 서버가 종료되지 않은 상태에서 터미널이 종료되었으면 이미 실행중인
	 장고 서버 프로세스를 종료해야한다. Error: That port is already in use. 이런 오류발생할 수 있음.
	killall python 입력. ****
	
	그리고 python manage.py runserver 0:8000 입력
5. git config credential.helper store 입력하면 깃허브 인증 절차를 생략

6. 고정 ip 를 얻으면 C:\projects\mysite\config\settings.py 에 ALLOWED_HOSTS 값에 넣어줘야한다.

**** 로컬PC에서 코드 수정 후 깃으로 AWS 에 파일 내려받기
	코드 작업 후 내 로컬pc에서	
	(mysite) c:\projects\mysite>git add *
	(mysite) c:\projects\mysite>git commit -m "~~~"
	(mysite) c:\projects\mysite>git push

	이후 AWS 터미널로 다시 돌아와

	(mysite) ubuntu@ip-172-26-14-116:~/projects/mysite$ git pull 를 입력.
	
	이후 다시 AWS 터미널에서 서버 실행.
	python manage.py runserver 0:8000 입력.

7. 이후 누구든지 3.34.54.66:8000 을 주소창에 넣으면 forum 에 접속할 수 있다.(고정 IP + 포트번호)


8. 서버와 개발환경을 분리
서버의 고정 아이피를 setting.py 에 등록했기 때문에 이제 기존 localhost:8000 로는 접속할 수 가 없다.
그래서 setting.py을 구분해줘야 한다.
settings이라는 폴더에 base.py 와 local.py, prod.py 로 나누어 사용한다.

(mysite) c:\projects\mysite>python manage.py runserver --settings=config.settings.local
이렇게 입력해야 개발환경에서 기존 로컬서버를 사용할 수 있음.
**** 개발환경 자동화 DJANGO_SETTINGS_MODULE
	set DJANGO_SETTINGS_MODULE=config.settings.local 입력
	python manage.py runserver  기존처럼 입력해 사용할 수 있음.
	
	**** 장고의 가상환경이 설치된 venvs 폴더 안 배치파일 C:\venvs\mysite.cmd 수정 
		set DJANGO_SETTINGS_MODULE=config.settings.local 입력하면 기존 환경변수와 맞물려
		개발환경에서 set DJANGO_SETTINGS_MODULE=config.settings.local 를 입력할 필요조차
		없다.

AWS 서버 환경에서는
python manage.py runserver 0:8000 --settings=config.settings.prod 를 입력해야 한다.
**** 로컬 개발환경의 파일들이 바꼈으니 git 으로 추가하고 AWS 서버에서 다시 받아야 한다.
	**** 서버 설정 자동화
		개발환경의 mysite.cmd 활용처럼 mysite.sh 파일을 작성해 가상환경진입과 환경변수설정을
		자동화할 수 있다(nano 편집기)
		cd /home/ubuntu/venvs/
		nano mysite.sh 입력 후 뜬 화면에서
		

		#!/bin/bash

		cd ~/projects/mysite
		export DJANGO_SETTINGS_MODULE=config.settings.prod
		. ~/venvs/mysite/bin/activate


		위 4줄 전체를 입력 후 ctrl+o 로 저장한 뒤 ctrl+x 로 편집기를 종료.
		이후 AWS 터미널 환경에서 
		cd ~/venvs 이동 후
		. mysite.sh 를 입력하면 해당 환경을 인식하고 가상환경을 연결해준다.
		(mysite) ubuntu@ip-172-26-14-116:~/projects/mysite$  이렇게 뜸.
		이후 python manage.py runserver 0:8000 을 하면 기존처럼 정상적으로 forum을
		접속할 수 있다.

------------------------------------------------------------------------------

- MobaXterm 사용.
AWS 라이트세일 터미널이 자주 끊기는 것 같아 불편. 그래서 해당 애플리케이션으로 AWS ssh 키를 받아
서버에 접속할 예정.

1. AWS 라이트세일 계정에서 ssh 키를 다운받아 c드라이브 venvs 폴더에 넣고
	c:\venvs>rename LightsailDefaultKey-ap-northeast-2.pem mysite.pem 입력해 파일명을 바꾼다.
2. mobaxterm.mobatek.net/download.html 프로그램 다운받고 session 에 host 랑 ssh 키 찾아서 넣으면
	접속된다.

* 이제부터 서버관련 명령은 해당 프로그램을 사용해서 입력하면 된다!

------------------------------------------------------------------------------

- 웹 브라우저와 웹서버 관계

브라우저 -> 웹 서버 -> 동적요청 -> WSGI(위스키)서버(Gunicorn) -> Django(WSGI 애플리케이션)
		          ㅣ					 l
		      정적파일				 데이터베이스(동적파일)
	   	     .css .js .png .jpg			  ex. 요청할 때마다 값이 바뀔 수 있는 것들

**** Gunicorn 설치(운영을 위한 도구이므로 AWS 서버에만 설치하면 된다)
	(mysite) ubuntu@ip-172-26-14-116:~/projects/mysite$ pip install gunicorn
	이후 gunicorn --bind 0:8000 config.wsgi:application 입력(서버 실행명령어) -> URL 에 http://3.34.54.66:8000/ 입력시 forum 접속가능

	****
	(해당 명령어의 의미는 8000번 포트로 WSGI 서버를 수행, 
	WSGI 서버가 호출하는 WSGI 애플리케이션이 config/wsgi.py 파일의 application 이라는 의미다.)	
	(해당 명령어로 서버가 실행이 안된다면 sudo fuser -k 8000/tcp 다시 입력해  8000 사용을 죽이고
	재입력하면 서버가 실행된다.)	
	****
		
	이후 URL(http://3.34.54.66:8000/forum/)을 입력해 forum에 들어가보면 기존에 정적파일들이 
	적용되어있지 않은 상태로 보일 것이다. 이는 Gunicorn 은 정적파일을 제대로 읽지 못하기 때문이다.
	이 정적파일은 웹서버(Nginx)를 사용해 해결한다.

	현재 Forum 의 서버는 Unix 계열의 시스템(우분투)이기 때문에 포트(8000)를 이용하는 것보다
	유닉스 소켓(Unix socket)을 사용하는 것이 더 빠르며 효율적이다.	
	gunicorn --bind unix:/tmp/gunicorn.sock config.wsgi:application 입력.

	*****************
	유닉스 소켓 방식으로 Gunicorn 서버를 실행하면 단독으로 Gunicorn 서버에 접속/실행할 수 없다. 
	해당 Gunicorn 서버는 Nginx와 같은 웹 서버에서 유닉스 소켓으로 WSGI 서버에 접속하도록 설정해야 한다.
	*****************
	
	Gunicorn을 자동으로 실행(시작, 중지)하기 위해서 AWS 서버에 서비스로 등록(환경변수, 서비스파일 작성)
	서버에서 nano 편집기를 이용하여 작성한다.
	*환경 변수 파일 
	/home/ubuntu/venvs/mysite.env - 파일내용 : DJANGO_SETTINGS_MODULE=config.settings.prod
	*서비스 파일
	sudo nano mysite.service 입력 후 아래 내용을 등록해 저장한다.
	
	[Unit]
	Description=gunicorn daemon
	After=network.target

	[Service]
	User=ubuntu
	Group=ubuntu
	WorkingDirectory=/home/ubuntu/projects/mysite
	EnvironmentFile=/home/ubuntu/venvs/mysite.env
	ExecStart=/home/ubuntu/venvs/mysite/bin/gunicorn \
	        --workers 2 \
	        --bind unix:/tmp/gunicorn.sock \
	        config.wsgi:application
	[Install]
	WantedBy=multi-user.target
	
	*서비스 실행 및 등록
	(mysite) ubuntu@ip-172-26-14-116:/etc/systemd/system$ sudo systemctl start mysite.service
	입력 후
	
	sudo systemctl status mysite.service 입력했을 시
	아래와 같은 메시지가 나와야 실행된거다.

	● mysite.service - gunicorn daemon
	   Loaded: loaded (/etc/systemd/system/mysite.service; disabled; vendor preset: enabled)
	   Active: active (running) since Thu 2020-04-23 12:12:27 UTC; 1s ago
	 Main PID: 26513 (gunicorn)
	    Tasks: 3 (limit: 547)
	   CGroup: /system.slice/mysite.service
	           ├─26513 /home/ubuntu/venvs/mysite/bin/python3 /home/ubuntu/venvs/mysite/bin/gunicorn --workers 2 --bind unix:/tmp/gunicorn.sock config.wsgi:application
	           ├─26534 /home/ubuntu/venvs/mysite/bin/python3 /home/ubuntu/venvs/mysite/bin/gunicorn --workers 2 --bind unix:/tmp/gunicorn.sock config.wsgi:application
	           └─26536 /home/ubuntu/venvs/mysite/bin/python3 /home/ubuntu/venvs/mysite/bin/gunicorn --workers 2 --bind unix:/tmp/gunicorn.sock config.wsgi:application

	* AWS 서버가 재시작시 Gunicorn 자동실행 설정
	sudo systemctl enable mysite.service (자동실행) -> 이걸 입력하면 된다.
	sudo systemctl stop mysite.service (종료)
	sudo systemctl restart mysite.service	(서비스 재시작)

**** AWS 서버에 Nginx 사용법.
1. 설치
	~/projects/mysite$ sudo apt install nginx 입력
2. 설정(cd /etc/nginx/sites-available 이동)
	sudo nano mysite 입력 - Nginx의 설정 파일을 mysite라는 이름으로 아래와 같이 작성 
	
	server {
	        listen 80;
	        server_name 3.34.54.66;

	        location = /favicon.ico { access_log off; log_not_found off; }

	        location /static {
	                alias /home/ubuntu/projects/mysite/static;
	        }

	        location / {
            	    include proxy_params;
	                proxy_pass http://unix:/tmp/gunicorn.sock;
	        }
	}

	****
	http 프로토콜 기본 포트 80, 내 서버 고정 ip 3.34.54.66, /static 은 Nginx 가 해당 디렉터리의 파일을 읽어
	처리한다는 뜻.
	location / 은 static 외에 모든 요청은 Gunicorn이 처리한다는 동적 요청 설정. proxy_pass 는 Gunicorn의
	유닉스 소켓 경로.
	****

3. Nginx 위에 설정한 mysite 파일 읽도록 설정
	(mysite) ubuntu@ip-172-26-14-116:/etc/nginx/sites-available$ cd /etc/nginx/sites-enabled/ 입력.
	ls 입력 후 default 파일 있는지 확인.
	sudo rm default 입력 - mysite 파일 링크를 위해 default 링크를 삭제 
	sudo ln -s /etc/nginx/sites-available/mysite 입력 - mysite 파일 링크

4. Nginx 다시 시작(pip 으로 설치할 때 자동실행되므로 설정을 새롭게 했으니 재시작해줘야 한다.)
	(mysite) ubuntu@ip-172-26-14-116:/etc/nginx/sites-enabled$ sudo systemctl restart nginx 입력

	****
	sudo nginx -t	(설정 파일 오류 확인 명령어)
	sudo systemctl stop nginx (종료)
	sudo systemctl start nginx (시작)
	****	

5. Gunicorn 과 Nginx 설치를 다 했기 때문에 url에 포트 번호(8000) 없이도 http://3.34.54.66/ 만으로 forum 에 
	접속할 수 있다.

-------------------------------------------------------------------------------

- 장고 Admin(서버용)
(mysite) ubuntu@ip-172-26-14-116:~/projects/mysite$ python manage.py createsuperuser 입력
이름: admin
비밀번호: admin


장고에 내장된 개발 서버는 장고 Admin이 사용될 때 자동으로
/home/ubuntu/venvs/mysite/lib/python3.6/site-packages/django/contrib/admin/static
여기서 정적파일을 읽고

Nginx는 /home/ubuntu/projects/mysite/static 여기서 정적파일을 읽는다.

그래서 http://3.34.54.66/admin 입력 후 보이는 브라우저는 스타일깨져서 나타남.

이를 해결하기 위해서는 장고 환경설정 파일에 STATIC_ROOT 디렉터리를 설정하고 
관리자 앱의 정적 파일을 STATIC_ROOT 디렉터리로 복사해야한다.
(C:\projects\mysite\config\settings\prod.py 와 base.py 를 확인)

* 서버의 프로그램이 변경됐을 땐 git pull 을 이용해 최신화 하고 Gunicorn 을 항상 재시작해줘야 한다.
	(mysite) ubuntu@ip-172-26-14-116:~/projects/mysite$ sudo systemctl restart mysite.service

		****
		[개발 환경에서 프로그램이 변경된 경우]

		git add *
		git commit -m "수정내용 코멘트"
		git push

		[서버 환경에서 변경된 내용 적용]

		git pull
		sudo systemctl restart gunicorn.service
		****

서버환경으로 변경된 파일들을 받아왔으니 해당 파일들을 서버가 제대로 읽을 수 있도록 
디렉터리에 복사해줘야 한다(정적 파일이 /home/ubuntu/projects/mysite/static 디렉터리로 복사될 것)
(mysite) ubuntu@ip-172-26-14-116:~/projects/mysite$ python manage.py collectstatic

-------------------------------------------------------------------------------

- 로그파일 등록/설정 -> base.py 확인
* 서버환경에서 로그확인하는 방법 
(mysite) ubuntu@ip-172-26-14-116:~/projects/mysite$ cd logs
(mysite) ubuntu@ip-172-26-14-116:~/projects/mysite/logs$ cat mysite.log

cat 대신에 tail -f mysite.log를 주로 사용. 
tail -f mysite.log를 실행하면 mysite.log 파일에 로그가 쌓일 때마다 로그의 내용이 자동으로 출력.


-------------------------------------------------------------------------------

- 도메인 등록

1. 후이즈검색.한국 -> 사용할 도메인 검색 quantforum.co.kr -> 가비아에서 구매
-> AWS 라이트세일 네트워킹 탭 -> DNS 영역 생성 클릭 -> 도메인 입력 -> DNS 영역 생성 확인.
-> DNS 레코드 추가 -> A 레코드 -> 하위도메인 @ -> 확인 staticlp-1 입력 -> 그린 체킹 클릭

AWS 라이트세일에 나온 이름 서버 4가지를 
가비아 네임서버 설정 (홈 > 도메인 정보 변경 > 네임서버 > 설정 ) 에 가서 기존 것을 지우고 다 추가한다.
(이게 2일 걸린 듯... 네임서버주소가 도메인에 적용되는 시간... 무튼 이후에 Nginx 에 도메인을 설정해야한다)

2. 서버환경에서 Nginx 설정에 도메인을 적용해야한다.
파일명: /etc/nginx/sites-available/mysite 의 server_name 을 해당 도메인으로 수정한다.
sudo nano mysite 입력 후 수정.

server {
        listen 80;
        server_name quantforum.kr;

        location = /favicon.ico { access_log off; log_not_found off; }

        location /static {
                alias /home/ubuntu/projects/mysite/static;
        }

        location / {
                include proxy_params;
                proxy_pass http://unix:/tmp/gunicorn.sock;
        }
}

이후 개발 환경 prod.py 의 ALLOWED_HOSTS 에 구입한 도메인 추가입력.

git으로 바뀐 파일 서버에 내려받고 이후 재시작 
(mysite) ubuntu@ip-172-26-14-116:/etc/nginx/sites-available$ sudo systemctl restart nginx 입력

3. quantforum.kr 로 접속해 확인

-------------------------------------------------------------------------------

- 데이터베이스 확장(SQLite -> PostgreSQL) 2가지 방법(후자 채택)
	- 서버에 PostgreSQL을 설치하여 사용하는 것
	- AWS 라이트세일 데이터베이스 인스턴스 사용하는 것★

AWS 리전 및 가용 영역 변경 -> 서울 -> PostgreSQL 최신버전 선택 -> 15달러 -> 리소스 이름에 'Database-1'
-> 데이터베이스 생성 클릭.

연결된 데이터베이스 세부정보들은 forum 에서 PostgreSQL에 접속할 때 필요

1. 서버에 PostgreSQL 클라이언트 설치
(mysite) ubuntu@ip-172-26-14-116:~/projects/mysite$ sudo apt install postgresql-client

2. 서버에 데이터베이스 생성 (-h 뒷 주소는 연결된 데이터베이스의 엔드포인트다.)
createdb forum --username=dbmasteruser -h ls-0f369f631f262ea24a2be84d4a0aca67d43ade26.czz5gkwznb9w.ap-northeast-2.rds.amazonaws.com
비밀번호는 연결세부정보에서 기본 제공되는 것을 바꿔야함

3. 장고로 개발되었으므로 장고에서 PostgreSQL에 접속하는 데 필요한 psycopg2-binary 모듈이 필요
pip install psycopg2-binary 입력.

4. settings/prod.py 파일에 DATABASE 항목 설정 (git push, pull 로 서버에 파일 적용)

5. 서버의 데이터베이스가 변경되었기 때문에 적용시켜줘야함.
	(mysite) ubuntu@ip-172-26-14-116:~/projects/mysite$ python manage.py migrate

6. 슈퍼유저 생성.
python manage.py createsuperuser 입력

이름 : admin
이메일 주소 :  admin@forum.kr
비밀번호: admin

7. 서버 재시작.
sudo systemctl restart nginx 입력.

-------------------------------------------------------------------------------

******* 서버에 올리기 전 개발시 주의사항.
- 모델이 변경되면 항상 아래 작업들을 해줘야 한다.
콜렉터 작업이 끝나면 cmd 에서
(mysite) c:\projects\mysite>python manage.py makemigrations 후
Select an option: 1 보고 >>> 1을 입력.
(mysite) c:\projects\mysite>python manage.py migrate 끝.

-------------------------------------------------------------------------------
