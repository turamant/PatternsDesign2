import abc

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
    def __str__(self):
        return f"{__class__.__name__}"

class Circle(Shape):
    def draw(self):
        pygame.draw.circle(screen, (0, 255, 255), (self.x, self.y), 10)
    def __str__(self):
        return f"{__class__.__name__}"


class AbstractFactory:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def make_object(self):
        return

class CircleFactory(AbstractFactory):
    def make_object(self):
        return Circle(100, 100)

class SquareFactory(AbstractFactory):
    def make_object(self):
        return Square(100, 100)




if __name__=='__main__':
    window_dimension = 800, 600
    screen = pygame.display.set_mode(window_dimension)
    players_quit = False

    objS = SquareFactory().make_object()
    objC = CircleFactory().make_object()
    obj = objS

    while not players_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                players_quit = True
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_c]:
                obj = objC
            if pressed[pygame.K_s]:
                obj = objS
            if pressed[pygame.K_UP]:
                obj.move('up')
            if pressed[pygame.K_DOWN]:
                obj.move('down')
            if pressed[pygame.K_LEFT]:
                obj.move('left')
            if pressed[pygame.K_RIGHT]:
                obj.move('right')

            screen.fill((0, 0, 0))
            obj.draw()
        pygame.display.flip()