# 기초 프로그램 만들기

### [숫자 맞추기 게임](https://github.com/jsk890/Python/blob/main/basic_program/%EC%88%AB%EC%9E%90%20%EB%A7%9E%EC%B6%94%EA%B8%B0%20%EA%B2%8C%EC%9E%84.py)
- 랜덤 라이브러리를 import
- 시도 횟수 카운팅
- 숫자이외 입력시 예외처리

![image](https://user-images.githubusercontent.com/55019081/168511051-86594a51-a941-4f58-93ce-40a7f9fd50ae.png)

### [내외부 IP 확인하기](https://github.com/jsk890/Python/blob/main/basic_program/%EB%82%B4%EC%99%B8%EB%B6%80%20IP%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0.py)
- socket, requests, re 모듈 사용
- 연결된 소켓 정보 확인
- 외부 사이트를 통해 정보 확인
- 정규식 표현

![image](https://user-images.githubusercontent.com/55019081/168529171-c8f97cec-b198-412c-87a9-4c6382211d4f.png)

### [텍스트를 음성으로 변환하여 저장하기](https://github.com/jsk890/Python/blob/main/basic_program/%ED%85%8D%EC%8A%A4%ED%8A%B8%20%EC%9D%8C%EC%84%B1%20%EB%B3%80%ED%99%98/%ED%85%8D%EC%8A%A4%ED%8A%B8%EB%A5%BC%20%EC%9D%8C%EC%84%B1%EC%9C%BC%EB%A1%9C%20%EB%B3%80%ED%99%98%ED%95%98%EA%B8%B0.py)
- gtts, playsound 모듈 설치
- pip install gtts
- pip install playsound
- pip 명령어가 작동되지 않는다면 파이썬 설치 단계에서 PATH경로 지정을 해주지 않았으므로 재설치 필요
- with로 파일 경로 읽고 오픈 및 클로즈
- 파일 저장

![image](https://user-images.githubusercontent.com/55019081/168547087-5f9d4993-ed02-4653-8167-956b1918e1d0.png)

https://user-images.githubusercontent.com/55019081/168547104-79695e90-45bc-4dca-b104-53319c0b20f9.mp4

### [QR코드 생성하기](https://github.com/jsk890/Python/blob/main/basic_program/QR%EC%BD%94%EB%93%9C%20%EC%83%9D%EC%84%B1%EA%B8%B0/QR%EC%BD%94%EB%93%9C%EC%83%9D%EC%84%B1%EA%B8%B0.py)
- No module named 'PIL' 오류시 pip install pillow 설치
- 텍스트 파일에 있는 URL의 주소를 한줄 씩 읽어 QR이미지로 생성

![image](https://user-images.githubusercontent.com/55019081/168557762-308a1854-8992-4613-8c46-8ebc57874aab.png)
