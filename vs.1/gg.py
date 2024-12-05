import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 400))#畫面大小

#載入圖片
img_dino = pygame.image.load("dino.png")
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
cactus_height = 80
cactus_rects = []
cactus_velocity = 5 

clock = pygame.time.Clock()

score = 0  # 初始分數
font = pygame.font.Font(None, 36)

running = True

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 開始跳躍
                is_jumping = True
                
                
    # fill the screen with a color to wipe away anything from last frame
    screen.fill((255,255,255))

    # 跳躍邏輯
    if is_jumping:
        dino_rect.y -= now_jump
        now_jump -= g  # 重力作用
        if dino_rect.y >= 300:  # 恐龍落回地面
            dino_rect.y = 300
            now_jump=jump
            is_jumping = False
            

   
    # 生成仙人掌
    if random.randint(1, 100) == 1:
        cactus_rect = pygame.Rect(1280, 300, cactus_width, cactus_height)
        cactus_rects.append(cactus_rect)
  
    # 移動仙人掌
    for cactus_rect in cactus_rects:
        cactus_rect.x -= cactus_velocity
        if cactus_rect.x < -cactus_width:
            cactus_rects.remove(cactus_rect)


     # 碰撞檢測
    for cactus_rect in cactus_rects:
        if dino_rect.colliderect(cactus_rect):
            print("Game Over!")
            running = False

    # 更新分數（每幀增加）
    score += 1

    # 顯示分數
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))  # 顯示在畫面左上角


    # RENDER YOUR GAME HERE
    screen.blit(img_dino,dino_rect)
    for cactus_rect in cactus_rects:
        screen.blit(img_cactus, cactus_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()