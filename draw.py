"""
Physics Simulation

Author: B SAI SANNIDH
Email: b.sai.sannidh@gmail.com
GitHub: https://github.com/kraVLonE/
Date: 2024-05-22
"""

import pygame

def draw_body(screen, body):
    pygame.draw.circle(screen, body.color, (int(body.pos.i), int(body.pos.j)), int(body.r))
