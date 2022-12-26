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

#캐릭터의 움직인 양
to_x = 0
to_y = 0

#이벤트 루프
#게임이 진행중인가?
while True:
    for event in pygame.event.get(): #어떤이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            pygame.quit()
            exit() #닫아버림

        if event.type == pygame.KEYDOWN: #키가 눌렀을 떄
            if event.key == pygame.K_LEFT: #캐릭터가 왼쪽으로
                to_x -= 5
            elif event.key == pygame.K_RIGHT: #캐릭터가 오른쪽으로 
                to_x += 5 
            elif event.key == pygame.K_UP: #캐릭터가 위로
                to_y -= 5
            elif event.key == pygame.K_DOWN: #캐릭터가 아래로
                to_y += 5
        if event.type == pygame.KEYUP: #방향키를 땠을 때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    #움직인 만큼 더해 주기
    character_x_pos += to_x
    character_y_pos += to_y

    #화면 벗어나지 않게 조정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > 410:
        character_x_pos = 410
    elif character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos >570:
        character_y_pos = 570


    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭터 그리기
    
    pygame.display.update() #게임화면 다시 그리기
