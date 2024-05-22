"""
Physics Simulation

Author: B SAI SANNIDH
Email: b.sai.sannidh@gmail.com
GitHub: https://github.com/kraVLonE/
Date: 2024-05-22
"""

class Vec:
    def __init__(self, i, j):
        self.i = i
        self.j = j

class Body:
    def __init__(self, pos, vel, r, m, color):
        self.pos = pos
        self.vel = vel
        self.r = r
        self.m = m
        self.color = color
