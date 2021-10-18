import pygame

Max_bullet = 6
WIDTH, HEIGHT = 1280, 720
FPS = 60
BACKGROUND = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))
P_VELOCITY = 5
BULLET_VELOCITY = 7
PLAYER1 = pygame.image.load("red.png")
PLAYER2 = pygame.image.load("green.png")
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
FONT = pygame.font.SysFont("comicsan", 50)
P1_HEALTH = 10
P2_HEALTH = 10
BORDER = pygame.Rect(625, 0, 10, HEIGHT)

pygame.display.set_caption("Space War")
p1_pos = pygame.Rect(200, 200, 50, 50)
p2_pos = pygame.Rect(900, 200, 50, 50)
bullets = {"p1": [], "p2": []}


def winner():
    if P1_HEALTH == 0:
        text = FONT.render("Player 2 won!", True, (255, 255, 255))
        WINDOW.blit(text, (WIDTH//2-(text.get_width()//2),  HEIGHT//2 - (text.get_height()//2)))
        pygame.time.delay(50)
        pygame.display.update()
    if P2_HEALTH == 0:
        text = FONT.render("Player 1 won!", True, (255, 255, 255))
        WINDOW.blit(text, (WIDTH//2-BORDER.width//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(5000)
    if P1_HEALTH == 0 and P2_HEALTH == 0:
        text = FONT.render("No one won!", True, (255, 255, 255))
        WINDOW.blit(text, (WIDTH//2-BORDER.width//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(5000)


def handle_bullets():
    global P2_HEALTH, P1_HEALTH
    for bullet in bullets["p1"]:
        bullet.x += 5
        if (n := bullet.colliderect(p2_pos)) or (WIDTH - bullet.x) <= 1:
            bullets["p1"].remove(bullet)
            if n:
                P2_HEALTH -= 1
    for bullet in bullets["p2"]:
        bullet.x -= 5
        if (n := bullet.colliderect(p1_pos)) or bullet.x <= 1:
            bullets["p2"].remove(bullet)
            if n:
                P1_HEALTH -= 1
    for player1 in bullets["p1"]:
        for player2 in bullets["p2"]:
            if player2.colliderect(player1):
                bullets["p1"].remove(player1)
                bullets["p2"].remove(player2)
                print("bullets collided")


def handle_fire(player):
    if player == 1:
        if len(bullets["p1"]) < Max_bullet:
            bullet = pygame.Rect(p1_pos.x, p1_pos.y + 25, 4, 2)
            bullets["p1"].append(bullet)
    if player == 2:
        if len(bullets["p2"]) < Max_bullet:
            bullet = pygame.Rect(p2_pos.x, p2_pos.y + 25, 4, 2)
            bullets["p2"].append(bullet)


def handle_p1(keys):
    if keys[pygame.K_w]:
        if p1_pos.y - P_VELOCITY > 1:
            p1_pos.y -= P_VELOCITY
    if keys[pygame.K_s]:
        if HEIGHT - (p1_pos.y + 50 + P_VELOCITY) > 1:
            p1_pos.y += P_VELOCITY
    if keys[pygame.K_a]:
        if p1_pos.x - P_VELOCITY > 1:
            p1_pos.x -= P_VELOCITY
    if keys[pygame.K_d]:
        if BORDER.x - (p1_pos.x + P_VELOCITY + 50) > 1:
            p1_pos.x += P_VELOCITY


def handle_p2(keys):
    if keys[pygame.K_UP]:
        if p2_pos.y - P_VELOCITY > 1:
            p2_pos.y -= P_VELOCITY
    if keys[pygame.K_DOWN]:
        if (HEIGHT - (p2_pos.y + P_VELOCITY + 50)) > 1:
            p2_pos.y += P_VELOCITY
    if keys[pygame.K_LEFT]:
        if (p2_pos.x - P_VELOCITY) - (BORDER.x + BORDER.width) > 1:
            p2_pos.x -= P_VELOCITY
    if keys[pygame.K_RIGHT]:
        if WIDTH - (p2_pos.x + P_VELOCITY + 50) > 1:
            p2_pos.x += P_VELOCITY


def show():
    WINDOW.blit(BACKGROUND, (0, 0))
    # pygame.draw.rect(WINDOW, (1, 1, 1,), )
    WINDOW.blit(PLAYER1, p1_pos)
    WINDOW.blit(PLAYER2, p2_pos)
    pygame.draw.rect(WINDOW, (0, 0, 0), BORDER)
    for bullet in bullets["p2"]:
        pygame.draw.rect(WINDOW, (1, 0, 0, 0), bullet)
    for bullet in bullets["p1"]:
        pygame.draw.rect(WINDOW, (1, 0, 0, 0), bullet)
    p1_text = FONT.render(f"HEATH: {P1_HEALTH}", True, (255, 255, 255))
    p2_text = FONT.render(f"HEATH: {P2_HEALTH}", True, (255, 255, 255))
    p2_t_width = p2_text.get_rect().width
    WINDOW.blit(p1_text, (2, 2))
    WINDOW.blit(p2_text, (WIDTH - (p2_t_width + 10), 2))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    handle_fire(1)
                if event.key == pygame.K_RCTRL:
                    handle_fire(2)
        handle_bullets()
        keys = pygame.key.get_pressed()
        handle_p1(keys)
        handle_p2(keys)
        winner()

        show()

    pygame.quit()


if __name__ == '__main__':
    main()
