import pygame
from button import Button

pygame.init()
screen = pygame.display.set_mode((1280, 720))

pygame.mixer.init()
pygame.mixer.music.load('8bitwin.mp3')

# Define the button rect and label
button_rect = pygame.Rect(600, 350, 100, 50)
button_label = "Play"


def toggle_music():
    global button_label
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        button_label = "Play"
    else:
        pygame.mixer.music.play(-1)
        button_label = "Stop"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                toggle_music()

    # Draw the button and label
    pygame.draw.rect(screen, (255, 255, 255), button_rect)
    font = pygame.font.Font(None, 32)
    text = font.render(button_label, True, (0, 0, 0))
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

    pygame.display.flip()
