import pgzrun
import os
import pygame

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 1280
HEIGHT = 720
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("QuizIt! game")

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 15

q1 = ["Who is the father of computers?",
      "Charles Babbage", "Henry Ford", "Nikola Tesla", "Adolf Hitler", 1]

q2 = ["What was the first commerical video game?",
      "Pong", "Space Invaders", "Donkey Kong", "Pac-Man", 1]

q3 = ["What was the first computer mouse made of?",
            "Wood", "Metal", "Plastic", "Rubber", 1]

q4 = ["What does the acronym ROM stand for?",
            "Random Operating Memory", "Read-Only Memory", "Rapid Operation Mode", "Real-time Operation Module", 2]

q5 = ["What does the acronym CPU stand for?",
            "Central Processing Unit", "Control Processing Unit", "Computer Processing Unit", "Critical Processing Unit", 1]

q6 = ["What was the first personal computer?",
            "IBM PC", "Apple II", "Commodore PET", "Altair 8800", 4]

q7 = ["What was the first video game console?",
            "Magnavox Odyssey", "Atari 2600", "ColecoVision", "Nintendo Entertainment System", 1]

q8 = ["What was the first graphical web browser?",
            "Mosaic", "Internet Explorer", "Netscape Navigator", "Opera", 1]

q9 = ["What was the first email sent?",
            "Hello, World!", "What hath God wrought?", "Merry Christmas", "QWERTYUIOP", 2]

q10 = ["What was the first search engine?",
              "Archie", "Google", "Yahoo!", "Bing", 1]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9 ,q10]

question = questions.pop(0)

#assets
bg = pygame.image.load('School BG 1.png')
bg = pygame.transform.scale(bg, (1280, 720))



def draw(): 
    
    screen.blit(bg, (0, 0))
    screen.draw.filled_rect(main_box, "coral")
    screen.draw.filled_rect(timer_box, "coral")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "yellow")
        screen.draw.textbox(str(time_left), timer_box, color=("black"))
        screen.draw.textbox(question[0], main_box, color=("black"))

        index = 1
        for box in answer_boxes:
            screen.draw.textbox(question[index], box, color=("black"))
            index = index + 1


#GAME OVER
def game_over():
    global question, time_left
    message = "Game over, Thank You for playing! You got %s questions correct!" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

#CORRECT ANSWER 
def correct_answer():
    global question, score, time_left

    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 15
    else:
        print("End of questions")
        game_over()

#COLLIDE POINT ON SCREEN
def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("Good Job! You got that right!")
                correct_answer()
            else:
                game_over()
        index = index + 1

#UPDATES TIME LEFT
def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)


pgzrun.go()
