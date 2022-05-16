#QR 라이브러리, QR코드 하나 생성
import qrcode

qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

save_path = 'basic_program\\' + qr_data + '.png'
qr_img.save(save_path)

# 텍스트 파일을 만들어 QR이미지로 만들고 싶은 URL의 경로를 저장해 놓는다
file_path=r"basic_program\qr코드모음.txt"
with open(file_path, 'rt', encoding='utf-8') as f:
    # 텍스트 파일에 있는 글들을 줄 단위로 읽어 저장
    read_lines = f.readlines()
    
    for line in read_lines:
        line = line.strip()
        print(line)
        # 한 줄씩 읽어 QR이미지로 만든다
        qr_data = line
        qr_img = qrcode.make(qr_data)
        
        save_path='basic_program\\' + qr_data + '.png'
        qr_img.save(save_path)
