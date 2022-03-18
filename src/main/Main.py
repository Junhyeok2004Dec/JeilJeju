import pygame

pygame.init()

# define default vars


Color = (255, 255, 255)  # white
Black = (0, 0, 0)  # Black

size = [2560, 1080]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

font = pygame.font.SysFont("dotum", 95)

image = pygame.image.load("../assets/1.png")
image = pygame.transform.scale(image, (100, 100))

flag = None


def printText(string, color=(0, 0, 0), pos=(80, 80)):
    textSurface = font.render(string, True, pygame.Color(color), None)
    textRect = textSurface.get_rect()
    textRect.topleft = pos

    screen.blit(textSurface, textRect)


def mainWindow():
    global done, flag
    global buttons


    imageX = 0
    imageY = 0

    while not done:
        clock.tick(120)
        screen.fill(Color)

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                buttons = [pygame.key.name(keyName) for keyName, var in enumerate(pressed) if var]
                flag = True
            elif event.type == pygame.KEYUP:
                flag = False
            elif event.type == pygame.QUIT:
                done = True

        screen.blit(image, (imageX, imageY))

        if flag == True:
            printText(buttons[0] + 'Слава 發', (55,222,111), (80, 80))
        elif flag == False:
            printText(buttons[0] + '이 떼졌습니다....')
        else:
            printText("None")
        pygame.display.update()


mainWindow()
pygame.quit()
