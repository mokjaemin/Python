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

#공 만들기 (4개의 크기에 따라 따로 정리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "ballon1.png")),
    pygame.image.load(os.path.join(image_path, "ballon2.png")),
    pygame.image.load(os.path.join(image_path, "ballon3.png")),
    pygame.image.load(os.path.join(image_path, "ballon4.png"))
]

#공의 속도
ball_speed_y = [-18, -15, -12, -9]

#공들
balls = []

#최초 방생하는 큰공 추가
balls.append({
    "pos_x" : 50, #공의 x좌표
    "pos_y" : 50, #공의 y 좌표
    "img_idx" : 0, #공의 이미지 인덱스
    "to_x" : 3, #x축 이동방향 +3이면 오른쪽, -3이면 왼쪽으로 이동한다고 생각
    "to_y" : -6, # y축 이동방향 
    "init_spd_y" : ball_speed_y[0] #최초속도
})


#사라질 무기와 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

#시간 관련
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 40) 
total_time = 20
start_ticks = pygame.time.get_ticks() 




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

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls): #enumerate - 리스트의 인덱스값과 값을 반환
        ball_pos_x = ball_val["pos_x"] #값들중 pos_x에 해당하는 값을 반환
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #가로벽에 닿았을때 공의 방향 변경
        if ball_pos_x <0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"]*-1

        #세로위치
        #스테이지에 공이 튕겨서 올라갈 때
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5 #포물선 형태로 표현(속도를 줄여나감)

        ball_val["pos_x"] += ball_val["to_x"]    
        ball_val["pos_y"] += ball_val["to_y"]    




    #4. 충돌 처리
    
    #캐릭터 렉트 정보
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls): 
        ball_pos_x = ball_val["pos_x"] 
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        #공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y 
        
        #공과 캐릭터 충돌 체크
        if character_rect.colliderect(ball_rect):
            pygame.quit()
            break

        #공과 무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons): 
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            #무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            #충돌 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # 해당 무기 없애기
                ball_to_remove = ball_idx # 해당 볼 없애기
                
                #가장 작은 공이 아니라면 다음단계의 공으로 나눠주기
                if ball_img_idx < 3:

                    #현재 공의 위치 가져오기
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    #나눠진 공의 정보
                    small_ball_rect = ball_images[ball_img_idx].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]


                    #왼쪽으로 튕겨나가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width/2) - (small_ball_width/2), #공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height/2) - (small_ball_height/2), #공의 y 좌표
                        "img_idx" : ball_img_idx + 1, #공의 이미지 인덱스
                        "to_x" : -3, #x축 이동방향 +3이면 오른쪽, -3이면 왼쪽으로 이동한다고 생각
                        "to_y" : -6, # y축 이동방향 
                        "init_spd_y" : ball_speed_y[ball_img_idx +1] #최초속도
                    })
                    #오른쪽으로 튕겨 나가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width/2) - (small_ball_width/2), #공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height/2) - (small_ball_height/2), #공의 y 좌표
                        "img_idx" : ball_img_idx + 1, #공의 이미지 인덱스
                        "to_x" : 3, #x축 이동방향 +3이면 오른쪽, -3이면 왼쪽으로 이동한다고 생각
                        "to_y" : -6, # y축 이동방향 
                        "init_spd_y" : ball_speed_y[ball_img_idx +1] #최초속도
                    })                    



    #충돌된 공 or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    if len(balls) == 0:
        pygame.quit()






    #5. 화면에 그리기
    screen.blit(background, (0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
        

    screen.blit(stage, (0,screen_height - stage_height))

    screen.blit(character, (character_x_pos, character_y_pos))



    elasped_time = (pygame.time.get_ticks() - start_ticks)/1000

    timer = game_font.render(str(int(total_time - elasped_time)), True, (255,255,255))
    screen.blit(timer, (10,10))

    
    timer1 = game_font.render("survive", True, (255,255,255))
    screen.blit(timer1, (150,10))


    if (total_time - elasped_time) < 0:
        pygame.time.delay(2000)
        pygame.quit()
    
    pygame.display.update() #게임화면 다시 그리기 (필수로 업데이트)


#################################################################################################