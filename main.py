from Button import *
from Obstacle import *

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 40)
running = True
paused = True
gameOver = False

#Game Variables
counter = 0
pygame.time.set_timer(pygame.USEREVENT, 1000)
player_pos = pygame.Vector2(50, 250)
player_speed = 0
gravity = 0.098
jump_power = -3.5
scroll_speed = 5

def unpause():
    global paused
    paused = False
def exit_game():
    global running
    running = False

paused_button = Button(screen, font, 250, 250, 80, 40, "Play", unpause)
exit_button = Button(screen, font, 250, 250, 80, 40, "Exit", exit_game)

obstacles = []

while running:
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_speed = jump_power
        if event.type == pygame.USEREVENT and not gameOver and not paused:
            counter += 1
            #Generate obstacles
            obstacle = Obstacle(screen, scroll_speed)
            obstacles.append(obstacle)

    #Logic for game
    if gameOver:
        screen.fill("red")
        screen.blit(font.render("Game Over", True, pygame.Color("red")), (screen.get_width()/2, screen.get_height()/2))
        exit_button.process()

    elif not paused:
        if player_pos.y < 0 or player_pos.y > 500:
            gameOver = True



        player_speed += gravity
        player_pos.y += player_speed


        #Render Screen
        screen.fill("cyan")
        pygame.draw.circle(screen, "yellow", player_pos, 10)
        for item in obstacles:
            if item.upper_rect.x < -100:
                obstacles.remove(item)
            else:
                item.process()
                #rects = item.get_rects()
                #if rects[0].colliderect(player_pos) or rects[1].colliderect(player_pos):
                #    game_over = True
        screen.blit(font.render(f"Score: {counter}", True, pygame.Color("white")), (100, 0))
        #Send frame to screen

    else:
        screen.fill("white")
        paused_button.process()




    pygame.display.flip()
    clock.tick(60)
pygame.quit()