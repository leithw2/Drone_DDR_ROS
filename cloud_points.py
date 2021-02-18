import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time
xs= []
ys= []
zs= []
class Point:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0

class wall:
    def __init__(self, angle, orientation, center, height, width):
        self.angle  = angle #z
        self.ori    = orientation # +1 right -1 left
        self.center = center
        self.height = height
        self.width_x  = width_x
        self.width_y  = width_y

    def check_collition(self, point, t):
        #print(point.x)
        if point.z <= self.height and point.x <= self.center[0] + self.width_y and point.x >= self.center[0] - self.width_y:
            if (self.ori == -1):
                #if (point.x >= self.center[0] - self.width_x):
                    if ((point.y ) >= self.center[1] + self.angle * t ):
                        return True
            if (self.ori == +1):
                #if (point.x <= -self.center[0] - self.width_x):
                    if ((point.y ) <= -self.center[1] + self.angle * t):
                        return True

        return False

class wallL(wall):
    def __init__(self):

        self.angle = .0 #z
        self.ori = -1 # +1 right -1 left
        self.center = [0,1,0]
        self.height = 1
        self.width_x = 2
        self.width_y = 2



class wallR(wall):
    def __init__(self):

        self.angle = -.0 #z
        self.ori = 1 # +1 right -1 left
        self.center = [0,1,0]
        self.height = 1
        self.width_x = 2
        self.width_y = 2


class wallB(wall):
    def __init__(self):

        self.angle = -.1 #z
        self.ori = -1 # +1 right -1 left
        self.center = [4,0,0]
        self.height = 1
        self.width = 10

    def check_collition(self, point, t):
        #print(point.x)
        if point.z <= self.height:
            if ((point.x - self.center[1]*0) >= self.center[0] + self.angle * t):
                return True


        return False


class Floor(wall):
    def __init__(self):

        self.angle = -0 #z
        self.ori = +1 # +1 right -1 left
        self.center = [0,0,-.4]
        self.height = 2
        self.width = 10


    def check_collition(self, point, t):
        #print(point.x)
        if (self.ori == -1):
            if (point.z >= -self.center[2] + self.angle * t):
                return True
        if (self.ori == +1):
            if (point.z <= self.center[2] + self.angle * t):
                return True

        return False

class roof(wall):
    def __init__(self):
        pass


wL = wallL()
wR = wallR()
wB = wallB()
floor = Floor()
point = Point()

colliders = []
dist = []
wallFound =False

c_open = 1
l_range = 6
norma = np.linalg.norm([l_range, c_open, c_open])

def randomizer0():
    wL = wallL()
    wR = wallR()
    #wB = wallB()
    floor = Floor()
    #point = Point()

    colliders = []

    colliders.append(wR)
    colliders.append(wL)
    #colliders.append(wB)
    colliders.append(floor)

    for coll in colliders:
        coll.angle = np.random.uniform(low=-0.2, high=0.2)
        coll.center= (coll.center[0] + np.random.uniform(low=-.3, high=.3),
                      coll.center[1] + np.random.uniform(low=-.5, high=.5),
                      coll.center[2] + np.random.uniform(low=-.3, high=.3))

        coll.height = coll.height + np.random.uniform(low=-.3, high=.3)

    return colliders

def randomizer1():
    wL = wallL()
    wR = wallR()
    wB = wallB()
    floor = Floor()

    colliders = []

    colliders.append(wR)
    colliders.append(wL)
    colliders.append(wB)
    colliders.append(floor)

    for coll in colliders:
        coll.angle = np.random.uniform(low=-0.1, high=0.1)
        coll.center= (coll.center[0] + np.random.uniform(low=-.3, high=.3),
                      coll.center[1] + np.random.uniform(low=-.3, high=.3),
                      coll.center[2] + np.random.uniform(low=-.3, high=.3))

        coll.height = coll.height + np.random.uniform(low=-.3, high=.3)

    return colliders

