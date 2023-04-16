import pygame
import random

# Constants
WIDTH = 800
HEIGHT = 600
GRAVITY = 0.1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(10, 20)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.velocity = 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.velocity *= -0.9

# Initialize Pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")

# List of balls
balls = []

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(Ball(event.pos[0], event.pos[1]))

    # Update balls
    for ball in balls:
        ball.update()

    # Draw balls
    screen.fill(WHITE)
    for ball in balls:
        ball.draw(screen)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
