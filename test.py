import pygame
import sys


pygame.display.init()
width = 300
height = 350
bg = (255, 255, 255)

screen = pygame.display.set_mode((width, height))
screen.fill(bg)


class Button:

    def __init__(self, rect_x, rect_y, rect_width, rect_height):
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.rect_width = rect_width
        self.rect_height = rect_height

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.rect_x, self.rect_y, self.rect_width, self.rect_height))


button1 = Button(10, 10, 100, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    button1.draw()       
    pygame.display.update()