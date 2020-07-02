from src.manager import make_empty_table
import pygame
pygame.init()

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
# WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

pygame.display.set_caption('Path Finding Visualizer')

FPS = 60
clock = pygame.time.Clock()

run = True

# initialize table
table_width = (WIDTH - 1) // 31
table_height = round(HEIGHT * 3 / 4) // 31
sp_x = WIDTH - table_width * 31
sp_y = HEIGHT - table_height * 31

table = make_empty_table(table_width, table_height, start = (0,0), end=(5,6))
print(table)


while run:
    clock.tick(FPS)
    pygame.display.update()

    # set bg color
    screen.fill((21,146,227))


    

    for y in range (table_height):
        for x in range (table_width):
            pygame.draw.rect(screen, (222, 222, 222), pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))


    # event handler
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False
    


pygame.quit() 