from vpython import *
import numpy as np
from datetime import datetime
import time
import math

np.seterr(divide='ignore', invalid='ignore')
xswap = 90
zswap = 90


def bounce_band(ball,i):
    ball.pos = ball.pos + ball.velocity * dt
    if ball.pos.x <= -42.5 or ball.pos.x >= 42.5 and colisonwall[i] == False:
        ball.velocity.x = -ball.velocity.x
        colisonwall[i] = True

    if ball.pos.z <= -87.5 or ball.pos.z >= 87.5 and colisonwall[i] == False:
        colisonwall[i] = True
        ball.velocity.z = -ball.velocity.z
    if colisonwall[i] == True and (ball.pos.z > -87.5 and ball.pos.z < 87.5) and (ball.pos.x > -42.5 and ball.pos.x < 42.5):
        colisonwall[i] = False
def bounce_ball(ball, ballv2,i,j):
    global xswap
    if (ball.pos.x - ballv2.pos.x) ** 2 + (ball.pos.z - ballv2.pos.z) ** 2 <= 5 ** 2 and i != j and colison[i] == False and colison[j] == False:
        colison[i] = True
        colison[j] = True
        phi = math.atan2(ballv2.velocity.x-ball.velocity.x,ballv2.velocity.z-ball.velocity.z)
        if phi < 0:
            phi = phi + 2 * np.pi
        teta1 = math.atan2(ball.velocity.x,ball.velocity.z)
        if teta1 < 0:
            teta1 = teta1 + np.pi*2
        teta2 = math.atan2(ballv2.velocity.x,ballv2.velocity.z)
        if teta2 < 0:
            teta2 = teta2 + np.pi*2
        ballval = [ball.velocity.x, ball.velocity.z]
        ball.velocity.z = math.sqrt(ballv2.velocity.x**2+ ballv2.velocity.z**2) * round(math.cos(teta2 - phi),2) * round(math.cos(phi),2) + math.sqrt(ball.velocity.x**2+ ball.velocity.z**2) * round(math.sin(teta1 - phi),2) * round(math.cos(phi + (np.pi / 2)),2)
        ball.velocity.x = math.sqrt(ballv2.velocity.x**2+ ballv2.velocity.z**2) * round(math.cos(teta2 - phi),2) * round(math.sin(phi),2) + math.sqrt(ball.velocity.x**2+ ball.velocity.z**2) * round(math.sin(teta1 - phi),2) * round(math.sin(phi + (np.pi / 2)),2)

        ballv2.velocity.z = math.sqrt(ballval[0]**2 + ballval[1]**2) * round(math.cos(teta1 - phi),2) *round(math.cos(phi),2) + math.sqrt(ballv2.velocity.x**2+ ballv2.velocity.z**2) *  round(math.sin(teta2 - phi),2)  * round(math.cos(phi + (np.pi / 2)),2)
        ballv2.velocity.x = math.sqrt(ballval[0]**2 + ballval[1]**2) * round(math.cos(teta1 - phi),2) * round(math.sin(phi),2) + math.sqrt(ballv2.velocity.x**2+ ballv2.velocity.z**2) *  round(math.sin(teta2 - phi),2) * round(math.sin(phi + (np.pi / 2)),2)

        print(phi)
        print(teta1)
        print(teta2)
        # print("----------------")
        # print(ball.velocity.x)
        # print(ball.velocity.z)
        # print(ballv2.velocity.x)
        # print(ballv2.velocity.z)
        # print("----------------")
        # print(math.sqrt(ballval[0] ** 2 + ballval[1] ** 2))
        # print(math.sqrt(ball.velocity.x ** 2 + ball.velocity.z ** 2))
        # print(math.sqrt(ballv2.velocity.x**2+ ballv2.velocity.z**2))
        # print(math.cos(teta2 - phi))
        # print(math.cos(phi))
    if(ball.pos.x - ballv2.pos.x) ** 2 + (ball.pos.z - ballv2.pos.z) ** 2 >= 5.1 ** 2 and colison[i] == True and colison[j] == True:
        colison[i] = False
        colison[j] = False
scene.center = vector(0, 0, 0)
scene.forward = vector(-1, -1, 0)
scene.up = vector(0, 1, 0)
scene.width = 1800
scene.height = 850
z = box(pos=vector(0, 0, 0), axis=vector(1, 0, 0), size=vector(100, 0.25, 0.25), color=color.red)
y = box(pos=vector(0, 0, 0), axis=vector(1, 0, 0), size=vector(0.25, 100, 0.25), color=color.blue)
z = box(pos=vector(0, 0, 0), axis=vector(1, 0, 0), size=vector(0.25, 0.25, 100), color=color.black)

