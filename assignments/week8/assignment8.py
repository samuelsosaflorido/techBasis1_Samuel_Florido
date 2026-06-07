# For this assignment I decided to create a funny animated situation using two images from the anime Neon Genesis Evangelion
# First of all, I chose the image where Shinji is sitting on the chair at the ending of the anime, which has become a massive meme
# After this, I decided to introduce certain random elements on it, such as speed and size of the image
# In order to add a funnier situation for this, I decided to introduce the meme of Asuka saying "Pathetic" as a background image
# For this assignment I have used also Claude AI in order to help me understand the code, check possible mistakes and give feedback
# Working on this code was a little bit challenging as I had to understand how to properly introduce the random elements and also the scales
# Adding also the randomness and position of the images took me a long while to understand it but thanks to the help of Claude I think I managed to implement it correctly


import pygame
import random

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (255, 255, 255)


# Defining class
class DepressedShinji():
    def __init__(self, pos_x=0, pos_y=0):
        self.img = pygame.image.load("depressedshinji.png").convert_alpha()
        size = random.randint(50, 150)
        self.img = pygame.transform.scale(self.img, (size, size))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_x = random.uniform(2, 6)
        self.speed_y = random.uniform(-3, 3)

    # Move method
    def move(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        if self.pos_x > SCREEN_WIDTH:
            self.pos_x = -100
        if self.pos_y > SCREEN_HEIGHT - 100 or self.pos_y < 0:
            self.speed_y *= -1

    def draw(self):
        screen.blit(self.img, (self.pos_x, self.pos_y))


# Setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Assignment 8")
clock = pygame.time.Clock()

asuka = pygame.image.load("asuka.png").convert()
asuka = pygame.transform.scale(asuka, (SCREEN_WIDTH, SCREEN_HEIGHT))

depressedshinji1 = DepressedShinji(pos_x=random.randint(0, SCREEN_WIDTH), pos_y=random.randint(0, SCREEN_HEIGHT - 100))
depressedshinji2 = DepressedShinji(pos_x=random.randint(0, SCREEN_WIDTH), pos_y=random.randint(0, SCREEN_HEIGHT - 100))
depressedshinji3 = DepressedShinji(pos_x=random.randint(0, SCREEN_WIDTH), pos_y=random.randint(0, SCREEN_HEIGHT - 100))
depressedshinji4 = DepressedShinji(pos_x=random.randint(0, SCREEN_WIDTH), pos_y=random.randint(0, SCREEN_HEIGHT - 100))

# This is for defining the movements
flag = True
while flag:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    # Using Claude, I added this to draw Asuka first so she appears as a background image while the different Shinjis are moving
    screen.blit(asuka, (0, 0))

    # for each Shinji: first move() to update position, then draw() to show it
    # I added this specific order for the images to move following what has been defined earlier
    depressedshinji1.move()
    depressedshinji1.draw()
    depressedshinji2.move()
    depressedshinji2.draw()
    depressedshinji3.move()
    depressedshinji3.draw()
    depressedshinji4.move()
    depressedshinji4.draw()

    pygame.display.flip()

pygame.quit()
exit(0)
