import pygame
import random
import sys

width, height = 800, 600
display = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
fps = 120

class Box:
    def __init__(self, x, y, size, direction):
        self.x = x
        self.y = y
        self.size = size
        self.direction = direction

    def move(self):
        self.x += self.direction[0]
        self.y += self.direction[1]
    
    def handle_direction_change(self):
        if self.x <= 0 or self.x + self.size >= width:
            self.direction[0] = -self.direction[0]

        if self.y <= 0 or self.y + self.size >= height:
            self.direction[1] = -self.direction[1]

def main():
    size = 100
    box = Box(random.randint(0, width - size), random.randint(0, height - size), size, [random.choice([1, -1]), random.choice([1, -1])])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill((0, 0, 0))
        box.move()
        box.handle_direction_change()
        pygame.draw.rect(display, (255, 255, 0), (box.x, box.y, box.size, box.size))

        pygame.display.update()

        clock.tick(fps)

    sys.exit()

main()