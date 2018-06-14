import pygame

#initiate PyGame to run commands
pygame.init()

#sets the surface or canvas of the game as 800x600. 
gameDisplay = pygame.display.set_mode((800,600))

#Sets the display's caption
pygame.display.set_caption('KXSW')

#displays clock
clock = pygame.time.Clock()

#Game loop
exited = False
while not exited:

	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			exited = True
				
		print(event)
			
	pygame.display.update()
	clock.tick(60)
	
pygame.quit()
quit()
