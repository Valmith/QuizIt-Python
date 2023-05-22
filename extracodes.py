# #START SCREEN
# def startscreen():

#     screen.blit(bg, (0, 0))
#     screen.blit(character_jam, (100, 300))
#     screen.blit(character_nico, (950, 300))
#     screen.blit(logo, (470, 50))
#     screen.blit(cont_button, (460, 200))
    
#     screen.blit(start_button, (460, 300))
    
#     screen.blit(credits_button, (460, 400))
#     screen.blit(settings, (70,660))
#     screen.blit(info, (150, 660))
#     screen.blit(name, (490, 550))



# def update_time_left():
#     global time_left
#     print('FIRST THINGY IS RUNNING')

#     # decrement time_left by 1
#     time_left -= 1

#     # update timer box with new time left
#     timer_text = f"Time Left: {time_left}"
#     screen.draw.textbox(timer_text, timer_box, color="black")

#     # check if time_left has reached 0
#     if time_left <= 0:
#         # stop timer
#         pygame.time.set_timer(pygame.USEREVENT, 0)
#         # call game_over function
#         game_over()  
  




