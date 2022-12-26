import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "ahrwoals11@pusan.ac.kr"
msg.set_content("다운로드 하세요.")

# mime타입을 통해 타입 확인
# main = application sub = octet-stream 하면 거의 다 됨
# 이미지
# with open("./pngfile/id.png", "rb") as f:
#     msg.add_attachment(f.read(), maintype = "image", subtype = "png", filename = f.name)

#pdf
with open("test.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype = "application", subtype = "pdf", filename = f.name)

#xlsx
with open("example.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype = "application", subtype = "octet-stream", filename = f.name)



with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)