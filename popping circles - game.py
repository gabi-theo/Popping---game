import pygame
import random
import time
import pyautogui

#initializing the game screen and needed variables
pygame.init()
window_width = 1300
window_height = 750
window = pygame.display.set_mode((window_width,window_height))
puncte = 0
timp = 0
display = True
radius = 50

#the file where the scores will be stored
file = open('scores.txt','a')

#class for creating a circle
class Circle():
    def __init__(self,culoare, x ,y ,raza):
        self.culoare = culoare
        self.x = x
        self.y = y
        self.raza = raza
        self.vel = 5

    #method for the circles moving around
    def move(self):
        self.velx = random.randint(-30,30)
        self.vely = random.randint(-30,30)
        self.x += self.velx
        self.y += self.vely
        time.sleep(0.001)

        #conditions for not living the screen
        if self.x > window_width:
            self.x = window_width - self.raza
        if self.x < 0:
            self.x = self.x+self.raza
        if self.y > window_height:
            self.y = window_height - self.raza
        if self.y < 0:
            self.y = self.y + self.raza

    #method for having the actuall position updated
    #helpfull when circles collide with the rectangle
    def position(self):
        self.x = self.x
        self.y = self.y
        return self.x, self.y, self.raza

    #method for drawing the objects on the screen
    def draw(self,window):
        pygame.draw.circle(window,self.culoare,(self.x,self.y),self.raza)
        pygame.display.update()
        
#class for creating the rectangle
class Rectangle():
    def __init__(self,culoare, x ,y ,width, height):
        self.culoare = culoare
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    #method for having the actuall position updated
    #helpfull when circles collide with the circle
    def position(self):
        self.x = self.x
        self.y = self.y
        
        return self.x, self.y
    
    #method for drawing the objects on the screen    
    def draw(self,window):
        pygame.draw.rect(window,self.culoare,(self.x,self.y, self.width, self.height))
        pygame.display.update()

    
        

run = True
#some lists for getting random values for positions and colors of the objects
x = []
y = []
r = []
g = []
b = []

#filling lists with random numbers
for i in range(11):
    x.append(random.randint(30,window_width - radius))
    y.append(random.randint(30,window_height + radius))
    r.append(random.randint(50,255))
    g.append(random.randint(50,255))
    b.append(random.randint(50,255))


#creating the objects
cerc0 = Circle((255,0,0),x[0],y[0],radius)
cerc1 = Circle((r[1],g[1],b[1]),x[1],y[1],radius)
cerc2 = Circle((r[2],g[2],b[2]),x[2],y[2],radius)
cerc3 = Circle((r[3],g[3],b[3]),x[3],y[3],radius)
cerc4 = Circle((r[4],g[4],b[4]),x[4],y[4],radius)
cerc5 = Circle((r[5],g[5],b[5]),x[5],y[5],radius)
cerc6 = Circle((r[6],g[6],b[6]),x[6],y[6],radius)
cerc7 = Circle((r[7],g[7],b[7]),x[7],y[7],radius)
cerc8 = Circle((r[8],g[8],b[8]),x[8],y[8],radius)
cerc9 = Circle((r[9],g[9],b[9]),x[9],y[9],radius)

patrat = Rectangle((r[0],g[0],b[0]),x[0],y[0],30,30)

#variables that will delete our objects when will be the case
cerc0_draw = True
cerc1_draw = True
cerc2_draw = True
cerc3_draw = True
cerc4_draw = True
cerc5_draw = True
cerc6_draw = True
cerc7_draw = True
cerc8_draw = True
cerc9_draw = True

#function that will display the time of the game
def display_time():
    global timp
    font = pygame.font.Font('freesansbold.ttf', 12)
    text = font.render('Timp: '+str(timp), True, (0,255,0))
    textRect = text.get_rect()
    textRect.center = (50, 50)
    window.blit(text, textRect)
    timp+=1
    return timp

#variable that will tell us when is the game done     
over = False

