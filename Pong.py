import pygame
pygame.init()
pygame.display.set_caption("Pong")
window = pygame.display.set_mode((900, 635))

# Draws background.
def background():
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (0, 128, 128), (0, 0, 900, 45))
    pygame.draw.rect(window, (0, 128, 128), (0, 620, 900, 15))
    pygame.draw.rect(window, (0, 128, 128), (0, 0, 15, 900))
    pygame.draw.rect(window, (0, 128, 128), (885, 0, 15, 900))

# Variables for the paddles (both).
x1 = 60
y1 = 282
x2 = 840
y2 = 282
width = 5
height = 91
vel = 2

# Variables for the ball.
circlex = 450
circley = 318
raidius = 10
velx = -45//10
vely = 30//10

# So that the ball dosent get drawn every time the while loop loops (it would be to fast).
frameRate = 2

run = True
while run:
    
    pygame.time.delay(5)
    
    # Quits game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    # Determines centers of paddles. Used to determine which dirrection the ball should.
    centery = y1 + (height-1)/2 + 1
    centery2 = y2 + (height-1)/2 + 1
    
    # Framerate thing
    if frameRate == 2:
        
        # This if statement is to see if the ball is in the y range of the left paddle and in the x value. Same for the elif below but for other paddle.
        if y1 <= circley and circley <= y1 + height and x1 + width >= (circlex - raidius) >= x1:
            
            # Checks the position of the ball compared to the paddle, and if its above the center it bounces up, below the center down, and if its in the center then goes straight. It also changes the x value of dirreciton. Same for the other paddle just that opposits for x values.
            if circley < centery:
                vely = -(centery - circley)//10
                velx+=velx*-2
            elif circley > centery:
                vely = (circley - centery)//10
                velx+=velx*-2
            else:
                velx+=velx*-2
                vely = 0

        elif y2 <= circley and circley <= y2 + height and x2 <= (circlex + raidius) <= x2 + width:
            if circley < centery2:
                vely = -(centery2 - circley)//10
                velx+=velx*-2
            elif circley > centery2:
                vely = (circley - centery2)//10
                velx+=velx*-2
            else:
                velx+=velx*-2
                vely = 0      

        # Changes position of ball
        circlex+=velx
        circley+=vely
        
        # For the framerate thing
        frameRate = 0
    
    # Checks to see if the ball touches the top and botom boundaries. If it does, then reverse the y value.
    if circley + raidius + vely >= 620 or 45 >= circley - raidius + vely:
        vely+=vely*-2

    # This and the ifs below check to see if the players click keys, and if so, move the paddles acordingly.
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and y1 - vel >= 45:
        y1-=vel
    
    if keys[pygame.K_s] and y1 + vel + height <= 620 :
        y1+=vel

    if keys[pygame.K_UP] and y2 - vel >= 45:
        y2-=vel

    if keys[pygame.K_DOWN] and y2 + vel + height <= 620 :
        y2+=vel

    # This is to check if the ball got past one of the paddles. Prints player who won.
    if circlex + raidius >= 885:
        run == False
        print("Player 1 won!")
        break
    elif circlex - raidius <= 15:
        run == False
        print("Player 2 won!")
        break
        
    # Draws background
    background()

    # Draws ball and paddles.
    pygame.draw.rect(window, (175, 175, 0), (x1, y1, width, height))
    pygame.draw.rect(window, (175, 175, 0), (x2, y2, width, height))
    pygame.draw.circle(window, (175, 175, 0), (int(circlex), int(circley)), raidius )
    
    pygame.display.update()

    # Framerate thing
    frameRate+=1

pygame.quit()
   

