import pygame
pygame.init()
import random
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,255)
screen_width=800
screen_hight=500
food_x=random.randint(20,screen_width/2)
food_y=random.randint(20,screen_hight/2)
mountain1_x=random.randint(20,screen_width/2)
mountain1_y=random.randint(20,screen_hight/2)
mountain2_x=random.randint(20,screen_width/2)
mountain2_y=random.randint(20,screen_hight/2)
mountain3_x=random.randint(20,screen_width/2)
mountain3_y=random.randint(20,screen_hight/2)

score=0
init_velocity=10
gameWindow=pygame.display.set_mode((screen_width,screen_hight))
pygame.display.set_caption("Reet Game")
pygame.display.update()
exit_game=False
game_over=False     
snake_x=45
snake_y=45
snake_size=10
fps=30
clock=pygame.time.Clock()
velocity_x=0
velocity_y=0

# font=pygame.font.Sysfont(none,55)
# def text_screen(text,color,x,y):
     # screen_text(font.render(text,True,color)
     # gameWindow.blit(screen_text, [x,y])


while not exit_game: 
     for event in pygame.event.get():
          print(event)
          if event.type==pygame.QUIT:
               print(event)
               exit_game=True
          
          if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_RIGHT:
                    velocity_x=init_velocity
                    velocity_y=0                
               if event.key==pygame.K_LEFT:
                    velocity_x=-init_velocity
                    velocity_y=0                
               if event.key==pygame.K_UP:
                    velocity_y= -init_velocity
                    velocity_x=0                

               if event.key==pygame.K_DOWN:
                    velocity_y=init_velocity
                    velocity_x=0                        

     if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8 :
          score=score+1
          print("score=",score)
           
          food_x=random.randint(20,screen_width)
          food_y=random.randint(20,screen_hight)

     gameWindow.fill(white)     
     # text_screen("score:"+str(score+10),red,5,5)
     pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
     # pygame.draw.circle(gameWindow,blue,[mountain1_x,mountain1_y,5,5,5])
     # pygame.draw.circle(gameWindow,blue,[mountain2_x,mountain2_y,snake_size+2,snake_size+2])
     # # pygame.draw.circle(gameWindow,blue,[mountain3_x,mountain3_y,snake_size+2,snake_size+2])

     pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
     pygame.display.update()
     clock.tick(fps)

     snake_x+=velocity_x
     snake_y+=velocity_y




pygame.quit()
quit()          
     