# 폴더 파일 관리 및 사진관리입니다.
# 우선 폴더 파일 관리를 해볼게요!!

# 수업에서 다뤘던 내용을 기준으로 설명드릴게요
# 추가적인 학습은 각자 !! 구글링을 통해서 하시면 됩니다~~
# 궁금한게 있으시면 개인적으로 연락해주세요.


import os


os.getcwd()  # 현재경로를 반환
os.listdir()  # listdir 의 default 값은 현재경로이고
                  # os.listdir ( 특정 폴더 ) 로 설정할 경우 해당 폴더 하위의 모든 폴더 파일이 리스트로 저장되요
                  # 리스트로 반환되는 사실을 잊지 맙시다!!!

os.mkdir("test") # 해당 구문은 Directory(폴더)를 만드는 명령어에요!
                           # 하지만, mkdir 로 만드려는 폴더가 존재하는 폴더일 경우 에러가 발생합니다.
os.path.isdir("test") # 해당 폴더가 존재하는지 알아보고 싶을 때 사용하고, Bool 값을 반환합니다.
os.path.isfile() # 해당 파일이 존재하는지 알아보고 싶을 때 사용하고, Bool 값을 반환합니다. 

# 이것들만 알고있어도 무엇을 할 수 있느냐??
# 우선 폴더생성시 해당 폴더가 있으면, "폴더가 존재합니다", 존재하지 않을 경우에는
# 폴더를 생성하는 프로그램을 짤 수 있습니다.

