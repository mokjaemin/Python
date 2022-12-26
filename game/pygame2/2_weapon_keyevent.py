import pygame
import os


#################################################################################################

#기본초기화 부분(반드시 해야하는 부분)
pygame.init()

#화면 크기 설정
screen_width = 640 #가로크기
screen_height = 480 #세로크기
screen = pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption("James pang game") #게임 이름

#FPS
clock = pygame.time.Clock()

#################################################################################################



#################################################################################################

#1.사용자 정의(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images폴더 위치 반환

#배경만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지 높이 위에 캐릭터를 그리기 위해

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height - stage_height
character_speed = 0.6
to_x = 0

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 여러발 발사 가능
weapons = []

#무기 이동속도
weapon_speed = 10

while True:

    dt = clock.tick(60) #r게임 회면의 초당 프렘수 설정(움직임의 부드러움 조정)

    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): #어떤이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            pygame.quit()

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                to_x -= character_speed

            elif event.key == pygame.K_RIGHT: 
                to_x += character_speed
            
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    #3. 게임캐릭터 위치 정의
    character_x_pos += to_x * dt
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    #무기 위치 정의
    weapons = [[w[0], w[1]-weapon_speed] for w in weapons]

    #천장에 닿으면 무기 없어짐
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]



    #4. 충돌 처리
    
    #5. 화면에 그리기
    screen.blit(background, (0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(stage, (0,screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    
    pygame.display.update() #게임화면 다시 그리기 (필수로 업데이트)


#################################################################################################