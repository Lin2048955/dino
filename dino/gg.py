import pygame
import random
# pygame setup
pygame.init()

# 畫布大小
screen = pygame.display.set_mode((1280, 400))

BLACK = (0,0,0)

# 載入圖片
img_dino = pygame.image.load("dino.png")
img_dinorun = [pygame.image.load("DinoRun1.png"),pygame.image.load("DinoRun2.png")]
img_dinoduck = [pygame.image.load("DinoDuck1.png"),pygame.image.load("DinoDuck2.png")]
img_bird = pygame.image.load("Bird1.png")
img_birdrun = [pygame.image.load("Bird1.png"),pygame.image.load("Bird2.png")]
img_track = pygame.image.load("track.png")
img_missile = pygame.image.load("missile.png")


img_cactus = pygame.image.load("cactus.png")
img_dino = pygame.transform.scale(img_dino,(100,100))
img_missile = pygame.transform.scale(img_missile,(100,50))

# 設定角色
dino_rect = img_dino.get_rect()
dino_rect.x = 50
dino_rect.y = 300
is_jumping = False
is_ducking = False
attack = False
jump = 15
nowjump =jump
g = 0.7

cactus_rect = img_cactus.get_rect()
cactus_rect.x = 3000
cactus_rect.y = 330
initspeed = 5

bird_rect = img_bird.get_rect()
bird_rect.x = 2000
bird_rect.y = 250
initspeed = 5
speed = initspeed

missile_rect = img_missile.get_rect()
missile_rect.x = dino_rect.x+50
missile_rect.y = dino_rect.y+20

# 設定分數
score = 0
highscore =0 # 最高紀錄
font = pygame.font.Font(None,36)

# 設定等級
level =0
speedlist = [5,6,7,8,9]

clock = pygame.time.Clock()
running = True
gameover = False

lastime = 0
frame = 0



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    score += 1 


    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_jumping = True
                if event.key == pygame.K_r:
                    score = 0
                    cactus_rect.x = 3000
                    bird_rect.x = 2000
                    gameover = False
                if event.key == pygame.K_v:
                    attack=True
                    missile_rect.y=dino_rect.y+20
                    missile_rect.x=dino_rect.x+50

                if event.key == pygame.K_c:
                    dino_rect.y = 330
                    is_ducking = True
                    
            if event.type == pygame.KEYUP:
                if is_ducking:
                    dino_rect.y = 300
                    is_ducking = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                is_jumping = True
                if gameover:
                    score = 0
                    cactus_rect.x = 3000
                    bird_rect.x = 2000
                    gameover = False


                    

    if not gameover:
        if is_jumping:
            dino_rect.y -= nowjump
            
            nowjump -= g
            if dino_rect.y>300:
                dino_rect.y=300
                missile_rect.y=dino_rect.y+20
                nowjump = jump
                is_jumping = False

        cactus_rect.x -= speed
        bird_rect.x -= speed
        
        if cactus_rect.x < 0:
            cactus_rect.x = random.randint(1280, 3000)
        if bird_rect.x < 0:
            bird_rect.x = random.randint(1280, 2000)
        

        if dino_rect.colliderect(cactus_rect) or dino_rect.colliderect(bird_rect):
            if score > highscore:
                highscore = score
            gameover = True
            speed = initspeed



        
        if score>1000:
            speed = speedlist[1]
            level = 1
        elif score >2000:
            speed = speedlist[2]
            level =2
        elif score >3000:
            speed = speedlist[3]
            level = 3

        

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((255,255,255))
        screen.blit(img_track,(0,370))

        score_show = font.render(f"Score: {score}",True, BLACK)
        screen.blit(score_show,(10,10))

        highscore_show = font.render(f"Hi Score: {highscore}",True, BLACK)
        screen.blit(highscore_show,(10,30))
        
        level_show = font.render(f"Level: {level} Speed: {speedlist[1]}",True, BLACK)
        screen.blit(level_show,(10,50))
        
        if attack:
            screen.blit(img_missile,(missile_rect.x,missile_rect.y))
            missile_rect.x+=5
            if missile_rect.colliderect(cactus_rect):
                missile_rect.x=1280
                cactus_rect.x = random.randint(1280, 3000)
            if missile_rect.colliderect(bird_rect):
                missile_rect.x=1280
                bird_rect.x = random.randint(1280, 3000)



        if gameover:
            gameover_show = font.render(f"Game Over",True, BLACK)
            screen.blit(gameover_show,(550,150))
        

        # 更新跑步動畫
        nowtime = pygame.time.get_ticks()
        if nowtime - lastime > 300:
            frame = (frame+1) % 2
            lastime  = nowtime

        
        
        if is_ducking:
            screen.blit(img_dinoduck[frame],dino_rect)
        else:
            screen.blit(img_dinorun[frame],dino_rect)
        # RENDER YOUR GAME HERE
        # screen.blit(img_dino,dino_rect)
        screen.blit(img_cactus,cactus_rect)
        screen.blit(img_birdrun[frame],bird_rect)


        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

pygame.quit()