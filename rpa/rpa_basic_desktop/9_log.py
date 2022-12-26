# import logging

# logging.basicConfig(level=logging.ERROR, format= "%(asctime)s [%(levelname)s] %(message)s")
# # logging.ERROR = 에러보다 높은 레벨만 출력
# logging.debug("아 이거 누가 짠거야??")
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 오래되었습니다. 보안이 필요할듯해용")
# logging.error("에러가 발생하였습니다.")
# logging.critical("복구가 불가능한 심각한 문제가 발생하였습니다.")
# 밑으로 갈 수록 심각한 수준

# result
# 2021-08-06 15:58:55,497 [DEBUG] 아 이거 누가 짠거야??
# 2021-08-06 15:58:55,497 [INFO] 자동화 수행 준비
# 2021-08-06 15:58:55,497 [WARNING] 이 스크립트는 오래되었습니다. 보안이 필요할듯해용
# 2021-08-06 15:58:55,497 [ERROR] 에러가 발생하였습니다.
# 2021-08-06 15:58:55,497 [CRITICAL] 복구가 불가능한 심각한 문제가 발생하였습니다.




# 터미널과 파일에 함께 로그 남기기
import logging
from datetime import datetime
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") 
# 시간, 로그레벨, 메시지 형태로 로그를 작성
logger = logging.getLogger()

# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림 (터미널)
streamhandler = logging.StreamHandler()
streamhandler.setFormatter(logFormatter)
logger.addHandler(streamhandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
# 시간정보가 담긴 파일 생성 하는 변수
filehandler = logging.FileHandler(filename, encoding="utf-8")
filehandler.setFormatter(logFormatter)
logger.addHandler(filehandler)

logger.debug("로그를 남겨보는 테스트를 진행합니다.")