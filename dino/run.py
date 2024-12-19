# Example file showing a basic pygame "game loop"
import pygame

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



img_cactus = pygame.image.load("cactus.png")
img_dino = pygame.transform.scale(img_dino,(100,100))

# 設定角色
dino_rect = img_dino.get_rect()
dino_rect.x = 50
dino_rect.y = 300
is_jumping = False
is_ducking = False
jump = 20
nowjump =jump
g = 1

cactus_rect = img_cactus.get_rect()
cactus_rect.x = 3000
cactus_rect.y = 330
speed = 5

bird_rect = img_bird.get_rect()
bird_rect.x = 2000
bird_rect.y = 250
speed = 5

# 設定分數
score = 0
highscore =0 # 最高紀錄
font = pygame.font.Font(None,36)

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
                    cactus_rect.x = 2000
                    gameover = False
                if event.key == pygame.K_DOWN:
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
                nowjump = jump
                is_jumping = False

        cactus_rect.x -= speed
        bird_rect.x -= speed
        if cactus_rect.x < 0:
            cactus_rect.x = 3000
        if bird_rect.x < 0:
            bird_rect.x = 2000
        

        if dino_rect.colliderect(cactus_rect):
            if score > highscore:
                highscore = score
            gameover = True
        
        if dino_rect.colliderect(bird_rect):
            if score > highscore:
                highscore = score
            gameover = True

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((255,255,255))


        score_show = font.render(f"Score: {score}",True, BLACK)
        screen.blit(score_show,(10,10))

        highscore_show = font.render(f"Hi Score: {highscore}",True, BLACK)
        screen.blit(highscore_show,(10,30))
        
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
