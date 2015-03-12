""" A program that allows the user to draw with the mouse, changing colors by clicking on color blocks and changing size of brush using up and down arrow keys"""

import pygame
from pygame.locals import *
import random
import math
import time

class ShapeModel:
    """ Encodes the game state """
    def __init__(self):
        #initialize the color selection areas
        white = Rectangle(20, 20, 615, 5, (255, 255, 255))
        black = Rectangle(20, 20, 615, 25, (0, 0, 0))
        blue1 = Rectangle(20, 20, 615, 45, (56, 53, 157))
        blue2 = Rectangle(20, 20, 615, 65, (44, 92, 179))
        blue3 = Rectangle(20, 20, 615, 85, (178, 193, 248))#
        purple1 = Rectangle(20, 20, 615, 105, (105, 22, 144))#
        purple2 = Rectangle(20, 20, 615, 125, (189, 31, 141))#
        pink1 = Rectangle(20, 20, 615, 145, (253, 0, 137))#
        red1 = Rectangle(20, 20, 615, 165, (241, 43, 18))#
        orange1 = Rectangle(20, 20, 615, 185, (247, 135, 0))#
        yellow1 = Rectangle(20, 20, 615, 205, (252, 255, 0))#
        orange2 = Rectangle(20, 20, 615, 225, (253, 189, 110))#
        green1 = Rectangle(20, 20, 615, 265, (31, 184, 18))#
        green2 = Rectangle(20, 20, 615, 245, (189, 204, 114))#
        blue4 = Rectangle(20, 20, 615, 285, (6, 179, 252))#
        blue5 = Rectangle(20, 20, 615, 305, (184, 227, 250))

        #initialize the shape selection areas
        square = Rectangle(20, 20, 500, 5, (150, 150, 150))
        circle = Circle(10, 535, 15, (150, 150, 150))

        self.new_color = (255, 255, 255)
        self.size = 5
        self.rectangles = []
        self.circles = []
        self.stationary_rectangles = [white, black, blue1, blue2, blue3, purple1, purple2, pink1, red1, orange1, yellow1, orange2, green1, green2, blue4, blue5, square]
        self.stationary_circles = [circle]

        self.drawing = False
        self.shape = 'rectangle'

    def create_rectangle(self, width, height, xpos, ypos, color):
        rectangle = Rectangle(height, width, xpos, ypos, color)
        self.rectangles.append(rectangle)

    def create_circle(self, radius, xpos, ypos, color):
        circle = Circle(radius, xpos, ypos, color)
        self.circles.append(circle)

    def update(self, size, mouse_xpos, mouse_ypos):
        """ Creates a shape in response to mouse input """
        if self.drawing == True:
            if self.shape == 'rectangle':
                self.create_rectangle(size, size, mouse_xpos - size/2, mouse_ypos - size/2, self.new_color)
            elif self.shape == 'circle':
                self.create_circle(size/2, mouse_xpos, mouse_ypos, self.new_color)

class Rectangle:
    """ Encodes the state of a rectangle in the game """
    def __init__(self, height, width, x, y, color):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.vy = 0
        self.color = color

