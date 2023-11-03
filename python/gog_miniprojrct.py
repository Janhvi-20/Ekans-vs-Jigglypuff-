import pygame,sys,random
from pygame.math import Vector2
from pygame.locals import *
from pygame import mixer

class Snake:
    def __init__(self):
        self.body=[Vector2(5,10), Vector2(6,10),Vector2(7,10)]
        self.direction=Vector2(-1,0)

        #head position of the snake 
        self.HEAD_UP=pygame.image.load('Snake_body/HEAD_UP.png')
        self.HEAD_DOWN=pygame.image.load('Snake_body/HEAD_DOWN.png')
        self.HEAD_LEFT=pygame.image.load('Snake_body/HEAD_LEFT.png')
        self.HEAD_RIGHT=pygame.image.load('Snake_body/HEAD_RIGHT.png')

        #tail position of the snake 
        self.tail_up=pygame.image.load('Snake_body/tail_up.png')
        self.tail_down=pygame.image.load('Snake_body/tail_down.png')
        self.tail_LEFT=pygame.image.load('Snake_body/tail_LEFT.png')
        self.tail_RIGHT=pygame.image.load('Snake_body/tail_RIGHT.png')

        #snake turning body
        self.turn_up=pygame.image.load('Snake_body/turn_up.png')
        self.turn_down=pygame.image.load('Snake_body/turn_down.png')
        self.turn_left=pygame.image.load('Snake_body/turn_left.png')
        self.turn_right=pygame.image.load('Snake_body/turn_right.png')

        #body of the snake 
        self.VER=pygame.image.load('Snake_body/snake body ver.png')
        self.HORI=pygame.image.load('Snake_body/snake body hori.png')


    def draw_snake(self):
        self.update_head()
        self.update_tail()
        for index,block in enumerate(self.body):
            block_rect=pygame.Rect(int(block.x*cell_size),int(block.y*cell_size), cell_size, cell_size)
            
            #drawing the snake with graphics
            if index == 0:
                screen.blit(self.head,block_rect)
            elif index ==len(self.body)-1:
                screen.blit(self.tail,block_rect)
            
            else:
                previous= self.body[index+1] - block
                next_block=self.body[index - 1] - block

                if previous.x==next_block.x:
                    screen.blit(self.VER,block_rect)

                elif previous.y==next_block.y:
                    screen.blit(self.HORI,block_rect)
                
                else:
                    if previous.x==-1 and next_block.y==-1 or previous.y==-1 and next_block.x == -1:
                      screen.blit(self.turn_up,block_rect)
                    elif previous.x==-1 and next_block.y==1 or previous.y==1 and next_block.x == -1:
                      screen.blit(self.turn_left,block_rect)
                    elif previous.x==1 and next_block.y==-1 or previous.y==-1 and next_block.x == 1:
                      screen.blit(self.turn_right,block_rect)
                    elif previous.x==1 and next_block.y==1 or previous.y==1 and next_block.x == 1:
                      screen.blit(self.turn_down,block_rect)

    def update_head (self):
        relate = self.body[1] - self.body[0]
        
        if Vector2(-1,0) == relate: self.head=self.HEAD_RIGHT
        elif Vector2(1,0) == relate: self.head=self.HEAD_LEFT
        elif Vector2(0,1) == relate: self.head=self.HEAD_UP
        elif Vector2(0,-1) == relate: self.head=self.HEAD_DOWN

    def update_tail (self):
        relate = self.body[-2] - self.body[-1]
        
        if Vector2(-1,0) == relate: self.tail=self.tail_LEFT
        elif Vector2(1,0) == relate: self.tail=self.tail_RIGHT
        elif Vector2(0,1) == relate: self.tail=self.tail_down
        elif Vector2(0,-1) == relate: self.tail=self.tail_up
 
    def movement(self):
        bodycopy=self.body[:-1]
        bodycopy.insert(0,bodycopy[0]+self.direction)
        self.body=bodycopy[:]

