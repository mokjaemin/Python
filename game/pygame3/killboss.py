### import
import pygame
import os
import random

### 초기화
pygame.init()

### 스크린 설정
screen_width = 1200 
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Kill the boss")

### 민감도 설정(FPS)
clock = pygame.time.Clock()

### 파일 설정
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images") # images폴더 위치 반환

### 배경만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

### 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height
character_speed = 0.6
to_x = 0
c_blood = 5000

### 무기 만들기1
weapon1 = pygame.image.load(os.path.join(image_path, "ballon2.png"))
weapon1_size = weapon1.get_rect().size
weapon1_width = weapon1_size[0]
weapon1_speed = 10
weapon1_x_pos = character_x_pos
weapon1_y_pos = character_y_pos
weapons1 = [] # 여러개의 무기를 위한 리스트 생성


### 무기 만들기2
weapon2 = pygame.image.load(os.path.join(image_path, "ballon3.png"))
weapon2_size = weapon2.get_rect().size
weapon2_width = weapon2_size[0]
weapon2_speed = 10
weapon2_x_pos = character_x_pos
weapon2_y_pos = character_y_pos
weapons2 = [] # 여러개의 무기를 위한 리스트 생성


### 무기 만들기3
weapon3 = pygame.image.load(os.path.join(image_path, "ballon4.png"))
weapon3_size = weapon3.get_rect().size
weapon3_width = weapon3_size[0]
weapon3_speed = 10
weapon3_x_pos = character_x_pos
weapon3_y_pos = character_y_pos
weapons3 = [] # 여러개의 무기를 위한 리스트 생성




### 적 만들기
enemy = pygame.image.load(os.path.join(image_path, "enemy.png"))
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width/2 - enemy_width/2
enemy_y_pos = 0
enemy_speed = 0
to_x = 0
blood = 10000

### 적 무기 만들기
weapon4 = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon4_size = weapon4.get_rect().size
weapon4_width = weapon4_size[0]
weapon4_speed = 9
weapon4_x_pos = random.uniform(0, 1000)
weapon4_y_pos = 0


weapon5 = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon5_size = weapon5.get_rect().size
weapon5_width = weapon4_size[0]
weapon5_speed = 11
weapon5_x_pos = random.uniform(0, 1000)
weapon5_y_pos = 0




### 사라질 무기 변수
weapon1_to_remove = -1
weapon2_to_remove = -1
weapon3_to_remove = -1


### 타이머 관련 설정
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 40) 
total_time = 100
start_ticks = pygame.time.get_ticks() 


