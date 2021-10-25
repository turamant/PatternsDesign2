import time

import pygame



class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        raise NotImplementedError

    def move(self, direction):
        if direction == 'up':
            self.y -= 4
        if direction == 'down':
            self.y += 4
        if direction == 'left':
            self.x -= 4
        if direction == 'right':
            self.x += 4

class Square(Shape):
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(self.x, self.y, 20, 20))

class Circle(Shape):
    def draw(self):
        pygame.draw.circle(screen, (0, 255, 255), (self.x, self.y), 10)

if __name__ == '__main__':
    window_dimensions = 800, 600
    #pygame.init()
    screen = pygame.display.set_mode(window_dimensions)
    players_quit = False
    square = Square(100, 100)
    circle = Circle(100, 100)
    obj = square
    while not players_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                players_quit = True
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                obj.move('up')
            if pressed[pygame.K_DOWN]:
                obj.move('down')
            if pressed[pygame.K_LEFT]:
                obj.move('left')
            if pressed[pygame.K_RIGHT]:
                obj.move('right')
            if pressed[pygame.K_c]:
                obj = circle
            if pressed[pygame.K_s]:
                obj = square
            screen.fill((0, 0, 0))
            obj.draw()
        pygame.display.flip()




