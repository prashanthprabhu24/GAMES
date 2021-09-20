# AI plays
import pygame  # setup
import time
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Covid-19')
keepGoing = True
pic = pygame.image.load('img1.bmp')
colorkey = pic.get_at((0, 0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
timer = pygame.time.Clock()
speedx = 5
speedy = 5
paddlew = 200
paddleh = 25
#paddlex = 400
paddley = 550
picw = 100
pich = 100
points = 0
lives = 5
font = pygame.font.SysFont("Times", 24)
#pygame.mixer.init()  # add sounds
#blip = pygame.mixer.Sound("blap.wav")

while keepGoing:  # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F2:  # F2 = New Game
                points = 0
                lives = 5
                picx = 0
                picy = 0
                speedx = 1
                speedy = 1

    picx += speedx
    picy += speedy

    if picx <= 0 or picx >= 700:
        speedx = -speedx * 1.1
    if picy <= 0:
        speedy = -speedy + 1
    if picy >= 550:
        lives -= 1
        speedy = -5
        speedx = 5
        picy = 499
        blap.play()

    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))

    # draw paddle
    #paddlex = pygame.mouse.get_pos()[0]
    '''paddlex = 5
    if picx + picw / 2 < paddlex-100:
        paddlex -= picx + picw / 2  # go left
    elif picx + picw / 2 > paddlex :
        paddlex += picx + picw / 2  # go right'''
    paddlex = picx + picw / 2
    paddlex -= paddlew / 2
    pygame.draw.rect(screen, WHITE, (paddlex, paddley, paddlew, paddleh))

    # check for paddle bounce
    if picy + pich >= paddley+50 and picy + pich <= paddley + paddleh+50 and speedy > 0:
        if picx + picw / 2 >= paddlex and picx + picw / 2 <= paddlex + paddlew:
            speedy = -speedy
            points += 1
            #blip.play()

    # draw text on screen
    draw_string = 'Lives: ' + str(lives) + ' Points: ' + str(points)
    # check to see if the game's over
    if lives < 1:
        speedx = speedy = 0
        draw_string = 'Game Over. Your score was: ' + str(points) + '. Press F1 to play again.'
    #draw_string = 'Lives saved  : 3,15,44,713     Cases remaining :  2,14,91,598 '
    text = font.render(draw_string, True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text, text_rect)
    text = font.render('VACCINE', True, 'black')
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = paddley
    text_rect.x = paddlex+50
    screen.blit(text, text_rect)

    pygame.display.update()
    timer.tick(30)

pygame.quit()  # exit
