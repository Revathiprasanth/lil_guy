from turtle import *
window=Screen()
window.bgcolor('#A5CF83')
window.addshape(r"C:\Users\USER\Downloads\lil_guy.gif")
window.tracer(0)  # Turns off auto-drawing so we control when to update

player=Turtle()
player.shape(r"C:\Users\USER\Downloads\lil_guy.gif")
player.penup()
player.speed(0)

block=Turtle()
block.shape('square')
block.color('#E89951')
block.penup()
block.shapesize(2,2)
block.goto(100,100)
block.speed(0)

def touch(a,b):
    distance=a.distance(b)
    if distance<40:
        return True
    return False
# --- Track which keys are held down ---
keys_held=set()

def press(key):
    keys_held.add(key)

def release(key):
    keys_held.discard(key)

# Tell the screen to call press/release when keys are pressed

window.listen()
window.onkeypress(lambda: press('w'),'w')
window.onkeypress(lambda: press('s'),'s')
window.onkeypress(lambda: press('a'),'a')
window.onkeypress(lambda: press('d'),'d')
window.onkeyrelease(lambda: release('w'),'w')
window.onkeyrelease(lambda: release('s'),'s')
window.onkeyrelease(lambda: release('a'),'a')
window.onkeyrelease(lambda: release('d'),'d')

speed=5

def game_loop():

    old_x=player.xcor()
    old_y=player.ycor()

    if 'w' in keys_held:
        player.sety(player.ycor()+speed)

    if 's' in keys_held:
        player.sety(player.ycor()-speed)
    if 'a' in keys_held:
        player.setx(player.xcor()-speed)
    if 'd' in keys_held:
        player.setx(player.xcor()+speed)

    if touch(player,block):
        player.goto(old_x,old_y)
        
    window.update()
    window.ontimer(game_loop,16)# runs game_loop every 16ms (about 60fps)

game_loop()

window.mainloop()
            
    




