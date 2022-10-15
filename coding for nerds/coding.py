import pygame, sys, random, math
pygame.init()




size = width, height = (2000, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Code For Nerds")

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
colors = [blue, red, green]
random_colors = random.choice(colors)

game_stage = 'INTRO'


running = True
while running == True:
    #game_stage changing buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_w:
                random_colors = random.choice(colors)
                screen.fill(random_colors)
        if event.type == pygame.MOUSEBUTTONDOWN:
            random_colors = random.choice(colors)
            screen.fill(random_colors)


    pygame.display.update()












pygame.quit()
sys.exit()