# 연결된 접속정보를 받아올 때 사용하는 모듈
import socket
# 사이트에 접속하기 위한 모듈
import requests
# IP주소를 찾기 위한 정규식을 사용하기 위해 re모듈 사용
import re

# 연결된 소켓의 이름을 가져옴
# 가상 환경등을 사용하여 여러개의 환경이 있을 경우 다른 환경의 IP가 출력 될 수 있음
in_addr = socket.gethostbyname(socket.gethostname())
# 외부 사이트에 접속하여 접속된 정보를 바탕으로 IP확인
# 조금 더 정확하게 확인 하는 방법
in_addr2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr2.connect(("www.google.co.kr",443))
# 내부 IP확인
print(in_addr)
print(in_addr2.getsockname()[0])

# IPconfig 사이트에 접속
req = requests.get("http://ipconfig.kr")
# 정규식 표현을 사용하여 IP주소를 가져옴
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})', req.text)[1]
# 외부 IP확인
print(out_addr)