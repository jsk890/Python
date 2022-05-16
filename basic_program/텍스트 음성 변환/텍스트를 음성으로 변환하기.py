# gtts 라이브러리로 부터 gTTS 불러오기
from gtts import gTTS
# playsound 모듈로부터 playsound를 불러와 사용\microsoft\pylance-release\blob\main\DIAGNOSTIC_SEVERITY_RULES.md
from playsound import playsound
text = "안녕하세요. 파이썬 입니다."
text2 = "텍스트를 음성으로 변환한 파일 입니다."

# text 변수의 문자열을 한글로 변환
tts = gTTS(text=text, lang='ko')
tts2 = gTTS(text=text2, lang='ko')
# 현재 경로의 폴더에 저장하기
# 문자열 앞에 r을 붙여 역슬래시가 다른 특별한 기능을 하지 않도록 하며, 역슬래시 자체로 해석하도록 함
tts.save(r"basic_program\hi.mp3")
tts2.save(r"basic_program\hi2.mp3")
# basic_program 폴더에 hi.mp3 파일을 재생

# playsound(r"basic_program\hi.mp3") #오류 발생

# 읽어올 파일의 경로
file_path = r'basic_program\나의텍스트.txt'
# 파일을 열고 종료되면 자동으로 파일을 닫음
# 파일을 f의 이름으로 오픈, 한글로 된 파일을 열기 때문에 인코딩하여 글자가 깨지지 않도록 함
with open(file_path, 'rt', encoding='utf-8') as f:
    read_file = f.read()
    
tts = gTTS(text = read_file, lang='ko')
tts.save(r"basic_program\나의텍스트.mp4")