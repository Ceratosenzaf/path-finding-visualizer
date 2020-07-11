from src.manager import make_empty_table
from src.dijkstra_algorithm.dijkstra import Dijkstra
import pygame
pygame.init()


WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

pygame.display.set_caption('Path Finding Visualizer')

FPS = 60
clock = pygame.time.Clock()


# initialize table
table_width = (WIDTH - 1) // 31
table_height = round(HEIGHT * 3 / 4) // 31
sp_x = WIDTH - table_width * 31
sp_y = HEIGHT - table_height * 31

table = make_empty_table(table_width, table_height, start = (7,6), end=(30,17))
# print(table)


# algo
dj = Dijkstra(table)

# run game
def run():
    run = True
    while run:
        clock.tick(FPS)

        # set bg color
        screen.fill((0,0,0))

        # update table
        # if dj.non_visited_nodes and dj.path == []:
            # result = dj.run()

        table = dj.get_table()


        # draw table
        for y in range (table_height):
            for x in range (table_width):
                if table[x][y] == 'start':
                    color = (68, 227, 21)
                    pygame.draw.rect(screen, color, pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))
                
                elif table[x][y] == 'end':
                    color = (227, 21, 21)
                    pygame.draw.rect(screen, color, pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))

                elif table[x][y].startswith('space') and f'space-{x}-{y}' in dj.non_visited_nodes:
                    color = (222,222,222)
                    pygame.draw.rect(screen, color, pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))

                elif table[x][y].startswith('wall'):
                    color = (0,0,0)
                    pygame.draw.rect(screen, color, pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))

                elif f'space-{x}-{y}' not in dj.non_visited_nodes:
                    color = (241, 159, 248)
                    pygame.draw.rect(screen, color, pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))

                for node in dj.path:
                    if node.endswith(f'space-{x}-{y}'):
                        color = (91, 97, 215)
                        pygame.draw.rect(screen, color, pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))

            
        # event handler
        for event in pygame.event.get():
            # handle exit
            if event.type == pygame.QUIT:
                pygame.quit() 
                return None

            # handle clicks
            if pygame.mouse.get_pressed()[0]:
                try:
                    x,y = event.pos
                    
                except AttributeError:
                    pass

        
        
        pygame.display.update()


    pygame.quit() 


if __name__ == "__main__":
    run()
