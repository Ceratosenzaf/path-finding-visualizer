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


# run game
def run():
    run = True
    run_algo = False

    # algo
    table = make_empty_table(table_width, table_height, start = (21,12), end=(39,12))
    dj = Dijkstra(table)

    while run:
        clock.tick(FPS)

        # set bg color
        screen.fill((0,0,0))


        #run algo
        if run_algo:
            screen.blit(pygame.font.SysFont('Arial', 25).render('Running', True, (173, 176, 227)), (WIDTH / 2 - 35, 20))
            if dj.non_visited_nodes and dj.path == []:
                result = dj.run()
                if result == None: # if there is no path
                    run_algo = False
            else:
                run_algo = False


        # update table
        table = dj.get_table()


        # draw GUI
        minimize = pygame.draw.rect(screen, (173, 176, 227), pygame.Rect(WIDTH - 80, 10, 30, 20))
        screen.blit(pygame.font.SysFont('Arial', 20, True).render('-', True, (0,0,0)), (WIDTH - 67, 6))

        close = pygame.draw.rect(screen, (173, 176, 227), pygame.Rect(WIDTH - 40, 10, 30, 20))
        screen.blit(pygame.font.SysFont('Arial', 20, True).render('X', True, (0,0,0)), (WIDTH - 30, 8))

        start = pygame.draw.rect(screen, (173, 176, 227), pygame.Rect(WIDTH / 2 - 170, sp_y / 2 - 30, 160, 60))
        screen.blit(pygame.font.SysFont('Arial', 25).render('RUN ALGO', True, (0,0,0)), (WIDTH / 2 - 145, sp_y / 2 - 15))

        clear = pygame.draw.rect(screen, (173, 176, 227), pygame.Rect(WIDTH / 2 + 10, sp_y / 2 - 30, 160, 60))
        screen.blit(pygame.font.SysFont('Arial', 25).render('CLEAR', True, (0,0,0)), (WIDTH / 2 + 53, sp_y / 2 - 15))


        # draw table
        for y in range (table_height):
            for x in range (table_width):
                if table[x][y] == 'start':      # start
                    color = (68, 227, 21)
                    pygame.draw.rect(screen, color, pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))
                
                elif table[x][y] == 'end':      # end
                    color = (227, 21, 21)
                    pygame.draw.rect(screen, color, pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))

                elif table[x][y].startswith('space') and f'space-{x}-{y}' in dj.non_visited_nodes:      # empty
                    color = (222,222,222)
                    pygame.draw.rect(screen, color, pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))

                elif table[x][y].startswith('wall'):        # wall
                    color = (0,0,0)
                    pygame.draw.rect(screen, color, pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))

                elif f'space-{x}-{y}' not in dj.non_visited_nodes:      # visited
                    color = (241, 159, 248)
                    pygame.draw.rect(screen, color, pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))

                for node in dj.path:        # quick path
                    if node.endswith(f'space-{x}-{y}'):
                        color = (91, 97, 215)
                        pygame.draw.rect(screen, color, pygame.Rect(x * 31 + sp_x/2, y * 31 + sp_y - sp_x/2, 30, 30))

            
        # event handler
        for event in pygame.event.get():
            # handle exit
            if event.type == pygame.QUIT:
                pygame.quit() 
                return None

            # handle left click on board (place wall)
            if pygame.mouse.get_pressed()[0] and not run_algo:
                try:
                    x,y = event.pos
                    t_x, t_y = (round(x - sp_x/2)//31, round(y - sp_y + sp_x/2)//31)
                    if x >= sp_x/2 and x <= (WIDTH - sp_x/2) and y >= sp_y - sp_x/2 and y < HEIGHT - sp_x/2 and table[t_x][t_y].startswith('space'):
                        table[t_x][t_y] = table[t_x][t_y].replace('space', 'wall')
                        dj.set_table(table)    
                except:
                    pass
            
            # handle right click on board (remove wall)
            if pygame.mouse.get_pressed()[2] and not run_algo:
                try:
                    x,y = event.pos
                    t_x, t_y = (round(x - sp_x/2)//31, round(y - sp_y + sp_x/2)//31)
                    if x >= sp_x/2 and x <= (WIDTH - sp_x/2) and y >= sp_y - sp_x/2 and y < HEIGHT - sp_x/2 and table[t_x][t_y].startswith('wall'):
                        table[t_x][t_y] = table[t_x][t_y].replace('wall', 'space')
                        dj.set_table(table)    
                except:
                    pass

            # handle wheel click on board (move start/end)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2 and not run_algo:
                starting_pos = event.pos
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 2 and not run_algo:
                final_pos = event.pos
                st_x, st_y = (round(starting_pos[0] - sp_x/2)//31, round(starting_pos[1] - sp_y + sp_x/2)//31)
                fi_x, fi_y = (round(final_pos[0] - sp_x/2)//31, round(final_pos[1] - sp_y + sp_x/2)//31)
                if (table[st_x][st_y] == 'start' or table[st_x][st_y] == 'end') and (table[fi_x][fi_y] != 'start' and table[fi_x][fi_y] != 'end') and (starting_pos[0] >= sp_x/2 and starting_pos[0] <= (WIDTH - sp_x/2) and starting_pos[1] >= sp_y - sp_x/2 and starting_pos[1] < HEIGHT - sp_x/2) and (final_pos[0] >= sp_x/2 and final_pos[0] <= (WIDTH - sp_x/2) and final_pos[1] >= sp_y - sp_x/2 and final_pos[1] < HEIGHT - sp_x/2):
                    table[fi_x][fi_y] = table[st_x][st_y]
                    table[st_x][st_y] = f'space-{st_x}-{st_y}'
                    dj.set_table(table)
        
            
            # start algo
            if pygame.mouse.get_pressed()[0] and start.collidepoint(pygame.mouse.get_pos()) and not run_algo:
                dj = Dijkstra(table)
                run_algo = True

            # clear path
            if pygame.mouse.get_pressed()[0] and clear.collidepoint(pygame.mouse.get_pos()) and not run_algo:
                table = make_empty_table(table_width, table_height, start = (21,12), end=(39,12))
                dj = Dijkstra(table)
            
            # minimize
            if pygame.mouse.get_pressed()[0] and minimize.collidepoint(pygame.mouse.get_pos()) and not run_algo:
                pygame.display.iconify()
                
            # close
            if pygame.mouse.get_pressed()[0] and close.collidepoint(pygame.mouse.get_pos()) and not run_algo:
                pygame.quit() 
                return None

        # refresh screen
        pygame.display.update()


    pygame.quit() 


if __name__ == "__main__":
    run()
