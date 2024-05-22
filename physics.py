"""
Physics Simulation

Author: B SAI SANNIDH
Email: b.sai.sannidh@gmail.com
GitHub: https://github.com/kraVLonE/
Date: 2024-05-22
"""

import math

def pos_update(body, gravity):
    body.vel.j += gravity  # Apply gravity to the vertical velocity
    body.pos.i += body.vel.i
    body.pos.j += body.vel.j

def col_checker(A, B):
    distance = math.sqrt((A.pos.i - B.pos.i) ** 2 + (A.pos.j - B.pos.j) ** 2)
    return distance <= (A.r + B.r)

def col_res(A, B, fric):
    if A.pos.j == B.pos.j:
        st = 0              # st ---> sin_theta
        ct = 1              # ct ---> cos_theta
    elif A.pos.i == B.pos.i:
        st = 1
        ct = 0
    else:
        tt = (A.pos.j - B.pos.j) / (A.pos.i - B.pos.i)          # tt ---> tan_theta
        st = tt / math.sqrt(1 + tt ** 2)
        ct = st / tt

    ua_i = A.vel.i*ct + A.vel.j*st
    ua_j = A.vel.j*ct - A.vel.i*st
    ub_i = B.vel.i*ct + B.vel.j*st
    ub_j = B.vel.j*ct - B.vel.i*st

    va_j = ua_j
    vb_j = ub_j
    va_i = ((ua_i*(A.m-B.m))+(2*B.m*ub_i))/(A.m+B.m)
    vb_i = ((ub_i*(B.m-A.m))+(2*A.m*ua_i))/(A.m+B.m)

    va_i *= fric
    vb_i *= fric

    A.vel.i = va_i * ct - va_j * st
    B.vel.i = vb_i * ct - vb_j * st
    A.vel.j = va_i * st + va_j * ct
    B.vel.j = vb_i * st + vb_j * ct

def check_borders(body, width, height):
    if body.pos.i - body.r <= 0 or body.pos.i + body.r >= width:
        body.vel.i = -body.vel.i
    if body.pos.j - body.r <= 0 or body.pos.j + body.r >= height:
        body.vel.j = -body.vel.j
