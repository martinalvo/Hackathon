import pygame
import random
pygame.init()
pygame.display.set_caption("Snake")
window = pygame.display.set_mode((629, 629))

run = True

# Defines how to Draw the background. 
def background():
    window.fill((0, 0, 0))
    lines = 29
    while lines < 574:
        pygame.draw.rect(window, (0, 128, 128), (lines, 0, 1, 629))
        pygame.draw.rect(window, (0, 128, 128), (0, lines, 629, 1))
        pygame.draw.rect(window, (0, 128, 128), (0, 0, 629, 30))
        pygame.draw.rect(window, (0, 128, 128), (0, 599, 629, 30))
        pygame.draw.rect(window, (0, 128, 128), (0, 0, 30, 629))
        pygame.draw.rect(window, (0, 128, 128), (599, 0, 30, 629))
        lines+=30

# Variables that determine the snakes movement and its size.
x = 30
y = 270
width = 29
height = 29
vel = 30
dirrection2 = 0
dirrection1 = 0
bodySize = 2

# Variables that determine apple location and if it should be drawn again or not.
apple = 0
applex = 0
appley = 0


# A list that will store the past cordinates of the head snake so that we can draw the body.
plays = [30, 270, 30, 270, 30, 270, 30, 270, 30, 270,]

# Variable to not draw body every single iteration of "while run" loop because if not it goes too fast.
frameRate = 3

while run:

    pygame.time.delay(50)

    # Closes app.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False 
    
    # Draws background.
    background()
    
    # Draws apple. Kind of like has to be hear because otherwise it just dosent draw.
    pygame.draw.rect(window, (255, 0, 0), (applex, appley, width, height))

    # This is to display the score in the screen in correct spot.  
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render("Score: " + str(bodySize - 2), True, (255, 0, 0), (0, 128, 128))
    textRect = text.get_rect()
    textRect.center = (60, 15)
    window.blit(text, textRect)

    # This and the next 4 if statments check to see if a key is pressed. If it is, then they change dirrection1 and dirrection2 to either a 1 or a 2, depending on the key pressed. This is used later to keep the snake constantly moving. The "and plays[-3] <= plays[-1]" is to keep the player from going into itself by going into itself thus killing itself.
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and plays[-3] >= plays[-1]:
        dirrection2 = 1 
        dirrection1 = 1
            
    if keys[pygame.K_DOWN] and plays[-3] <= plays[-1]:
        dirrection2 = 0
        dirrection1 = 1

    if keys[pygame.K_LEFT] and plays[-4] >= plays[-2]:
        dirrection2 = 1 
        dirrection1 = 0

    if keys[pygame.K_RIGHT] and plays[-4] <= plays[-2]:
        dirrection2 = 0
        dirrection1 = 0

    #  Use of the frameRate variable explained above
    if frameRate >= 3:
        
        # This checcks to see the amount of cords in the list, and if its greater than the bodySize*2 it delets the first two, which wont be usefull anymore. This prevents the list from growing to large and crashing the game.
        if len(plays) > bodySize*2:
            del plays[0]
            del plays[0]
                
        # This keeps the snake going in the dirrection that you pressed the key last.
        if dirrection2 == 1:
            if dirrection1 == 1:
                y-=vel
            elif dirrection1 == 0:
                x-=vel
            
        elif dirrection2 == 0:
            if dirrection1 == 1:
                y+=vel
            elif dirrection1 == 0:
                x+=vel
        
        #Draws head.
        pygame.draw.rect(window, (250, 180, 0), (x, y, width, height))

        # Boundaries of the game, if you hit them it stops the game.    
        if 30 > x or x > 599 or 30 > y or y > 599:
            run = False
            
       
        # Variable for body   
        increase = 0

        # This part is the one that draws the body of the snake. Basicaly it takes the coordinates acording to the size of the body, and increases by 2 every time in order to get the coords that are from the body after it.
        for i in range(bodySize):
            pastPlayx = plays[-bodySize*2 + increase]
            pastPlayy = plays[-bodySize*2 + increase +1]
            pygame.draw.rect(window, (175, 175, 0), (pastPlayx, pastPlayy, width, height))
            increase+=2
            
            # This checks so that the apple dosent print inside the snake by checking if the apple location is equal to the body coords of the curent piece of body. 
            if pastPlayx == applex and pastPlayy == appley:
                apple == 0
            
            # Checks if the head of the snake is body of snake.
            if x == pastPlayx and y == pastPlayy:
                run = False
        
        frameRate = 0
        
        pygame.display.update()
    
        # Adds current position of head to body so that it can be used by the body in the future.
        plays.append(x)
        plays.append(y)
    
    # Draws the apple if it was eaten by the snake (meaning apple = 0) in a random location.
    if apple == 0:
        applex = ((random.randint(1, 18))*30 + 30)
        appley = ((random.randint(1, 18))*30 + 30)
        apple = 1
    
    # Checks to see if head is in cords of apple, and if it is, then body increases and apple delets (aka apple = 0 so that code above runs).
    if x == applex and y == appley:
        pygame.draw.rect(window, (0, 0, 0), (applex, appley, width, height))
        apple = 0
        bodySize+=1
    
    # For the framerate thing   
    frameRate+=1

# Self explanatory
print("You lost. Your score was " + str(bodySize-2))
pygame.quit()
    
    
    