blat = box(pos=vector(0, -10, 0), axis=vector(1, 0, 0), size=vector(90, 0.25, 180), color=color.green)
blat_siana_1 = box(pos=vector(0, -5, 90), axis=vector(1, 0, 0), size=vector(90, 10, 0.25), color=color.green)
blat_siana_2 = box(pos=vector(0, -5, -90), axis=vector(1, 0, 0), size=vector(90, 10, 0.25), color=color.green)
blat_siana_3 = box(pos=vector(45, -5, 0), axis=vector(1, 0, 0), size=vector(0.25, 10, 180), color=color.green)
blat_siana_4 = box(pos=vector(-45, -5, 0), axis=vector(1, 0, 0), size=vector(0.25, 10, 180), color=color.green)
drewno_obramowka = box(pos=vector(47.5, 0, 0), axis=vector(1, 0, 0), size=vector(5, 0.25, 190),
                       texture=textures.wood_old)
drewno_obramowka2 = box(pos=vector(-47.5, 0, 0), axis=vector(1, 0, 0), size=vector(5, 0.25, 190),
                        texture=textures.wood_old)
drewno_obramowka2 = box(pos=vector(0, 0, 92.5), axis=vector(1, 0, 0), size=vector(100, 0.25, 5),
                        texture=textures.wood_old)
drewno_obramowka2 = box(pos=vector(0, 0, -92.5), axis=vector(1, 0, 0), size=vector(100, 0.25, 5),
                        texture=textures.wood_old)

drewno_siana_1 = box(pos=vector(0, -7.5, 95), axis=vector(1, 0, 0), size=vector(100, 15, 0.25),
                     texture=textures.wood_old)
drewno_siana_2 = box(pos=vector(0, -7.5, -95), axis=vector(1, 0, 0), size=vector(100, 15, 0.25),
                     texture=textures.wood_old)
drewno_siana_3 = box(pos=vector(50, -7.5, 0), axis=vector(1, 0, 0), size=vector(0.25, 15, 190),
                     texture=textures.wood_old)
drewno_siana_4 = box(pos=vector(-50, -7.5, 0), axis=vector(1, 0, 0), size=vector(0.25, 15, 190),
                     texture=textures.wood_old)

drwno_blat = box(pos=vector(0, -15, 0), axis=vector(1, 0, 0), size=vector(100, 0.25, 190), texture=textures.wood_old)

drwno_noga_1_dol = box(pos=vector(43, -45, 88), axis=vector(1, 0, 0), size=vector(14, 60, 14),
                       texture=textures.wood_old)
drwno_noga_2_dol = box(pos=vector(43, -45, -88), axis=vector(1, 0, 0), size=vector(14, 60, 14),
                       texture=textures.wood_old)

drwno_noga_3_dol = box(pos=vector(-43, -45, 88), axis=vector(1, 0, 0), size=vector(14, 60, 14),
                       texture=textures.wood_old)

drwno_noga_4_dol = box(pos=vector(-43, -45, -88), axis=vector(1, 0, 0), size=vector(14, 60, 14),
                       texture=textures.wood_old)
ball1 = sphere(pos=vector(0, -7.35, 0), radius=2.5, color=color.yellow)
ball2 = sphere(pos=vector(0, -7.35, -45), radius=2.5, color=color.cyan)
ball3 = sphere(pos=vector(0, -7.35, 42), radius=2.5)
ball4 = sphere(pos=vector(15, -7.35, 84), radius=2.5)
ball5 = sphere(pos=vector(23, -7.35, 5), radius=2.5)
ball6 = sphere(pos=vector(3, -7.35, 7), radius=2.5)
ball7 = sphere(pos=vector(10, -7.35, 50), radius=2.5)
ball8 = sphere(pos=vector(40, -7.35, -32), radius=2.5)


ball1.velocity = vector(0, 0, 1)
ball2.velocity = vector(0, 0, -1)
ball3.velocity = vector(random(), 0, random())
ball4.velocity = vector(random(), 0, random())
ball5.velocity = vector(random(), 0, random())
ball6.velocity = vector(random(), 0, random())
ball7.velocity = vector(random(), 0, random())
ball8.velocity = vector(random(), 0, random())

ballz = []
ballz.append(ball1)
ballz.append(ball2)
ballz.append(ball3)
ballz.append(ball4)
ballz.append(ball5)
ballz.append(ball6)
ballz.append(ball7)
ballz.append(ball8)
colison = [False]*len(ballz)
colisonwall = [False]*len(ballz)
dt = 0.3
while 1:
    rate(100)

    for i in range(len(ballz)):
        bounce_band(ballz[i],i)
        for j in range( len(ballz)):
            bounce_ball(ballz[i], ballz[j],i,j)
