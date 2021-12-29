import pygame
import random
import os

pygame.mixer.init()


pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0,0,255)
green = (0,255,0)
grey = (128,128,128)
pink_shader = (255,129,109)
snakegreen = (35, 45, 40)

bg = pygame.image.load("Screen/bg.jpg")
bg2 = pygame.image.load("Screen/bg2.jpg")
intro = pygame.image.load("Screen/intro.png")
outro = pygame.image.load("Screen/outro.png")

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SnakesWithmission")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Harrington", 35)



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

pygame.mixer.music.load("music/wc.mp3")
pygame.mixer.music.play()

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.blit(intro,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("music/bgm.mp3")
                    pygame.mixer.music.play()

                    gameloop()



        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45 
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    if(not os.path.exists("highscore.txt")):
       with open("highscore.txt", "w") as f:
           f.write("0")
    with open ("highscore.txt","r") as f:
        highscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    while not exit_game:
        
        if game_over:
            

            with open ("highscore.txt","w") as f:
                f.write(str (highscore))
            gameWindow.blit(outro,(0,0))
            text_screen("Score: " + str(score )+'''  HighScore: '''+str(highscore), snakegreen, 305, 350)

            


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10
                        snk_length += 5
                        if score>int(highscore):
                            highscore = score

                    if event.key == pygame.K_m:
                        score -= 5
                        snk_length -= 5
                        if score>int(highscore):
                            highscore = score

                    if event.key == pygame.K_a:
                        score = 0
                        snk_length = 5
                        highscore = 0

                    if event.key == pygame.K_c:
                        score += 300
                        snk_length += 160
                        if score>int(highscore):
                            highscore = score


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<9 and abs(snake_y - food_y)<9:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(highscore):
                    highscore = score

            gameWindow.blit(bg,(0,0))
            text_screen("                        Score: " + str(score)+"     HighScore: "+str(highscore), snakegreen, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('music/bgm1.mp3')
                pygame.mixer.music.play(100)

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('music/bgm2.mp3')
                pygame.mixer.music.play(100)
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
