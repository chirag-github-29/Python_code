import pygame,sys
import random

pygame.init()    # general setup and initialization, init starts the game timer which runs till the close buttom is pressed
clock = pygame.time.Clock()  
def ball_restart():
    global ball_s_x, ball_s_y
    ball.center = (scr_wdt/2,scr_hgt/2)
    ball_s_y *= random.choice((1,-1))
    ball_s_x *= random.choice((1,-1))
     

def ball_animation():
    #animation
    global ball_s_x, ball_s_y
    ball.x += ball_s_x #rate of change in position of x coordinate of ball 
    ball.y += ball_s_y #rate of change in position of y coordinate of ball

    if ball.left <= 0: #bouncy edges on right and left  #?? difference between x coordinate and top and bottom definers ??
        global p_score
        ball_restart()
        p_score += 1

    if  ball.right >= scr_hgt:
        global o_score
        ball_restart()
        o_score += 1

    if ball.top <= 0 or ball.bottom >= scr_wdt: #bouncy edges on top and bottom
        ball_s_y *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_s_x *= -1

# setting up the main window
scr_hgt = 700
scr_wdt = 700
screen = pygame.display.set_mode((scr_hgt, scr_wdt)) #assinging the variables to the display fxn
pygame.display.set_caption("GAME")  #defining the name of the window

#rectangles design
ball = pygame.Rect(scr_wdt/2 - 11,scr_hgt/2 - 11,22,22) #defining the ball element
player = pygame.Rect(scr_wdt-20,scr_hgt/2 - 70,10,140)
opponent = pygame.Rect(10, scr_hgt/2 - 70,10,140)

#defining colors
bg_color = pygame.Color('grey12')  #defing a color varible used in future
lightgrey = (200,200,200) #defing a color varible used in future

#defining motion variables 
ball_s_x = 5 * random.choice((1,-1))
ball_s_y = 5 * random.choice((1,-1))
player_s = 0
opponent_s = 7

#Score
p_score = 0
o_score = 0
game_font = pygame.font.SysFont("Calibribold",32)

#Score Timer
score_timer = None

#to check if the close button is pressed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  #exits the pygame module
            sys.exit()     #exits the window(system command)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            player_s += 7
        if event.key == pygame.K_UP:
            player_s -= 7

    if opponent.top < ball.y:
        opponent.top += opponent_s
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_s
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= scr_hgt:
        opponent.bottom = scr_hgt

    player.y = player_s
    if player.top <= 0:
        player.top = 0
    if player.bottom >= scr_hgt:
        player.bottom = scr_hgt

    ball_animation()

    

    #color assignment(whole system works in layers format)
    screen.fill(bg_color) #element which don't need draw command
    pygame.draw.rect(screen,lightgrey,player)  #drawn first, at bottom
    pygame.draw.rect(screen,lightgrey,opponent)
    pygame.draw.ellipse(screen,lightgrey,ball)  
    pygame.draw.aaline(screen,lightgrey,(scr_wdt/2,0), (scr_wdt/2, scr_hgt)) #drawn last, on top 

    player_text = game_font.render(f"{p_score}",False,lightgrey)
    screen.blit(player_text,(366,350)) #blit function is used to put a surface on other surface
    opponent_text = game_font.render(f"{o_score}",False,lightgrey)
    screen.blit(opponent_text,(306,350))
    
    #updating the window
    pygame.display.flip()  #draws whatever happens on the loop
    clock.tick(60)       #controls the FPS(basically how often a computer run cycles in a minute) of the game{in this case its 60}


