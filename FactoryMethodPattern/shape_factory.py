import pygame.display

PI = 3.14


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


    @staticmethod
    def factory(type):
        if type == "Circle":
            return Circle(100, 100)
        if type == "Square":
            return Square(100, 100)
        if type == "Arc":
            return Arc(100, 100)
        if type == "Triangle":
            return Triangle(100, 100)

        assert 0, "Bad shape requested:" + type

class Square(Shape):
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(self.x, self.y, 20, 20))

class Circle(Shape):
    def draw(self):
        pygame.draw.circle(screen, (0, 255, 255), (self.x, self.y), 10)

class Arc(Shape):
    def draw(self):
        pygame.draw.arc(screen, (0, 0, 255), [self.x, self.y, 150, 125], 0, PI / 2, 2)

class Triangle(Shape):
    def draw(self):
        pygame.draw.polygon(screen, (255, 0, 255), [[self.x, self.x], [self.x, self.y], [self.y, self.y]], 5)


if __name__ == '__main__':
    window_dimension = 800, 600
    screen = pygame.display.set_mode(window_dimension)
    objS = Shape.factory("Square")
    objC = Shape.factory("Circle")
    objA = Shape.factory("Arc")
    objT = Shape.factory("Triangle")
    players_quit = False
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
            if pressed[pygame.K_a]:
                obj = objA
            if pressed[pygame.K_t]:
                obj = objT

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
