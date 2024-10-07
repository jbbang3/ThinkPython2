import math

class Point:
    """Represent a point in 2D spcae"""

def print_point(p):
    print(p.x)
    print("{}, {}".format(p.x, p.y))

def distance_between_points(p1,p2):
    return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

class Rectangle:
    """Represents a rectangle"""

def find_center(rect):
    p=Point()
    p.x=rect.corner.x + rect.width/2
    p.y-rect.corner.y + rect.height/2
    return p

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

class Circle:
    """ represents a circle"""

def point_in_circle(c,p):
    return distance_between_points(c.center,p) < c.radius

def main():
    blank=Point()
    blank.x=1
    blank.y=4
    print_point(blank)
    print('s')

    c=Circle()
    c.radius=75
    c.center=Point()
    c.center.x=150
    c.center.y=100
    print(point_in_circle(c,blank))






if __name__=="__main__":
    main()