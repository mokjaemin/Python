import pygame

pygame.init() #초기화(반드시필요)

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption("James game") #게임 이름

#배경이미지 불러오기
background = pygame.image.load("/Users/mokjaemin/Desktop/pythonfile/background.png")

#이벤트 루프
#게임이 진행중인가?
while True:
    for event in pygame.event.get(): #어떤이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            pygame.quit()
            exit() #닫아버림
    screen.blit(background, (0,0)) #배경 그리기
    #screen.fill((0,0,255)) #색깔을 직접 채우기

    pygame.display.update() #게임화면 다시 그리기
