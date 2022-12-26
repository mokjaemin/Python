import pygame

pygame.init() #초기화(반드시필요)

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption("James game") #게임 이름

#배경이미지 불러오기
background = pygame.image.load("/Users/mokjaemin/Desktop/pythonfile/pygame1/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/mokjaemin/Desktop/pythonfile/pygame1/character.png")
character_size = character.get_rect().size #이미지 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) #캐릭터의 가로 위치(스크린의 절반)
character_y_pos = screen_height - character_height #캐릭터의 세로 위치(스크린의 절반)





#이벤트 루프
#게임이 진행중인가?
while True:
    for event in pygame.event.get(): #어떤이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            pygame.quit()
            exit() #닫아버림
    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭터 그리기


    pygame.display.update() #게임화면 다시 그리기
