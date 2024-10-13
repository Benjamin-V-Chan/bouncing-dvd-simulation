import pygame
import random
import sys

width, height = 800, 600
display = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
FPS = 120

COLORS = [(255, 0, 0),
            (255, 255, 0),
            (0, 255, 0),
            (0, 255, 255),
            (0, 0, 255),
            (255, 0, 255)]

def rotate_color(color_index):
    if color_index >= len(COLORS) - 1:
        return 0
    return color_index + 1

class Box:
    def __init__(self, x, y, size, color_index, direction):
        self.x = x
        self.y = y
        self.size = size
        self.color_index = color_index
        self.direction = direction

    def move(self):
        self.x += self.direction[0]
        self.y += self.direction[1]
    
    def handle_direction_change(self):
        if self.x <= 0 or self.x + self.size >= width:
            self.direction[0] = -self.direction[0]
            self.color_index = rotate_color(self.color_index)

        if self.y <= 0 or self.y + self.size >= height:
            self.direction[1] = -self.direction[1]
            self.color_index = rotate_color(self.color_index)

def main():
    size = 100
    box = Box(random.randint(0, width - size), random.randint(0, height - size), size, random.randint(0, len(COLORS) - 1), [random.choice([1, -1]), random.choice([1, -1])])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill((0, 0, 0))

        box.move()
        box.handle_direction_change()
        pygame.draw.rect(display, COLORS[box.color_index], (box.x, box.y, box.size, box.size))

        pygame.display.update()

        clock.tick(FPS)

    sys.exit()

main()