import os


# 파일 기본
# print(os.getcwd()) # 현재 작업 공간
# os.chdir("rpa_basic_desktop")
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd())
# os.chdir("/Users") # 절대 경로로 이동
# print(os.getcwd())


# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
# print(os.path.join(os.getcwd(), "my_file.txt"))

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"/Users/mokjaemin/Desktop/pythonfile/my_file.txt"))

# 파일 정보 가져오기
# import time
# import datetime

# # 파일의 생성 날짜
# file_path = "pygame3/killboss.py"
# ctime = os.path.getctime(file_path)
# # 날짜정보를 strftime을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 크기
# print(os.path.getsize(file_path))



# 바로 아래 파일 목록만 가져오기
# print(os.listdir()) # 현재 작업공간 아래에 모든 파일 목록 가져옴
# print(os.listdir("rpa_basic_desktop")) # 해당 파일 아래에 모든 파일 목록 가져옴


# 모든 하위 파일까지 가져오기
# result = os.walk(".") # "." - 현재 폴더내에서 다 찾음
# print(result)
# for root, dirs, files in result:
#     print(root, dirs, files)

# 폴더 내에서 특정 파일 찾기
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk(os.getcwd()):
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)

# 폴더 내에서 특정 패턴을 가진 파일 찾기
# import fnmatch
# pattern = "8*.py" # 8로 시작 .py 로 끝나는 파일 
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))

# print(result)


# # 주어진 경로가 파일인지 폴던인지 확인
# print(os.path.isdir("rpa_basic_desktop"))
# print(os.path.isfile("rpa_basic_desktop"))


# # 해당 파일이 없다면 False 반환
# print(os.path.isfile("rpa_basiccccccc_desktop"))



# 주어진 경로가 존재하는지?
# if os.path.exists("rpa_basic_desktop"):
#     print("파일 존재 합니다")
# else:
#     print("파일이 존재하지 않습니다.")


# 파일 만들기
# open("new_file.txt", "a").close() # 빈파일 생성



# 파일명 변경
# os.rename("new_file.txt", "new_file_rename.txt") # 왼쪽에서 오른쪽으로 이름 변경


# 파일 삭제
# os.remove("new_file_rename.txt")



# 폴더 만들기
# os.mkdir("new_folder") # 현재 경로 기준으로 폴더 생성, 경로 작성시 해당 경로 밑에 생성
# # 이미 존재하는 폴더명은 사용 불가



# 여러 폴더 만들기
# os.makedirs("new_folders/a/b/c")


# 폴더명 변경
# os.rename("new_folder", "new_ff")



# 폴더 지우기
# os.rmdir("new_ff") # 폴더안이 비어있을때만 삭제
# import shutil
# shutil.rmtree("new_folders") # 폴더가 안비어있을때도 삭제



# 파일 복사하기
# 특정 파일을 폴더에 복사하기
import shutil
# shutil.copy("trash.png", "test_folder") # 원본 경로와 대상 경로로 복사
# shutil.copy("trash.png", "test_folder/copied_trash.png") # 이름까지 변경

# shutil.copyfile("trash.png", "test_folder/copied_trash.png") # 걍 별차이 없음


# 폴더 복사
# shutil.copytree("test_folder", "test_folder2") # 원본, 복사본

# 폴더 이동
# shutil.move("test_folder2", "test_folder") # 폴더2를 폴더 밑으로