class Circle:
    """ Encodes the state of a circle in the game """
    def __init__(self, radius, x, y, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.vy = 0
        self.color = color


class ShapeView:
    """ A view of shape game rendered in a Pygame window """
    def __init__(self,model,screen,color):
        self.model = model
        self.screen = screen
        self.color = color
        self.falling = False
    
    def draw(self):
        """ Iterates through lists of gravitize-able and stationary rectangles and circles"""
        self.screen.fill(self.color)
        #rectangles and circles that will move when gravity is turned on
        for rectangle in self.model.rectangles:
            rectangle.y += rectangle.vy
            if self.falling:
                rectangle.vy += 0.01*rectangle.width
            pygame.draw.rect(self.screen, rectangle.color, pygame.Rect(rectangle.x, rectangle.y, rectangle.width, rectangle.height))
            if rectangle.y > 480:
                self.model.rectangles.remove(rectangle)

        for circle in self.model.circles:
            circle.y += circle.vy
            circle.y = int(circle.y)
            if self.falling:
                circle.vy += 0.02*circle.radius
            pygame.draw.circle(self.screen, circle.color, (circle.x, circle.y), circle.radius)
            if circle.y > 480:
                self.model.circles.remove(circle)

        #rectangles and circles for selection that don't move
        for rectangle in self.model.stationary_rectangles:
            pygame.draw.rect(self.screen, rectangle.color, pygame.Rect(rectangle.x, rectangle.y, rectangle.width, rectangle.height))

        for circle in self.model.stationary_circles:
            pygame.draw.circle(self.screen, circle.color, (circle.x, circle.y), circle.radius)

        pygame.display.update()

class ShapeController:
    """ responds to user input (mouse click and position)"""
    def __init__(self,model):
        self.model = model
        self.start_screen = True

    def handle_mouse_event(self,event):
        if event.type == MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            #start button detector
            if self.start_screen:
                if mouse_position[0] in range (270, 370):
                    if mouse_position[1] in range(216, 256):
                        self.start_screen = False
            #color selection detector
            if mouse_position[0] in range (615, 635):
                if mouse_position[1] in range(5, 25):
                    self.model.new_color = (255, 255, 255)
                elif mouse_position[1] in range(25, 45):
                    self.model.new_color = (0, 0, 0)
                elif mouse_position[1] in range(45, 65):
                    self.model.new_color = (56, 53, 157) #blue1
                elif mouse_position[1] in range(65, 85):
                    self.model.new_color = (44, 92, 179) #blue2
                elif mouse_position[1] in range(85, 105):
                    self.model.new_color = (178, 193, 248) #blue3
                elif mouse_position[1] in range(105, 125):
                    self.model.new_color = (105, 22, 144) #purple1
                elif mouse_position[1] in range(125, 145):
                    self.model.new_color = (189, 31, 141) #purple2
                elif mouse_position[1] in range(145, 165):
                    self.model.new_color = (253, 0, 137) #pink1
                elif mouse_position[1] in range(165, 185):
                    self.model.new_color = (241, 43, 18) #red1
                elif mouse_position[1] in range(185, 205):
                    self.model.new_color = (247, 135, 0) #orange1
                elif mouse_position[1] in range(205, 225):
                    self.model.new_color = (252, 255, 0) #yellow1
                elif mouse_position[1] in range(225, 245):
                    self.model.new_color = (253, 189, 110) #orange2
                elif mouse_position[1] in range(265, 285):
                    self.model.new_color = (31, 184, 18) #green1
                elif mouse_position[1] in range(245, 265):
                    self.model.new_color = (189, 204, 114) #green2
                elif mouse_position[1] in range(285, 305):
                    self.model.new_color = (6, 179, 252) #blue4
                elif mouse_position[1] in range(305, 325):
                    self.model.new_color = (184, 227, 250) #blue5
            #shape selection detector
            if mouse_position[1] in range (5, 25):
                if mouse_position[0] in range(500, 520):
                    self.model.shape = 'rectangle'
                if mouse_position[0] in range(525, 545):
                    self.model.shape = 'circle'

            self.model.x = mouse_position[0]
            self.model.y = mouse_position[1]
            self.model.drawing = True

        elif event.type == MOUSEBUTTONUP:
            self.model.drawing = False

    def handle_keyboard_event(self, event, view):
        """ changes size of brush and toggles gravity based on keyboard input"""
        if event.key == pygame.K_UP:
            self.model.size = self.model.size + 1
        elif event.key == pygame.K_DOWN:
            if self.model.size is not 1:
                self.model.size = self.model.size - 1
        elif event.key == pygame.K_LEFT:
            view.falling = False
        elif event.key == pygame.K_RIGHT:
            view.falling = True

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('ShapesPaint')
    image = pygame.image.load('ShapesPaintStart.PNG')

    #starting screen
    start_model = ShapeModel()
    start_model.stationary_rectangles = []
    start_model.stationary_circles = []
    start_view = ShapeView(start_model, screen, pygame.Color(240, 200, 80))

    #drawing screen
    model = ShapeModel()
    view = ShapeView(model, screen, pygame.Color(0, 0, 0))
    controller = ShapeController(model)
    
    running = True
    
    while running:
        if controller.start_screen:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN or MOUSEBUTTONUP:
                    controller.handle_mouse_event(event)

            screen.blit(image, (0, 0))
            pygame.display.flip()
            time.sleep(.005)

        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN or MOUSEBUTTONUP:
                    controller.handle_mouse_event(event)
                if event.type == KEYDOWN:
                    controller.handle_keyboard_event(event, view)

            model.update(model.size, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            view.draw()
            time.sleep(.005)
        
    pygame.quit()