### 메인
while True:

    dt = clock.tick(60) #r게임 회면의 초당 프렘수 설정(움직임의 부드러움 조정)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                to_x -= character_speed

            elif event.key == pygame.K_RIGHT: 
                to_x += character_speed

            elif event.key == pygame.K_a:
                weapon1_x_pos = character_x_pos + (character_width/2) - (weapon1_width/2)
                weapon1_y_pos = character_y_pos
                weapons1.append([weapon1_x_pos, weapon1_y_pos])

            elif event.key == pygame.K_s:
                weapon2_x_pos = character_x_pos + (character_width/2) - (weapon2_width/2)
                weapon2_y_pos = character_y_pos
                weapons2.append([weapon2_x_pos, weapon2_y_pos])

            elif event.key == pygame.K_d:
                weapon3_x_pos = character_x_pos + (character_width/2) - (weapon3_width/2)
                weapon3_y_pos = character_y_pos
                weapons3.append([weapon3_x_pos, weapon3_y_pos])


        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    ### 캐릭터가 화면에서 벗어나지 못하게 설정
    character_x_pos += to_x * dt
    if character_x_pos < 0:
        character_x_pos = 0

    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width


    if enemy_x_pos > screen_width-enemy_width:
        enemy_x_pos = screen_width-enemy_width
        enemy_speed = enemy_speed*-1

    elif enemy_x_pos < 0:
        enemy_speed = enemy_speed*-1
    

    ### 무기 속도 설정
    weapon1_y_pos += 7
    weapon2_y_pos += 8
    weapon3_y_pos += 9

    weapon4_y_pos += weapon4_speed
    weapon5_y_pos += weapon5_speed

    if weapon4_y_pos > 700:
        weapon4_y_pos = 0
        weapon4_x_pos = random.uniform(0, 1000)

    if weapon5_y_pos > 700:
        weapon5_y_pos = 0
        weapon5_x_pos = random.uniform(0, 1000)
  

    ### 적 움직임
    enemy_x_pos += enemy_speed


    ### 무기 위치 설정 및 천장에 닿으면 무기 없어짐
    weapons1 = [[w1[0], w1[1]-weapon1_speed] for w1 in weapons1 if w1[1] > 0]
    weapons2 = [[w2[0], w2[1]-weapon2_speed] for w2 in weapons2 if w2[1] > 0]
    weapons3 = [[w3[0], w3[1]-weapon3_speed] for w3 in weapons3 if w3[1] > 0]
    
    
    
    ### 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    weapon4_rect = weapon4.get_rect()
    weapon4_rect.left = weapon4_x_pos
    weapon4_rect.top = weapon4_y_pos


    weapon5_rect = weapon5.get_rect()
    weapon5_rect.left = weapon5_x_pos
    weapon5_rect.top = weapon5_y_pos


    weapon1_rect = weapon1.get_rect()
    weapon1_rect.left = weapon1_x_pos
    weapon1_rect.top = weapon1_y_pos

    weapon2_rect = weapon2.get_rect()
    weapon2_rect.left = weapon2_x_pos
    weapon2_rect.top = weapon2_y_pos

    weapon3_rect = weapon3.get_rect()
    weapon3_rect.left = weapon3_x_pos
    weapon3_rect.top = weapon3_y_pos


    if character_rect.colliderect(weapon4_rect):
        c_blood -= 80


    if character_rect.colliderect(weapon5_rect):
        c_blood -= 80


    if  enemy_rect.colliderect(weapon1_rect):
        blood -= 30


    if  enemy_rect.colliderect(weapon2_rect):
        blood -= 20


    if  enemy_rect.colliderect(weapon3_rect):
        blood -= 10

    if blood < 0:
        pygame.quit()
    
    if c_blood < 0:
        pygame.quit()
    



    ### 충돌된 피 or 무기 없애기

    if weapon1_to_remove > -1:
        del weapons1[weapon1_to_remove]
        weapon1_to_remove = -1
    
    if weapon2_to_remove > -1:
        del weapons2[weapon2_to_remove]
        weapon2_to_remove = -1
    
    if weapon3_to_remove > -1:
        del weapons3[weapon3_to_remove]
        weapon3_to_remove = -1







    ### 화면에 그리기
    screen.blit(background, (0,0))

    
    for weapon1_x_pos, weapon1_y_pos in weapons1:
        screen.blit(weapon1, (weapon1_x_pos, weapon1_y_pos))

    
    for weapon2_x_pos, weapon2_y_pos in weapons2:
        screen.blit(weapon2, (weapon2_x_pos, weapon2_y_pos))

    
    for weapon3_x_pos, weapon3_y_pos in weapons3:
        screen.blit(weapon3, (weapon3_x_pos, weapon3_y_pos))

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(weapon4, (weapon4_x_pos, weapon4_y_pos))
    screen.blit(weapon5, (weapon5_x_pos, weapon5_y_pos))




    ### 타이머 및 타이틀 설정
    elasped_time = (pygame.time.get_ticks() - start_ticks)/1000
    timer = game_font.render(str(int(total_time - elasped_time)), True, (0,0,0))
    screen.blit(timer, (10,10))
    title = game_font.render("kill the monster", True, (0,0,0))
    screen.blit(title, (120,10))
    blood_amount = game_font.render("blood:"+str(blood), True, (0,0,0))
    screen.blit(blood_amount, (10,50))
    c_blood_amount = game_font.render("character blood:"+str(c_blood), True, (0,0,0))
    screen.blit(c_blood_amount, (10,80))


    if (total_time - elasped_time) < 0:
        pygame.time.delay(2000)
        pygame.quit()
    
    pygame.display.update() #게임화면 다시 그리기 (필수로 업데이트)


