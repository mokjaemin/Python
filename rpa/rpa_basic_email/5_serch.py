from imap_tools import MailBox
from account import *

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:

    # 전체 메일을 불러움
    for msg in mailbox.fetch(limit=5, reverse=True): # 전체 메일을 불러움
        print("[{}] {}".format(msg.from_, msg.subject))


    # 읽지 않은 메일 3개를 불러움
    # for msg in mailbox.fetch('(UNSEEN)', limit=3, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))


    # 특정인이 보낸 메일
    # for msg in mailbox.fetch('(FROM ahrwoals11@pusan.ac.kr)', limit=3, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    
    # 제목, 본문내 특정 글자를 포함하는 메일
    # 항상 '' 먼저쓰고 "" 쓰자
    # for msg in mailbox.fetch('(TEXT "test mail")', limit=3, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))



    # 어떤 글자를 포함하는 제목
    # for msg in mailbox.fetch('(SUBJECT "test mail")', limit=3, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))



    # 한글 지원이 안되기에 우회하여 검색
    # for msg in mailbox.fetch(limit=3, reverse=True): # 어떤 글자를 포함하는 제목
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))



    # 특정 날짜 이후의 메일
    # for msg in mailbox.fetch('(SENTSINCE 01-Aug-2021)',limit=3, reverse=True):
    #         print("[{}] {}".format(msg.from_, msg.subject))


    # 특정 날짜에 온 메일
    # for msg in mailbox.fetch('(ON 01-Aug-2021)',limit=3, reverse=True):
    #         print("[{}] {}".format(msg.from_, msg.subject))


    # 두가지 이상의 조건을 모두 만족하는 메일
#     for msg in mailbox.fetch('(SENTSINCE 01-Aug-2021 SUBJECT "test mail")',limit=3, reverse=True):
#             print("[{}] {}".format(msg.from_, msg.subject))    

    # 두가지 중 하나의 조건이라도 만족하는 메일
#     for msg in mailbox.fetch('(OR SENTSINCE 01-Aug-2021 SUBJECT "test mail")',limit=3, reverse=True):
#             print("[{}] {}".format(msg.from_, msg.subject))  