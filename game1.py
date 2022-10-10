import pygame

pygame.init()

WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)

bricks1 = [pygame.Rect(10 + i * 85, 60, 70, 30) for i in range(7)]
bricks2 = [pygame.Rect(10 + i * 85, 100, 70, 30) for i in range(7)]
bricks3 = [pygame.Rect(10 + i * 85, 140, 70, 30) for i in range(7)]

def draw_brick(bricks,color):
    for i in bricks:
        pygame.draw.rect(screen, color, i)
score = 0

lifs=3

initial_padell=[230,450]
initial_ball=[275,440]

velocity = [1, 1]

size = (600, 600)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Bricks Game")

paddle = pygame.Rect(230, 450, 100, 10)
ball = pygame.Rect(275, 440, 10, 10)

gameContinue = True

firsttime=True

finalwall=False

topcount=0

wallcount=0
def initialcond(initial_padell,initila_ball):
    paddle.x = initial_padell[0]
    paddle.y = initial_padell[1]
    ball.x = initial_ball[0]
    ball.y = initial_ball[1]
    pygame.draw.rect(screen, LIGHTBLUE, paddle)
    pygame.draw.rect(screen, WHITE, ball)

while gameContinue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameContinue = False

    screen.fill(DARKBLUE)

    pygame.draw.rect(screen, LIGHTBLUE, paddle)

    font = pygame.font.Font(None, 34)

    text = font.render("SCORE: " + str(score), 1, WHITE)
    li_txt=font.render("BALLS: "+str(lifs),'1',WHITE)
    screen.blit(text, (20, 10))
    screen.blit(li_txt,(180,10))

    # creating bricks
    draw_brick(bricks1,'RED')
    draw_brick(bricks2,'YELLOW')
    draw_brick(bricks3,'GREEN')

    pygame.draw.rect(screen, WHITE, ball)
    # paddle move:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x < 540:
                paddle.x = paddle.x + 2

        if event.key == pygame.K_LEFT:
            if paddle.x > 0:
                paddle.x = paddle.x - 2

    if firsttime:
        if event.type==pygame.KEYDOWN:
            firsttime=False

        pygame.time.wait(1)
        pygame.display.flip()
        continue

    ball.y = ball.y - velocity[1]
    if not finalwall:
        ball.x = ball.x + velocity[0]

    if ball.y <= 3:
        velocity[1] = -velocity[1]

        #firsttime=True


    if ball.x > 590 or ball.x <= 0:
        wallcount=wallcount+1
        velocity[0] = -velocity[0]
        boththewalls=True
        #finalwall=False

    if paddle.collidepoint(ball.x, ball.y):
        wallcount=0
        velocity[1] = -velocity[1]
        finalwall=False

    if ball.y >= 590:
        lifs = lifs - 1
        initialcond(initial_padell, initial_ball)
        wallcount = 0



    if lifs<=0:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over ", 1, RED)
        screen.blit(text, (150, 350))

        pygame.display.flip()

        pygame.time.wait(2000)

        break;

    for i in bricks1:
        if i.collidepoint(ball.x, ball.y):
            bricks1.remove(i)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score = score + 1
            try:
                p=bricks2[i]
                p1=bricks3[i]

            except:
                finalwall=True

            wallcount=0

    for i in bricks2:
        if i.collidepoint(ball.x, ball.y):
            bricks2.remove(i)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score = score + 1
            finalwall=False
            boththewalls=False
            wallcount=0

    for i in bricks3:
        if i.collidepoint(ball.x, ball.y):
            bricks3.remove(i)
            #velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score = score + 1
            finalwall=False
            boththewalls=False
            wallcount=0

    if wallcount>=2:
        lifs=lifs-1
        initialcond(initial_padell,initial_ball)


    if score == 21:
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WON ", 1, RED)
        screen.blit(text, (150, 350))
        pygame.display.flip()

        pygame.time.wait(3000)
        break;
    pygame.time.wait(1)
    pygame.display.flip()