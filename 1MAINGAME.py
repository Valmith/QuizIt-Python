import pgzrun
import os
import pygame, sys
import tkinter.messagebox
from button import Button
from random import shuffle

#Centers the window 
os.environ['SDL_VIDEO_CENTERED'] = '1'

#dimensions of the window
WIDTH = 1280
HEIGHT = 720

#initializes the pygame framework
pygame.init()

#initialize dimensions
gamescreen = pygame.display.set_mode((WIDTH, HEIGHT)) 

#PLAYS MUSIC
pygame.mixer.init()
pygame.mixer.music.load('8bitwinner.mp3')
# -1 means background music
pygame.mixer.music.play(-1)

#Sets tab header label
pygame.display.set_caption("QuizIt! game")


#Spawns the rectangles needed for the main game
main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

#Moves rectangles to it's places
main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

#Placed in string for use later
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

#initialize the score and the initial timer
score = 0
time_left = 20

#initialize the clock
clock = pygame.time.Clock()

#Updates the timer everytime user does any shit
UPDATE_TIME_EVENT = pygame.USEREVENT + 1


#Initialize the questions
q1 = ["Who is the father of computers?",
      "Charles Babbage", "Henry Ford", "Nikola Tesla", "Adolf Hitler", 1]

q2 = ["What was the first commerical video game?",
      "Pong", "Space Invaders", "Donkey Kong", "Pac-Man", 1]

q3 = ["What was the first computer mouse made of?",
            "Metal", "Wood", "Plastic", "Rubber", 2]

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

#removes the question displayed 
question = questions.pop(0)

#shuffles the questions
shuffle(questions)

#assets
bg = pygame.image.load('School BG 1.png')
bg = pygame.transform.scale(bg, (1280, 720))
character_jam = pygame.image.load('JAM.png')
character_jam = pygame.transform.scale (character_jam, (250, 350))
character_nico = pygame.image.load('NICO.png')
character_nico = pygame.transform.scale (character_nico, (250, 350))
logo = pygame.image.load('QuizIT.png')
logo = pygame.transform.scale (logo, (550, 300))
cont_button = pygame.image.load('Continue.png')
cont_button = pygame.transform.scale (cont_button, (360, 130))
start_button = pygame.image.load('Start Game.png')
start_button = pygame.transform.scale (start_button, (360, 130))
credits_button = pygame.image.load('Credits.png')
credits_button = pygame.transform.scale (credits_button, (360, 130))
helpbg = pygame.image.load("helpbg.png")
helpbg = pygame.transform.scale(helpbg, (1280, 720))
helpboxr =pygame.image.load("helpboxr.png")
helpboxr = pygame.transform.scale(helpboxr, (950, 480))
settings = pygame.image.load('settings.png')
settings = pygame.transform.scale (settings, (40, 40))
info = pygame.image.load('info.png')
info = pygame.transform.scale (info, (40, 40))
name = pygame.image.load('name.png')
name = pygame.transform.scale (name, (300, 15))
boxr= pygame.image.load("boxr.png")
boxr = pygame.transform.scale (boxr, (360, 120))
mainbox=pygame.image.load("mainbox.png")
timerbox=pygame.image.load("timerbox.png")
answerbox = pygame.image.load("answerbox.png")

#this imports the font i stole online
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


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
            print("Clicked on answer " + str(index)) # prints to console what box you clicked on
            if index == question[5]:
                tkinter.messagebox.showinfo("Correct Answer", "Good Job! You got that right!")
                print("Good Job! You got that right!") # prints to console you got it right
                correct_answer()
            else:
                skip_question()
        index = index + 1


#HERE STARTS WHILE TRUE LOOPS
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

        #sets font for above as well as color
        options_text = [get_font(25).render(text, True, "Black") for text in options]
        options_rect = [text.get_rect(center=(640, 100 + index * 100)) for index, text in enumerate(options_text)]

        for text, rect in zip(options_text, options_rect):
            screen.blit(text, rect)

        #bakc button
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

#draws the first screen to appear
def draw(): 

    #quizgame()
    main_menu()


def main_menu():
    pygame.display.set_caption("Main Menu")

    
    while True:
        screen.blit(bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=boxr, pos=(640, 250), 
                            text_input="START", font=get_font(35), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=boxr, pos=(640, 400), 
                            text_input="HELP", font=get_font(35), base_color="#d7fcd4", hovering_color="Orange")
        QUIT_BUTTON = Button(image=boxr, pos=(640, 550), 
                            text_input="QUIT", font=get_font(35), base_color="#d7fcd4", hovering_color="Red")
        
        screen.blit(name,(470, 620)) 
        screen.blit(character_jam, (100, 300))
        screen.blit(character_nico, (950, 300))
        screen.blit(logo, (375, -30))

        #change button color
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    quizgame()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

#MAIN GAME LOOP
#EXTRA COMMENT FOR EPIC PURPOSES
def quizgame():
    pygame.time.set_timer(UPDATE_TIME_EVENT, 1000)

    while True:
        
        global score, game_over, correct_answer, skip_question, on_key_up, question, index, time_left, update_time_left, clock
        
        #CLOSES GAME IF YOU PRESS X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == UPDATE_TIME_EVENT:
                update_time_left()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                on_mouse_down(pos)

            if event.type == pygame.KEYUP:
                on_key_up(event.key)
    
        #DRAWS THE BOARD
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

        clock.tick(60)

        pygame.display.update()



#GAME OVER FUNCTION
def game_over():
    
    global question, time_left
    message = "Game over, Thank You for playing! You got %s questions correct!" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

#HERE IS THE EDIT FILE EPIC
#HERE IS THE EDIT FILE EPIC
#HERE IS THE EDIT FILE EPIC
#HERE IS THE EDIT FILE EPIC
#HERE IS THE EDIT FILE EPIC
#HERE IS THE EDIT FILE EPIC
#HERE IS THE EDIT FILE EPIC
#HERE IS THE EDIT FILE EPIC
#HERE IS THE EDIT FILE EPIC
#HERE IS THE EDIT FILE EPIC
#CADEEZ NUTS
#CADEEZ NUTS
#CADEEZ NUTS
#CADEEZ NUTS
#CADEEZ NUTS
#CADEEZ NUTS
#CADEEZ NUTS


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

#COUNTDOWN
def update_time_left():
    print("IT IS RUNNING THE TIMER OWO")

    global time_left, question

    if time_left:
        time_left = time_left - 1
        
    else:
        #If timer reaches 0, end game
        pygame.time.set_timer(UPDATE_TIME_EVENT, 0)

        skip_question()

        print("IT IS RUNNING THE TIMER again")


pgzrun.go()
