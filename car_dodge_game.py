import pygame
import time
import random

#initiate PyGame to run commands
pygame.init()

display_width = 800
display_height = 600

#sets the surface or canvas of the game as 800x600. 
gameDisplay = pygame.display.set_mode((display_width,display_height))

#Sets the display's caption
pygame.display.set_caption('KXSW')

black = (0,0,0)
white = (255,255,255)
red = (180,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)

car_width = 73

#displays clock
clock = pygame.time.Clock()

#uses image called racecar.png
carImg = pygame.image.load('racecar.png')

#Text displaying function that shows many object we have dodged in the top left of the screen
def blocks_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: " +str(count), True, black)
	gameDisplay.blit(text,(0,0))

#function that takes x and y starting points, width and height variables, and a color
#use pygame.draw.rect() to draw a polygon to our specs inside the game_loop() function
def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

#define the car function. "Blit" just draws the image to the screen
def car(x,y):
	gameDisplay.blit(carImg, (x,y))
	
def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextMsg, TextCoords = text_objects(text, largeText)
	TextCoords.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextMsg, TextCoords)
	
	pygame.display.update()
	time.sleep(2)

#Define what happens after a crash and restart the game loop afterwards
def crash():
	message_display('You Crashed')
	game_loop()

#create a button
def button(msg,x,y,w,h,ic,ac,action=None):
	
	#print the mouse out
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
		
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(gameDisplay, ic,(x,y,w,h))	
	
	smallText = pygame.font.Font("freesansbold.ttf",20)
	textMsg, textCoords = text_objects(msg, smallText)
	textCoords.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textMsg, textCoords)


def quitgame():
	pygame.quit()
	
#displays a title at 15 fps. 
def game_intro():
	intro = True
	
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf',115)
		TextMsg, TextCoords = text_objects("Dodge..", largeText)
		TextCoords.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(TextMsg, TextCoords)
		
		button("GO", 150,450,100,50,green,bright_green,game_loop)
		button("Quit",550,450,100,50,red,bright_red,quitgame)
		
		pygame.display.update()
		clock.tick(15)

#Game loop
def game_loop():
	x = (display_width * 0.4)
	y = (display_height * 0.85)
	x_change = 0
	
	#this will be our object specs that will be created by the pygame.draw.rect() function inside the function things() we created
	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100
	
	#count of how many things you come accross and how many dodged
	thingCount = 1
	dodged = 0
	
	exited = False
	
	while not exited:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exited = True
		
			#Asking if event is keydown event (any key being pressed)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
					
		x += x_change
			
		gameDisplay.fill(white)
		car(x,y)
		
		#call things function we defined earlier with the variables created in game_loop()
		things(thing_startx, thing_starty, thing_width, thing_height, black)
		thing_starty += thing_speed
		car(x,y)
		blocks_dodged(dodged)
		
		#check if the car has crossed the left and right boundaries
		if x > display_width - car_width or x < 0:
			crash()
		
		#if the rectangle will spawn on the screen we want not to and instead spawn 600 spaces up so it seems like we come across it
		#when a block is recreated (meaning that you avoided it and it went off the screen where another is created) dodge count is accumulated
		#the speed is also slightly higher while the things created are also a little bigger
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)
			dodged += 1
			thing_speed += .3
			thing_width += (dodged *1.2)
		
		#Asking is y, the car's top left, has crossed the object's y + height, meaning the bottom left.
		#if it has, then we print that a y crossover has occured. 
		if y < thing_starty+thing_height:
			print('y crossover')
			
			if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx + thing_width:
				print('x crossover')
				crash()
		
		pygame.display.update()
		clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()

