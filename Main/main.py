import pygame

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
background_img = pygame.image.load('background1.jpg')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Chines Chess")
icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)

# load button 'start' game
startImg = pygame.image.load('start_btn.png')
# load button 'exit' game
exitImg = pygame.image.load('exit_btn.png')


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height*scale)))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        pos = pygame.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouseget_pressed()[0] == 1:
                print("Start")
        screen.blit(self.image, (self.rect.x, self.rect.y))


# create start button
# start_button = Button(300, 200, startImg, 0.5)
# exit_button = Button(450, 200, exitImg, 0.5)

# start_button.draw()
# exit_button.draw()

running = True
while running:
    screen.blit(background_img, (0, 0))
    start_button = Button(300, 200, startImg, 0.5)
    exit_button = Button(450, 200, exitImg, 0.5)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
