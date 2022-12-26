import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "ahrwoals11@gamil.com"

# 여러명 보낼때
# msg["To"] = "a.naver.com, b.naver.com"
# or
# to_list = ["a.naver.com", "b.naver.com"]
# msg["To"] = ", ".join(to_list) # , + space 를 통해 구별

# 참조
# msg["Cc"] = "a.naver.com"

# 비밀 참조
# msg["Bcc"] = "a.naver.com"


msg.set_content("테스트 본문입니다.")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

