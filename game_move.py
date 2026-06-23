from turtle import *

window=Screen()
window.title('Cool move thing')
window.bgcolor('#0A2947')

player=Turtle()
player.shape('turtle')
player.color('#F3E4C9')
player.shapesize(stretch_wid=4, stretch_len=4)
player.penup()

#move thing up , down , left , right
def up():
    y = player.ycor()#get where thing is
    player.sety(y+20)#move thing up

def down():
    y = player.ycor()
    player.sety(y-20)

def left():
    x = player.xcor()
    player.setx(x-20)

def right():
    x = player.xcor()
    player.setx(x+20)

window.listen()
window.onkey(up,'w')
window.onkey(down,'s')
window.onkey(left,'a')
window.onkey(right,'d')

window.mainloop()

    
    