class Fruit:
    #creating a class for fruit and a vector 
    def __init__(self):
        self.x=random.randint(0,cell_number-2)
        self.y=random.randint(0,cell_number-2)
        self.pos=Vector2(self.x,self.y)

    def draw_fruit(self):
       fruit_rect=pygame.Rect(int(self.pos.x*cell_size), int(self.pos.y*cell_size), cell_size, cell_size)
       #pygame.draw.rect(screen,(250,0,0),fruit_rect)
       screen.blit(image,fruit_rect)
               
class MAIN:
    SCORE=0
    def __init__(self):
        self.snake=Snake()
        self.fruit = Fruit()
    
    def update(self):
        
        self.collision()
        self.snake.movement()
        self.game_fail()
        self.score()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.score()
    
    def collision (self):
        if self.fruit.pos == self.snake.body[0]:
            munch=mixer.Sound('snake_hiss.mp3')
            munch.play()
            self.SCORE = self.SCORE+1
            self.fruit.__init__()
            self.snake.body.insert(-1,self.fruit.pos)


    def score(self):
        score_surface=text.render("Score:-"+str(self.SCORE),True,(0,200,220))
        screen.blit(score_surface,(5,10))



    def game_fail(self):
        if not 0<=self.snake.body[0].x <=cell_number or not 0<=self.snake.body[0].y <=cell_number:
            pygame.quit()
            sys.exit()
        for c in self.snake.body[1:]:
            if c==self.snake.body[0]:
                pygame.quit()
                sys.exit()

     
pygame.init()
mixer.init()
#start page ...................................................................
mixer.music.load('pokemon theme song.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)
screen2 = pygame.display.set_mode((800,800))
img = pygame.image.load('intropage.jpeg')

clock=pygame.time.Clock()
text=pygame.font.Font('Pokemon Solid.ttf',70)
#score_s=text.render("Jiggly puff  VS  Ekans",True,(225,0,0))
game=True
while game:
    screen2.blit(img,(0,0))
    #screen2.blit(score_s,(15,200))
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #to check the exit of the game 
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                game=False
    
    pygame.display.update() #update of the screen 
    clock.tick(80)

#/........................//////............................/////................

#the game music that is running in the game 

if game==False:
    mixer.music.load('background.mp3')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)
#..................................................................................
# game heading and icon of the game 
pygame.display.set_caption(title="EKANS VS JIGGLYPUFF")
Icon=pygame.image.load("pink snake.jpg")
pygame.display.set_icon(Icon)

#..................................................................................

back=pygame.image.load('bushes.png')
image=pygame.image.load('jigglypuff.png')

cell_size=40
cell_number=20
screen=pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
clock=pygame.time.Clock()

text=pygame.font.Font('brodies.ttf',18)
main_game=MAIN()

def highestscore(self):
    with open ('highscore.txt','r') as f:
        return f.read
    
try:
    high_s=int(highestscore())
except:
    high_s=0

game_paused= False
#screen update speed that is how fast the snake refreshes itself
SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


#.....................................................................................
#......................................................................................
game= False
while game!=True:
        screen.blit(back,dest=(0,0))

        for event in pygame.event.get():

          if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == SCREEN_UPDATE:
             main_game.update()
          if event.type == pygame.KEYDOWN:

            if event.key == K_UP and main_game.snake.direction.y!=1 :
                 main_game.snake.direction =Vector2(0,-1)
            
            if event.key ==K_LEFT and main_game.snake.direction.x!=1 :
                main_game.snake.direction = Vector2(-1,0)
            
            if event.key==K_DOWN and main_game.snake.direction.y!=-1:
                main_game.snake.direction =Vector2(0,1)
            
            if event.key==K_RIGHT and main_game.snake.direction.x!= -1:
                main_game.snake.direction= Vector2(1,0)

        if high_s < main_game.SCORE:
            high_s = main_game.SCORE
        with open('highscore.txt','w') as f:
            f.write(str(high_s))
        score_surface=text.render("HighScore:-"+str(high_s),True,(0,200,220))
        screen.blit(score_surface,(600,10))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60) 
