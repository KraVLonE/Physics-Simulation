"""
Physics Simulation

Author: B SAI SANNIDH
Email: b.sai.sannidh@gmail.com
GitHub: https://github.com/kraVLonE/
Date: 2024-05-22
"""

import pygame
import body
import physics
import draw

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Simulation with Bouncing, Gravity, and Collisions")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

def handle_events(bodies):
    global GRAVITY, fric
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                GRAVITY += 0.1
            elif event.key == pygame.K_f:
                GRAVITY = max(0, GRAVITY - 0.1)
            elif event.key == pygame.K_e:
                fric = min(1, fric + 0.1)
            elif event.key == pygame.K_i:
                fric = max(0, fric - 0.1)
    return True

def inputs():
    num_balls = int(input("Enter the number of balls: "))
    balls = []
    for _ in range(num_balls):
        x, y = map(int, input("Enter position (x y): ").split())
        vx, vy = map(float, input("Enter velocity (vx vy): ").split())
        radius = float(input("Enter radius: "))
        mass = float(input("Enter mass: "))
        color = tuple(map(int, input("Enter color (R G B): ").split()))
        ball = body.Body(body.Vec(x, y), body.Vec(vx, vy), radius, mass, color)
        balls.append(ball)
    return balls

def main():
    global GRAVITY, fric
    GRAVITY = 0.1  # Gravitational acceleration
    fric = 1  # 1 for elastic, < 1 for inelastic

    balls = inputs()

    flag = True
    while flag:
        screen.fill(BLACK)

        flag = handle_events(balls)

        for b in balls:
            physics.pos_update(b, GRAVITY)
            physics.check_borders(b, WIDTH, HEIGHT)

        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                if physics.col_checker(balls[i], balls[j]):
                    physics.col_res(balls[i], balls[j], fric)

        for b in balls:
            draw.draw_body(screen, b)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
