import pygame

pygame.init() #초기화(반드시필요)

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption("James game") #게임 이름

#FPS
clock = pygame.time.Clock()

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

#캐릭터의 속도
character_speed = 0.6

#적 캐릭터
enemy = pygame.image.load("/Users/mokjaemin/Desktop/pythonfile/pygame1/enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기를 구해옴
enemy_width = enemy_size[0] #적의 가로크기
enemy_height = enemy_size[1] #적의 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #적의 가로 위치(스크린의 절반)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) #적의 세로 위치(스크린의 절반)

#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트객체 생성(폰트 종류, 크기)

#총시간
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks() #현재 틱을 받아옴


#이벤트 루프
#게임이 진행중인가?
while True:

    dt = clock.tick(60) #r게임 회면의 초당 프렘수 설정(움직임의 부드러움 조정)

    for event in pygame.event.get(): #어떤이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            pygame.quit()

        if event.type == pygame.KEYDOWN: #키가 눌렀을 떄
            if event.key == pygame.K_LEFT: #캐릭터가 왼쪽으로
                to_x -= character_speed

            elif event.key == pygame.K_RIGHT: #캐릭터가 오른쪽으로 
                to_x += character_speed

            elif event.key == pygame.K_UP: #캐릭터가 위로
                to_y -= character_speed

            elif event.key == pygame.K_DOWN: #캐릭터가 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 땠을 때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    #움직인 만큼 더해 주기 + FPS값에 따른 움직임 감도 조정
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #화면 벗어나지 않게 조정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > 410:
        character_x_pos = 410
    elif character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos >570:
        character_y_pos = 570


    #충돌처리를 위한 캐릭터와 적의 rectangle 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        pygame.quit()
    

    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) #적 그리기


    #타이머 집어 넣기
    #경과 시간 계산
    elasped_time = (pygame.time.get_ticks() - start_ticks)/1000
    #경과시간을 1000으로 나누어서 초단위로 표시 원래단위는 밀리세크

    timer = game_font.render(str(int(total_time - elasped_time)), True, (255,255,255))
    #타이머 그리기, 순서대로 출력한 글자, 트루, 색상
    screen.blit(timer, (10,10))

    #시간이 0 이하이면 게임 종료
    if (total_time - elasped_time) < 0:
        pygame.time.delay(2000)
        pygame.quit()


    

    
    pygame.display.update() #게임화면 다시 그리기 (필수로 업데이트)


