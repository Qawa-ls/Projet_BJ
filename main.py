import pygame

pygame.init()

screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello world app")

font = pygame.font.SysFont(None, 48)
text = font.render("Hello World!", True, (255, 255, 255))
text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()