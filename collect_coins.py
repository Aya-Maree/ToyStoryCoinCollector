
import random
from tkinter import font
import pygame, time
pygame.init()
pygame.mixer.init()



#initializing the background image
bg_image = pygame.image.load('background.jpg') #loading the image
bg_rect = bg_image.get_rect()
screen = pygame.display.set_mode((bg_rect.width,bg_rect.height)) #initializes the window itself, it returns a surface object that represents the main screen   
screen_rect = screen.get_rect()

#initializng the coin image
coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
# Calculate the x-position of the image
coin_rect.x = (screen_width - coin_image.get_width()) / 2 #the x position of the coin image will be equal to the wdith of the screen minus the width of the coin image divided by 2
coin_rect.y = 0  #the y position of the coin image will be 0 to make it stay at the top of the screen

#initializng the bank (buzz) image
bank_image = pygame.image.load("bank.png")
bank_rect = bank_image.get_rect()
bank_rect.x = (screen_width - coin_image.get_width()) / 2
screen_height = screen_info.current_h
bank_rect.y  = screen_height-(bank_image.get_height()) #this will place the bank image at the bottom of the screen

#this is extra, just playing around with pygame
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1) 
font = pygame.font.Font('Font.ttf', 36)
msg = font.render("New level activated!", True, (255, 255, 255)) # create a surface object with the message
msg_rect = msg.get_rect() # get the rectangle that encloses the surface
msg_rect.center = screen_rect.center # center the message on the screen
text_surf = None

#created a render function so i don't have to reoeat the same code in the game loop
def render():  
   screen.blit(bg_image,bg_rect) #order of blitting matters, bg first then coin
   screen.blit(coin_image,(coin_rect.x, coin_rect.y)) #this will draw the image on the screen
   screen.blit(bank_image,(bank_rect.x,bank_rect.y))
   if text_surf is not None:
        screen.blit(text_surf, (10, 10))
   pygame.display.flip()
render()

coin_count = 0
coin_speed = 1
bank_speed = 100
remaining_count = 10

#game loop 
running = True
while running:
#event loop
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
            bank_rect.x = max(bank_rect.x - bank_speed, 0) #so the bank doesnt leave the bounds
         elif event.key == pygame.K_RIGHT:
            bank_rect.x = min(bank_rect.x + bank_speed, screen_width - bank_rect.width)

    # Update the position of the coin
   coin_rect.y += coin_speed
   if coin_rect.bottom >= screen_rect.bottom:
        # Set the y-position of the coin to the top of the screen
        coin_rect.y = 0
        # Set the x-position of the coin to a random value between 100 and 900
        coin_rect.x = random.randint(100, 900)

   if bank_rect.colliderect(coin_rect):
      coin_count +=1 #increment the coin count
      remaining_count -= 1#deincrement the coin count
      coin_rect.y=0
      coin_rect.x=random.randint(100, 900)
      text_surf = font.render("Coins: {}".format(coin_count), True, (255, 255, 255)) #displays current coin count
      print("new coin count: ",coin_count)
   if remaining_count == 0:
       coin_speed*=2
       print("new level activated")
       remaining_count = 10
       screen.blit(msg, msg_rect) # blit the message onto the screen
       pygame.display.flip() # update the screen
       time.sleep(2) # wait for 1 second
   #render
   render()       
pygame.quit()
         
            