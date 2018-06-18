from pyleap import *

def draw(dt):
    Rectangle(0, 0, window.width, window.height, "white").draw()
    Line(100, 100, 300, 200, 1, '#eeaa00').draw()
    Line(100, 200, 300, 300, 2, 'red').draw()
    Line(100, 300, 300, 400, 4, '#00ff00').draw()
    Line(100, 400, 300, 100, 10, 'black').draw()

schedule_interval(draw)
run()