#you can put your own name before you start the game. Just uncomment the next line and comment out the one with "test"
#name = input('Please enter your name')
name = 'test'
time.sleep(1)
while not over:
    #getting the mouse coordinates so we can move the rectangle after the mouse
    mouse = pygame.mouse.get_pos()
    patrat = Rectangle((r[10],g[10],b[10]),mouse[0],mouse[1],30,30)
    pygame.time.delay(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #if we did not touch the circles with our mouse the circles will be on the screen
    xp = patrat.position()
    if cerc0_draw == True:
        cerc0.draw(window)
        cerc0.move()
        c0 = cerc0.position()
        
    if cerc1_draw == True:
        cerc1.draw(window)
        cerc1.move()
        c1 = cerc1.position()
        
    if cerc2_draw == True:
        cerc2.draw(window)
        cerc2.move()
        c2 = cerc2.position()
        
    if cerc3_draw == True:
        cerc3.draw(window)
        cerc3.move()
        c3 = cerc3.position()
        
    if cerc4_draw == True:
        cerc4.draw(window)
        cerc4.move()
        c4 = cerc4.position()
        
    if cerc5_draw == True:
        cerc5.draw(window)
        cerc5.move()
        c5 = cerc5.position()
        
    if cerc6_draw == True:
        cerc6.draw(window)
        cerc6.move()
        c6 = cerc6.position()
        
    if cerc7_draw == True:
        cerc7.draw(window)
        cerc7.move()
        c7 = cerc7.position()
        
    if cerc8_draw == True:
        cerc8.draw(window)
        cerc8.move()
        c8 = cerc8.position()
        
    if cerc9_draw == True:
        cerc9.draw(window)
        cerc9.move()
        c9 = cerc9.position()
        
    patrat.draw(window)    

    #if we touch any circle, the object will be deleted and we will not display it anymore
    try:
        if c0[0]+ c0[2] > xp[0] and xp[0]> c0[0]- c0[2] and c0[1] + c0[2]>xp[1] and c0[1] - c0[2]<xp[1]:
            cerc0_draw = False
            del cerc0
            puncte +=1

            
        if c1[0]+ c1[2] > xp[0] and xp[0]> c1[0]- c1[2] and c1[1] + c1[2]>xp[1] and c1[1] - c1[2]<xp[1]:
            cerc1_draw = False
            del cerc1
            puncte +=1
            
        if c2[0]+ c2[2] > xp[0] and xp[0]> c2[0]- c2[2] and c2[1] + c2[2]>xp[1] and c2[1] - c2[2]<xp[1]:
            cerc2_draw = False
            del cerc2
            puncte +=1
            
        if c3[0]+ c3[2] > xp[0] and xp[0]> c3[0]- c3[2] and c3[1] + c3[2]>xp[1] and c3[1] - c3[2]<xp[1]:
            cerc3_draw = False
            del cerc3
            puncte +=1
            
        if c4[0]+ c4[2] > xp[0] and xp[0]> c4[0]- c4[2] and c4[1] + c4[2]>xp[1] and c4[1] - c4[2]<xp[1]:
            cerc4_draw = False
            del cerc4
            puncte +=1
            
        if c5[0]+ c5[2] > xp[0] and xp[0]> c5[0]- c5[2] and c5[1] + c5[2]>xp[1] and c5[1] - c5[2]<xp[1]:
            cerc5_draw = False
            del cerc5
            puncte +=1
            
        if c6[0]+ c6[2] > xp[0] and xp[0]> c6[0]- c6[2] and c6[1] + c6[2]>xp[1] and c6[1] - c6[2]<xp[1]:
            cerc6_draw = False
            del cerc6
            puncte +=1
            
        if c7[0]+ c7[2] > xp[0] and xp[0]> c7[0]- c7[2] and c7[1] + c7[2]>xp[1] and c7[1] - c7[2]<xp[1]:
            cerc7_draw = False
            del cerc7
            puncte +=1
            
        if c8[0]+ c8[2] > xp[0] and xp[0]> c8[0]- c8[2] and c8[1] + c8[2]>xp[1] and c8[1] - c8[2]<xp[1]:
            cerc8_draw = False
            del cerc8
            puncte +=1
            
        if c9[0]+ c9[2] > xp[0] and xp[0]> c9[0]- c9[2] and c9[1] + c9[2]>xp[1] and c9[1] - c9[2]<xp[1]:
            cerc9_draw = False
            del cerc9
            puncte +=1

    except NameError:
        pass
        
    window.fill((0,0,0))
    #we will display the time as long as we have 10 objects on the screen
    if display == True:
        display_time()

    if puncte > 9:
        display = False
        over = True
#when the game is over, we will store the score in our "score list"
final_time = display_time()
oldScore = []
file.write('\n'+name+' '+str(final_time))
file.close()


pygame.quit()
