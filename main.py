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
high_score = 0
with open('score.txt', 'a+') as file:
    file.seek(0)
    text = file.readlines()
    if len(text) > 0:
        high_score = int(text[0])


pygame.time.set_timer(pygame.USEREVENT, 1000)
player_pos = pygame.Vector2(50, 250)
player_speed = 0
gravity = 0.15
jump_power = -3.5
scroll_speed = 5

obstacles = []

def unpause():
    global paused
    paused = False
def exit_game():
    global running
    running = False
def replay():
    global gameOver, paused, counter, obstacles, player_pos, player_speed
    #Resets the entire game
    gameOver = False
    paused = True
    counter = 0
    obstacles = []
    player_pos = pygame.Vector2(50, 250)
    player_speed = 0

paused_button = Button(screen, font, 250, 250, 80, 40, "Play", unpause)
exit_button = Button(screen, font, 250, 250, 80, 40, "Exit", exit_game)
replay_button = Button(screen, font, 230, 320, 80, 40, "Replay", replay)

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
        if counter > high_score:
            high_score = counter
            with open('score.txt', 'w') as file:
                file.write(str(high_score))

        screen.fill("red")
        screen.blit(font.render("Game Over", True, pygame.Color("black")), (screen.get_width()/2 - 90, 50))
        screen.blit(font.render(f"Score: {counter}", True, pygame.Color("black")),(screen.get_width() / 2 - 70, 410))
        screen.blit(font.render(f"High Score: {high_score}", True, pygame.Color("black")), (screen.get_width()/2 - 110, 450))
        replay_button.process()
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
                if item.check_collision(player_pos):
                    gameOver = True
        screen.blit(font.render(f"Score: {counter}", True, pygame.Color("white")), (100, 0))
        #Send frame to screen

    else:
        screen.fill("white")
        paused_button.process()
        screen.blit(font.render(f"High Score: {high_score}", True, pygame.Color("black")), (screen.get_width()/2 - 110, 450))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()