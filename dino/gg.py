import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 400))#畫面大小

#載入圖片
img_dino = pygame.image.load("dino.png")
img_dinorun=[pygame.image.load("DinoRun1.png"),pygame.image.load("DinoRun2.png")]


img_cactus = pygame.image.load("cactus.png")
img_dino = pygame.transform.scale(img_dino,(100,100))



#設定角色
dino_rect = img_dino.get_rect()
dino_rect.x = 50
dino_rect.y = 300
jump = 15  # 恐龍垂直速度
is_jumping = False
g= 0.5  # 重力   
now_jump =jump  # 跳躍力度

#設定仙人掌
cactus_width = 30
cactus_height = 50
cactus_rects = []
cactus_velocity = 5 

clock = pygame.time.Clock()

score = 0  # 初始分數
highscore=0

font = pygame.font.Font(None, 36)
gameover= False
running = True
def spawn_cactus(cactus_width, cactus_height, cactus_rects):
            if random.randint(1, 100) == 1:
             cactus_rect = pygame.Rect(1280, 300, cactus_width, cactus_height)
             cactus_rects.append(cactus_rect)





while running:
    spawn_cactus(cactus_width, cactus_height, cactus_rects)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 開始跳躍
                is_jumping = True
            if event.key == pygame.K_r:
                score=0
                gameover= False
                cactus_rects.clear()
                spawn_cactus(cactus_width, cactus_height, cactus_rects)
                

        if event.type == pygame.MOUSEBUTTONDOWN:
            is_jumping =True
            

                
                
    # fill the screen with a color to wipe away anything from last frame
    

    if not gameover:
        if is_jumping:
            dino_rect.y -= now_jump
            now_jump -= g  # 重力作用
            if dino_rect.y >= 300:  # 恐龍落回地面
                dino_rect.y = 300
                now_jump=jump
                is_jumping = False
                

    
        

    
        # 移動仙人掌
        for cactus_rect in cactus_rects:
            cactus_rect.x -= cactus_velocity
            if cactus_rect.x < -cactus_width:
                cactus_rects.remove(cactus_rect)


        # 碰撞檢測
        for cactus_rect in cactus_rects:
            if dino_rect.colliderect(cactus_rect):
                if score > highscore:
                    highscore=score
                gameover=True
                
        screen.fill((255,255,255))
        # 更新分數（每幀增加）
        score += 1

        # 顯示分數
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))  # 顯示在畫面左上角
        
        hiscore_text = font.render(f" hi Score: {highscore}", True, (0, 0, 0))
        screen.blit(hiscore_text, (10, 30))


        
        if gameover:
            GAMEOVER_text = font.render(f"GAME OVER!!", True, (0,0,0))
            screen.blit(GAMEOVER_text, (550, 150))



        # RENDER YOUR GAME HERE
        screen.blit(img_dino,dino_rect)
        for cactus_rect in cactus_rects:
            screen.blit(img_cactus, cactus_rect)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

pygame.quit()