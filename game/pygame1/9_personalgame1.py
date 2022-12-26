
### import
import pygame
import random

### 초기화
pygame.init() 

### 스크리 설정
screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("avoid ball game") 

### 타이머 관련 설정
game_font = pygame.font.Font(None, 40)
total_time = 30
start_ticks = pygame.time.get_ticks() 

### 민감도 설정(FPS)
clock = pygame.time.Clock()

### 배경 설정
background = pygame.image.load("/Users/mokjaemin/Desktop/pythonfile/pic/c.png")

### 캐릭터 설정
character = pygame.image.load("/Users/mokjaemin/Desktop/pythonfile/pic/kim.png")
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height 
to_x = 0 # 좌우 이동량 변수
to_y = 0 # 상하 이동량 변수
character_speed = 0.6

### 적1 설정
enemy = pygame.image.load("/Users/mokjaemin/Desktop/pythonfile/pic/m.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1] 
enemy_x_pos = random.uniform(0,410)
enemy_y_pos = 0

### 적2 설정
enemy1 = pygame.image.load("/Users/mokjaemin/Desktop/pythonfile/pic/m.png")
enemy1_size = enemy1.get_rect().size 
enemy1_width = enemy1_size[0] 
enemy1_height = enemy1_size[1] 
enemy1_x_pos = random.uniform(0,410)
enemy1_y_pos = 0

### 적3 설정
enemy2 = pygame.image.load("/Users/mokjaemin/Desktop/pythonfile/pic/m.png")
enemy2_size = enemy2.get_rect().size 
enemy2_width = enemy2_size[0] 
enemy2_height = enemy2_size[1] 
enemy2_x_pos = random.uniform(0,410)
enemy2_y_pos = 0


### 메인
while True:

    dt = clock.tick(60) #클수록 빨라짐(민감해짐) 
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()

        if event.type == pygame.KEYDOWN: # 키가 눌렸을 때
            if event.key == pygame.K_LEFT: 
                to_x -= character_speed

            elif event.key == pygame.K_RIGHT: 
                to_x += character_speed

        if event.type == pygame.KEYUP: # 키가 떼어졌을 때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    ### 민감도 설정
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    ### 화면 벗어나지 못하게 조정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > 410:
        character_x_pos = 410
    elif character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos >570:
        character_y_pos = 570

    ### 적들의 속도 설정
    enemy_y_pos += 8
    enemy1_y_pos += 7
    enemy2_y_pos += 9

    ### 적들이 화면 벗어났을때 화면 재조정
    if enemy_y_pos > 620:
        enemy_y_pos = 50
        enemy_x_pos = random.uniform(0, 410)    

    if enemy1_y_pos > 620:
        enemy1_y_pos = 50
        enemy1_x_pos = random.uniform(0, 410)
  
    if enemy2_y_pos > 620:
        enemy2_y_pos = 50
        enemy2_x_pos = random.uniform(0, 410)


    ### 캐릭터 및 적들의 rect정보를 가져옴
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy1_rect = enemy1.get_rect()
    enemy1_rect.left = enemy1_x_pos
    enemy1_rect.top = enemy1_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos


    ### 위에서 가져온 rect 정보를 통해 충돌 감지
    if character_rect.colliderect(enemy_rect):
        pygame.time.delay(2000)
        pygame.quit()
    
    if character_rect.colliderect(enemy1_rect):
        pygame.time.delay(2000)
        pygame.quit()
    
    if character_rect.colliderect(enemy2_rect):
        pygame.time.delay(2000)
        pygame.quit()

    
    ### 화면에 그리기
    screen.blit(background, (0,0)) 
    screen.blit(character, (character_x_pos,character_y_pos)) 
    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))
    screen.blit(enemy1, (enemy1_x_pos,enemy1_y_pos))
    screen.blit(enemy2, (enemy2_x_pos,enemy2_y_pos))


    ### 타이머 설정
    elasped_time = (pygame.time.get_ticks() - start_ticks)/1000 
    timer = game_font.render(str(int(total_time - elasped_time)), True, (255,255,255))
    screen.blit(timer, (10,10))
    timer1 = game_font.render("avoid ball", True, (255,255,255))
    screen.blit(timer1, (100,10))
    if (total_time - elasped_time) < 0:
        pygame.time.delay(2000)
        pygame.quit()


    ### 계속된 업데이트
    pygame.display.update() 


