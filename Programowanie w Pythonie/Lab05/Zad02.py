from vpython import *
from datetime import datetime
import time

scene.center = vector(0, 0, 0)
scene.forward = vector(-1, 0, 0)
scene.up = vector(0, 1, 0)
scene.width = 1800
scene.height = 850
rod = cylinder(pos=vector(0, 0, 0), axis=vector(1, 0, 0), radius=5)

mybox1 = box(pos=vector(1.1, 0, 0), axis=vector(1, 0, 0), size=vector(0.5, 0.25, 0.25), color=color.black)
pointer = box(pos=vector(1.1, 2, 0), axis=vector(0, 1, 0), size=vector(4.75, 0.1, 0.1), color=color.green)
pointer1 = box(pos=vector(1.15, 1.5, 0), axis=vector(0, 1, 0), size=vector(3.75, 0.1, 0.2), color=color.red)
pointer2 = box(pos=vector(1.2, 1, 0), axis=vector(0, 1, 0), size=vector(2.75, 0.1, 0.3), color=color.blue)
h1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)
h2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)
h3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)
h4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)
h5 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)
h6 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)
h7 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)
h8 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)
h9 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)
h10 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)
h11 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)
h12 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.4, 0.1, 0.1), color=color.black)

h2.rotate(angle=radians(-(360 / 12)), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h3.rotate(angle=radians(-(360 / 12) * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h4.rotate(angle=radians(-(360 / 12) * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h5.rotate(angle=radians(-(360 / 12) * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h6.rotate(angle=radians(-(360 / 12) * 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h7.rotate(angle=radians(-(360 / 12) * 6), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h8.rotate(angle=radians(-(360 / 12) * 7), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h9.rotate(angle=radians(-(360 / 12) * 8), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h10.rotate(angle=radians(-(360 / 12) * 9), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h11.rotate(angle=radians(-(360 / 12) * 10), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h12.rotate(angle=radians(-(360 / 12) * 11), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))

h1_1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h1_1.rotate(angle=radians(-(360 / 12) / 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h1_2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h1_2.rotate(angle=radians(-(360 / 12) / 5 * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h1_3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h1_3.rotate(angle=radians(-(360 / 12) / 5 * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h1_4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h1_4.rotate(angle=radians(-(360 / 12) / 5 * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))

h2_1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h2_1.rotate(angle=radians(-(360 / 12) - (360 / 12) / 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h2_2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h2_2.rotate(angle=radians(-(360 / 12) - (360 / 12) / 5 * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h2_3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h2_3.rotate(angle=radians(-(360 / 12) - (360 / 12) / 5 * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h2_4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h2_4.rotate(angle=radians(-(360 / 12) - (360 / 12) / 5 * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))

h3_1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h3_1.rotate(angle=radians(-(360 / 12) * 2 - (360 / 12) / 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h3_2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h3_2.rotate(angle=radians(-(360 / 12) * 2 - (360 / 12) / 5 * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h3_3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h3_3.rotate(angle=radians(-(360 / 12) * 2 - (360 / 12) / 5 * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h3_4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h3_4.rotate(angle=radians(-(360 / 12) * 2 - (360 / 12) / 5 * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))

h4_1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h4_1.rotate(angle=radians(-(360 / 12) * 3 - (360 / 12) / 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h4_2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h4_2.rotate(angle=radians(-(360 / 12) * 3 - (360 / 12) / 5 * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h4_3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h4_3.rotate(angle=radians(-(360 / 12) * 3 - (360 / 12) / 5 * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h4_4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h4_4.rotate(angle=radians(-(360 / 12) * 3 - (360 / 12) / 5 * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))

h5_1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h5_1.rotate(angle=radians(-(360 / 12) * 4 - (360 / 12) / 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h5_2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h5_2.rotate(angle=radians(-(360 / 12) * 4 - (360 / 12) / 5 * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h5_3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h5_3.rotate(angle=radians(-(360 / 12) * 4 - (360 / 12) / 5 * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h5_4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h5_4.rotate(angle=radians(-(360 / 12) * 4 - (360 / 12) / 5 * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))

h6_1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h6_1.rotate(angle=radians(-(360 / 12) * 5 - (360 / 12) / 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h6_2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h6_2.rotate(angle=radians(-(360 / 12) * 5 - (360 / 12) / 5 * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h6_3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h6_3.rotate(angle=radians(-(360 / 12) * 5 - (360 / 12) / 5 * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h6_4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h6_4.rotate(angle=radians(-(360 / 12) * 5 - (360 / 12) / 5 * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))

h7_1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h7_1.rotate(angle=radians(-(360 / 12) * 6 - (360 / 12) / 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h7_2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h7_2.rotate(angle=radians(-(360 / 12) * 6 - (360 / 12) / 5 * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h7_3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h7_3.rotate(angle=radians(-(360 / 12) * 6 - (360 / 12) / 5 * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h7_4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h7_4.rotate(angle=radians(-(360 / 12) * 6 - (360 / 12) / 5 * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))

h8_1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h8_1.rotate(angle=radians(-(360 / 12) * 8 - (360 / 12) / 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h8_2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h8_2.rotate(angle=radians(-(360 / 12) * 8 - (360 / 12) / 5 * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h8_3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h8_3.rotate(angle=radians(-(360 / 12) * 8 - (360 / 12) / 5 * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h8_4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h8_4.rotate(angle=radians(-(360 / 12) * 8 - (360 / 12) / 5 * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))

h9_1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h9_1.rotate(angle=radians(-(360 / 12) * 9 - (360 / 12) / 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h9_2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h9_2.rotate(angle=radians(-(360 / 12) * 9 - (360 / 12) / 5 * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h9_3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h9_3.rotate(angle=radians(-(360 / 12) * 9 - (360 / 12) / 5 * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h9_4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h9_4.rotate(angle=radians(-(360 / 12) * 9 - (360 / 12) / 5 * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))

h10_1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h10_1.rotate(angle=radians(-(360 / 12) * 10 - (360 / 12) / 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h10_2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h10_2.rotate(angle=radians(-(360 / 12) * 10 - (360 / 12) / 5 * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h10_3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h10_3.rotate(angle=radians(-(360 / 12) * 10 - (360 / 12) / 5 * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h10_4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h10_4.rotate(angle=radians(-(360 / 12) * 10 - (360 / 12) / 5 * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))

h11_1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h11_1.rotate(angle=radians(-(360 / 12) * 11 - (360 / 12) / 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h11_2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h11_2.rotate(angle=radians(-(360 / 12) * 11 - (360 / 12) / 5 * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h11_3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h11_3.rotate(angle=radians(-(360 / 12) * 11 - (360 / 12) / 5 * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h11_4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h11_4.rotate(angle=radians(-(360 / 12) * 11 - (360 / 12) / 5 * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))

h12_1 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h12_1.rotate(angle=radians(-(360 / 12) * 7 - (360 / 12) / 5), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h12_2 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h12_2.rotate(angle=radians(-(360 / 12) * 7 - (360 / 12) / 5 * 2), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h12_3 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h12_3.rotate(angle=radians(-(360 / 12) * 7 - (360 / 12) / 5 * 3), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
h12_4 = box(pos=vector(1, 4.75, 0), axis=vector(0, 1, 0), size=vector(0.25, 0.05, 0.05), color=color.black)
h12_4.rotate(angle=radians(-(360 / 12) * 7 - (360 / 12) / 5 * 4), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
now = datetime.now()

a = str(now).split(" ")
hms = a[1].split(":")

sec = int(hms[2].split(".")[0])
min = int(hms[1])
h = int(hms[0])

pointer.rotate(angle=radians(-(360 / 60) * sec), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
pointer1.rotate(angle=radians(-(360 / 3600) * (sec + 60 * min)), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
pointer2.rotate(angle=radians(-(360 / 86400 * 2) * (sec + 60 * min + 3600 * h)), axis=vector(1, 0, 0),
                origin=vector(1.2, 0, 0))
while 1:
    time.sleep(1)
    pointer.rotate(angle=radians(-(360 / 60)), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
    pointer1.rotate(angle=radians(-(360 / 3600)), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
    pointer2.rotate(angle=radians(-(360 / 86400)), axis=vector(1, 0, 0), origin=vector(1.2, 0, 0))
