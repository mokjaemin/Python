
# 메일 불러오기

from imap_tools import MailBox
from account import *


with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    for msg in mailbox.fetch(limit=1, reverse=True): # 전체 메일을 불러움
            print("제목 : ", msg.subject)
            print("발신자 : ", msg.from_)
            print("수신자 ; ", msg.to)
            #print("참조자 : ", msg.cc) 
            #print("비밀참조자 : ", msg.bcc)
            print("날짜 : ", msg.date)
            print("본문 : ", msg.text) 
            print("html 메시지 : ", msg.html)
            print("="*100)

            # 첨부파일도 다운하기
            for att in msg.attachments:
                print("첨부파일은 이름", att.filename)
                print("타입", att.content_type)
                print("크기", att.size)

                # 파일 다운로드
                with open("download_" + att.filename, "wb") as f: # 다운로드시 파일이름 설정
                    f.write(att.payload)
                    print("첨부파일{} 다운완료".format(att.filename))