def randomizer2(): #Left Turn
    wL = wallL()
    wL.width_x = 2
    wR = wallR()
    wB = wallB()
    floor = Floor()

    colliders = []

    colliders.append(wR)
    colliders.append(wL)
    colliders.append(wB)
    colliders.append(floor)

    for coll in colliders:
        coll.angle = np.random.uniform(low=-0.1, high=0.1)
        coll.center= (coll.center[0] + np.random.uniform(low=-.3, high=.3),
                      coll.center[1] + np.random.uniform(low=-.3, high=.3),
                      coll.center[2] + np.random.uniform(low=-.3, high=.3))

        coll.height = coll.height + np.random.uniform(low=-.3, high=.3)

    return colliders

def randomizer3(): #Right Turn
    wL = wallL()
    wR = wallR()
    wR.width_x = 2
    wB = wallB()
    floor = Floor()

    colliders = []

    colliders.append(wR)
    colliders.append(wL)
    colliders.append(wB)
    colliders.append(floor)

    for coll in colliders:
        coll.angle = np.random.uniform(low=-0.1, high=0.1)
        coll.center= (coll.center[0] + np.random.uniform(low=-.3, high=.3),
                      coll.center[1] + np.random.uniform(low=-.3, high=.3),
                      coll.center[2] + np.random.uniform(low=-.3, high=.3))

        coll.height = coll.height + np.random.uniform(low=-.3, high=.3)

    return colliders

def randSampler():
    wallFound = False

    for j in np.arange(0,9216,1) :
        x = 1
        y = np.random.uniform(low=-c_open, high=c_open)
        z = np.random.uniform(low=-c_open, high=c_open)

        range = -1
        if np.random.uniform(low=0, high=1) > 0.95:
            range = np.random.uniform(low=0, high=1)
        for t in np.arange (0,l_range,.1):
            point.x = 1*t
            point.y = y*t
            point.z = z*t
        #print(point.x)

            for coll in colliders:
                if coll.check_collition(point,t):

                    xs.append(point.x)
                    ys.append(point.y)
                    zs.append(point.z)
                    wallFound = True
                    break

            if wallFound:
                wallFound = False
                range = np.linalg.norm([point.x, point.y, point.z])/norma
                break

        dist.append(range)
    return dist

def sampler():
    wallFound = False

    #for j in np.arange(-c_open, c_open , .1 ):
    for j in np.linspace( -c_open, c_open, num=128):#128
        #x = 1
        #z = j

        for k in np.linspace(c_open, -c_open, num=72):#72
            #y = k

            range = -1
            if np.random.uniform(low=0, high=1) > 0.97:
                range = np.random.uniform(low=0, high=1)

            for t in np.arange (0,l_range,.05):
                point.x = 1*t
                point.y = j*t
                point.z = k*t
                #print(point.x)

                for coll in colliders:
                    if coll.check_collition(point,t):
                        #print(point.x)


                        xs.append(point.x)
                        ys.append(point.y)
                        zs.append(point.z)

                        wallFound = True

                        break


                if wallFound:
                    wallFound = False
                    range = np.linalg.norm([point.x, point.y, point.z])/norma
                    if np.random.uniform(low=0, high=1) > 0.98:
                        range = range + np.random.uniform(low=.05, high=.05)
                    break

            dist.append(range)
    #if np.amax(dist) > 0.2 :
    return dist
    #else:
    #   print("error")
    #   return False

#randSampler()
x_data0 = []
x_data1 = []
x_data2 = []
x_data3 = []
x_testdata =[]
x_testdata2 =[]

train_size = 1
test_size = 1

tic = time.time()
for g in np.arange(0,train_size,1):
    # colliders = randomizer0()
    # dist =[]
    # x_data0.append(sampler())

    # colliders = randomizer1()
    # dist =[]
    # x_data1.append(sampler())

    colliders = randomizer2()
    dist =[]
    x_data2.append(sampler())

    #colliders = randomizer3()
    #dist =[]
    #x_data3.append(sampler())

# for g in np.arange(0,test_size,1):
#     colliders = randomizer0()
#     dist =[]
#     x_testdata.append(sampler())

#     colliders = randomizer1()
#     dist =[]
#     x_testdata2.append(sampler())


tic = time.time() - tic

fig = plt.figure()
ax = fig.gca(projection='3d')
print(len(xs))

ax.set_xlim3d(-.1, 3)
ax.set_ylim3d(-1.5,1.5)
ax.set_zlim3d(-1.5,2.5)
ax.scatter(0,0,0, marker='X')
ax.scatter(xs, ys, zs, marker='o')

plt.show()

print(tic)
