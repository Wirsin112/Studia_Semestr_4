from vpython import *
from datetime import datetime
import time

scene.center = vector(0, 0, 0)
scene.forward = vector(-1, -1, 0)
scene.up = vector(0, 1, 0)
scene.width = 1800
scene.height = 850
z = box(pos=vector(0, 0, 0), axis=vector(1, 0, 0), size=vector(100, 0.25, 0.25), color=color.red)
y = box(pos=vector(0, 0, 0), axis=vector(1, 0, 0), size=vector(0.25, 100, 0.25), color=color.blue)
z = box(pos=vector(0, 0, 0), axis=vector(1, 0, 0), size=vector(0.25, 0.25, 100), color=color.green)


blat = box(pos=vector(0, -10, 0), axis=vector(1, 0, 0), size=vector(90, 0.25, 180), color=color.green)
blat_siana_1 = box(pos=vector(0, -5, 90), axis=vector(1, 0, 0), size=vector(90, 10, 0.25), color=color.green)
blat_siana_2 = box(pos=vector(0, -5, -90), axis=vector(1, 0, 0), size=vector(90, 10, 0.25), color=color.green)
blat_siana_3 = box(pos=vector(45, -5, 0), axis=vector(1, 0, 0), size=vector(0.25, 10, 180), color=color.green)
blat_siana_4 = box(pos=vector(-45, -5, 0), axis=vector(1, 0, 0), size=vector(0.25, 10, 180), color=color.green)
drewno_obramowka = box(pos=vector(47.5, 0, 0), axis=vector(1, 0, 0), size=vector(5, 0.25, 190),texture=textures.wood_old)
drewno_obramowka2 = box(pos=vector(-47.5, 0, 0), axis=vector(1, 0, 0), size=vector(5, 0.25, 190),texture=textures.wood_old)
drewno_obramowka2 = box(pos=vector(0, 0, 92.5), axis=vector(1, 0, 0), size=vector(100, 0.25, 5),texture=textures.wood_old)
drewno_obramowka2 = box(pos=vector(0, 0, -92.5), axis=vector(1, 0, 0), size=vector(100, 0.25, 5),texture=textures.wood_old)

drewno_siana_1 = box(pos=vector(0, -7.5, 95), axis=vector(1, 0, 0), size=vector(100, 15, 0.25), texture=textures.wood_old)
drewno_siana_2 = box(pos=vector(0, -7.5, -95), axis=vector(1, 0, 0), size=vector(100, 15, 0.25), texture=textures.wood_old)
drewno_siana_3 = box(pos=vector(50, -7.5, 0), axis=vector(1, 0, 0), size=vector(0.25, 15, 190), texture=textures.wood_old)
drewno_siana_4 = box(pos=vector(-50, -7.5, 0), axis=vector(1, 0, 0), size=vector(0.25, 15, 190), texture=textures.wood_old)

drwno_blat = box(pos=vector(0, -15, 0), axis=vector(1, 0, 0), size=vector(100, 0.25, 190), texture=textures.wood_old)

drwno_noga_1_dol = box(pos=vector(43, -45, 88), axis=vector(1, 0, 0), size=vector(14, 60, 14), texture=textures.wood_old)
drwno_noga_2_dol = box(pos=vector(43, -45, -88), axis=vector(1, 0, 0), size=vector(14, 60, 14), texture=textures.wood_old)

drwno_noga_3_dol = box(pos=vector(-43, -45, 88), axis=vector(1, 0, 0), size=vector(14, 60, 14), texture=textures.wood_old)

drwno_noga_4_dol = box(pos=vector(-43, -45, -88), axis=vector(1, 0, 0), size=vector(14, 60, 14), texture=textures.wood_old)
ball1 = sphere(pos=vector(-6,-7,-6),radius=2.5)
ball2 = sphere(pos=vector(30,-7,20),radius=2.5)
ball3 = sphere(pos=vector(3,-7,42),radius=2.5)
ball4 = sphere(pos=vector(15,-7,84),radius=2.5)
ball5 = sphere(pos=vector(23,-7,5),radius=2.5)
ball6 = sphere(pos=vector(3,-7,7),radius=2.5)
ball7 = sphere(pos=vector(10,-7,50),radius=2.5)
ball8 = sphere(pos=vector(40,-7,-32),radius=2.5)

while 1:
    sleep(0.2)
    ball1.rotate(angle=20,axis=vec(0,0,0),origin=vector(0,0,0))
