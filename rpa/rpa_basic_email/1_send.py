import smtplib
from account import * # account.py 에서 정보를 가져옴



with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    
    smtp.ehlo() # 연결이 잘 수립되었는 지 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인

    subject = "test mail" # 메일 제목
    body = "mail body" # 메일 본문

    msg = f"subject: {subject}\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, "bamer@naver.com", msg) # 발신자, 수신자, 정해진 형태의 메시지
