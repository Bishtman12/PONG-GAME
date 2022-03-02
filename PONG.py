import random
import pygame
import sys

#GAME SETUP
pygame.init()
clock = pygame.time.Clock()
# GAME MOVEMENTS
def ball_movement():

    global ball_speedx , ball_speedy , player_score , opponent_score, ROUND,timer
    ball.x += ball_speedx
    ball.y += ball_speedy
    if ball.top <= 70 or ball.bottom >= screen_height:
        ball_speedy *= -1
    if ball.left <= 0 : # Player Won
        player_score += 1
        ROUND += 1
        timer = pygame.time.get_ticks()  # gets the time of the round
    if ball.right >= screen_width:  #  Player Lost
        opponent_score += 1
        ROUND += 1
        timer = pygame.time.get_ticks()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speedx *= -1

def player_movement():

    player.y += player_speed
    if player.top <= 70:
        player.top = 70
    if player.bottom >= screen_height:
        player.bottom = screen_height

def com_movement():

    if opponent.centery < ball.centery:
        opponent.top += opponent_speed
    if opponent.centery > ball.centery :
        opponent.bottom -= opponent_speed
    if opponent.top <= 70:
        opponent.top = 70
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speedx, ball_speedy,timer

    current_time = pygame.time.get_ticks() # this gets the time of the round
    ball.center = (screen_width/2,screen_height/2)

    if current_time - timer < 700:
        one = counter_font.render("3" , False , light_grey)
        screen.blit(one,(screen_width/2 -30,screen_height/2 + 20))

    if 700<current_time - timer < 1400:
        two = counter_font.render("2" , False , light_grey)
        screen.blit(two,(screen_width/2 -30,screen_height/2 + 20))

    if 1400<current_time - timer < 2100:
        three = counter_font.render("1" , False , light_grey)
        screen.blit(three,(screen_width/2 -30,screen_height/2 + 20))

    if current_time - timer < 2100:
        ball_speedx,ball_speedy = 0,0
    else:
        ball_speedx = 7*random.choice((1, -1))
        ball_speedy = 7*random.choice((1, -1))
        timer = 0

#GAME WINDOW
screen_width = 1200
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")

# GAME GEOMETRY
ball = pygame.Rect(screen_width/2 - 15 , screen_height/2 - 15 , 30 , 30) # ball is taken as rect for easy calc.
player = pygame.Rect(screen_width - 20, screen_height/2-70, 10 ,140)  # player is on the right side
opponent = pygame.Rect(10,screen_height/2-70 , 10, 140)  # opp is on the left side

#GAME PHYSICS
ball_speedx = 7 * random.choice((1, -1))
ball_speedy = 7 * random.choice((1, -1))

player_speed = 0
opponent_speed = 6.5

#COLORS
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)
font = pygame.font.SysFont('Comic Sans MS', 90)

#SCORE BOARD
player_score = 0
opponent_score = 0
ROUND = 1
score_font = pygame.font.Font('freesansbold.ttf' ,40 )
counter_font = pygame.font.Font('freesansbold.ttf' ,60 )

# Timer
timer = 3

#GAME LOGIC
while True:
    for event in pygame.event.get():  # getting the user input in pygame
        if event.type == pygame.QUIT:  # quit func.
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7

    # Calling functions here
    ball_movement()
    player_movement()
    com_movement()


    #Layers
    screen.fill(bg_color)


    Round_text = score_font.render(f"ROUND {ROUND}",False,light_grey)
    screen.blit(Round_text,(screen_width/2 - 75,10))
    player_text = score_font.render(f"Your Score {player_score}", False, light_grey)
    screen.blit(player_text, (screen_width - 300,10))
    opponent_text = score_font.render(f"Opponent Score {opponent_score}", False, light_grey)
    screen.blit(opponent_text, (0, 10))
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)

    pygame.draw.aaline(screen, light_grey,(0,70) , (screen_width,70)) # Set physics for this thing now


    pygame.draw.aaline(screen,light_grey,(screen_width/2,70),(screen_width/2,screen_height))
    if timer:
        ball_restart()
    # updating the windows
    pygame.display.flip()
    clock.tick(60)
