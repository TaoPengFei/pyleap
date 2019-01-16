from pyleap import *

window.set_size(600, 600)

t1 = Polygon(200, 100, 400, 100, 350, 300, 250, 300, "gray")
t2 = Polygon(300, 200, 500, 200, 450, 500, 350, 500, 200, 600, "yellow")

star = Polygon(175, 300, 250, 100, 50, 225, 275, 225, 75, 100, "#ff000080")
star.opacity = 0.5

print(star.color)

def Loop(dt):
    window.clear()

    t1.draw()
    t2.rotation += 1
    t2.draw()

    p = t2.collide(t1)
    if p:
        Point(p.x, p.y, color="red", point_size=5).draw()

    star.x += 1
    star.y += 1
    star.draw()

repeat(Loop)

run()