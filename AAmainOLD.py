import pgzrun
import os
import pygame, sys
import tkinter.messagebox
from button import Button


os.environ['SDL_VIDEO_CENTERED'] = '1'
WIDTH = 1280
HEIGHT = 720

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Main Menu")

pygame.mixer.init()
pygame.mixer.music.load('8bitwinner.mp3')
pygame.mixer.music.play(-1)

# gamescreen = pygame.display.set_mode((WIDTH, HEIGHT)) 

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
time_left = 20

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

#ASSETS
bg = pygame.image.load("School BG 1.png")
bg = pygame.transform.scale(bg, (1280, 720))
Schoolbg = pygame.image.load("School BG 1.png")
Schoolbg = pygame.transform.scale(Schoolbg, (1280, 720))
Schoolbg1 = pygame.image.load("School BG 1.png")
Schoolbg1 = pygame.transform.scale(Schoolbg1, (1280, 720))
helpbg = pygame.image.load("helpbg.png")
helpbg = pygame.transform.scale(helpbg, (1280, 720))
helpboxr =pygame.image.load("helpboxr.png")
helpboxr = pygame.transform.scale(helpboxr, (950, 480))
name = pygame.image.load("name.png")
character_jam = pygame.image.load('JAM.png')
character_jam = pygame.transform.scale (character_jam, (250, 350))
character_nico = pygame.image.load('NICO.png')
character_nico = pygame.transform.scale (character_nico, (250, 350))
logo = pygame.image.load('QuizIT.png')
logo = pygame.transform.scale (logo, (500, 260))
boxr= pygame.image.load("boxr.png")
boxr = pygame.transform.scale (boxr, (360, 120))
mainbox=pygame.image.load("mainbox.png")
timerbox=pygame.image.load("timerbox.png")
answerbox = pygame.image.load("answerbox.png")

# selectjam = pygame.image.load("JAM CHAR.png")
# selectnico = pygame.image.load("NCO CHAR.png")

#GET THE FONT
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

#QUIZ GAME
def play():
    pygame.display.set_caption("Quiz Game")

    while True:
        global question, score, answer_boxes

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SETS POSITIONS OF ASSESTS FOR GAME
        screen.blit(Schoolbg1, (0, 0))
        screen.blit(mainbox, (30, 37))
        screen.blit(timerbox, (960, 37))
        
        # for  box in answer_boxes:
        #     screen.draw.filled_rect(box, "yellow")
        #     screen.draw.textbox(str(time_left), timer_box, color=("black"))
        #     screen.draw.textbox(question[0], main_box, color=("black"))

        # index = 1
        # for box in answer_boxes:
        #     screen.draw.textbox(question[index], box, color=("black"))
        #     index = index + 1

        




        #Code for button to go back
        PLAY_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Blue")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()



def options():
    while True:
        pygame.display.set_caption("Options Menu")
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(helpboxr, (150,0))


        options = [
            "WELCOME TO QUIZIT!",
            "Select your answer from 4 options!",
            "Press H for a Hint!",
            "Press SPACE to skip a question!"
        ]

        options_text = [get_font(25).render(text, True, "Black") for text in options]
        options_rect = [text.get_rect(center=(640, 100 + index * 100)) for index, text in enumerate(options_text)]

        for text, rect in zip(options_text, options_rect):
            screen.blit(text, rect)

        OPTIONS_BACK = Button(image=pygame.image.load("boxr.png"), pos=(640, 550), 
                            text_input="BACK", font=get_font(60), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    pygame.display.set_caption("Main Menu")
    while True:
        screen.blit(Schoolbg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        # MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=boxr, pos=(640, 250), 
                            text_input="START", font=get_font(35), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=boxr, pos=(640, 400), 
                            text_input="HELP", font=get_font(35), base_color="#d7fcd4", hovering_color="Orange")
        QUIT_BUTTON = Button(image=boxr, pos=(640, 550), 
                            text_input="QUIT", font=get_font(35), base_color="#d7fcd4", hovering_color="Red")
        
        screen.blit(name,(470, 620)) 
        screen.blit(character_jam, (100, 300))
        screen.blit(character_nico, (950, 300))
        screen.blit(logo, (400, 0))

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

    
#GAME OVER FUNCTION
def game_over():
    
    global question, time_left
    message = "Game over, Thank You for playing! You got %s questions correct!" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

#CORRECT ANSWER FUNCTION
def correct_answer():
    global question, score, time_left

    score = score + 1

    if questions:
        question = questions.pop(0)
        time_left = 20
    else:
        
        game_over()
    



#SKIP A QUESTION
def skip_question():
    global question, score, time_left
    score -= 0 # keeps score the same 
    tkinter.messagebox.showerror("Wrong Answer", "You got that wrong! Good luck on the next one!")
    print("Wrong Answer! Goodluck on the next one!")
    if questions: 
        question = questions.pop(0) # get the next question
        time_left = 20
    else: # if there are no more questions
        game_over()



#HINT AND SKIP FUNCTION
def on_key_up(key):
    global score
    if key == keys.H:
        tkinter.messagebox.showinfo("Hint!", "The correct answer is %s" % question[5])
        print("The correct answer is %s" % question[5])
    if key == keys.SPACE:
        score = score - 1
        tkinter.messagebox.askyesno("Skip", "Would you like to skip this question?")
        print("Skipped question! The correct answer is %s" % question[5])
        correct_answer()



#COLLISION POINT FUNCTION FOR QUESTIONS
def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))#prints to console what box you clicked on
            if index == question[5]:
                tkinter.messagebox.showinfo("Correct Answer", "Good Job! You got that right!")
                print("Good Job! You got that right!")#prints to console you got it right
                correct_answer()
            else:
                skip_question()
        index = index + 1



#COUNTOWN UPDATE
def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)


main_menu()

pgzrun.go()
