import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

hero = pygame.image.load("./images/me1.png")


hero_rect = pygame.Rect(200, 300, 102, 126)
screen.blit(hero, hero_rect)
clock = pygame.time.Clock()

while True:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.K_DOWN:
            hero_rect.y -= 5
            screen.blit(hero, hero_rect)
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()
