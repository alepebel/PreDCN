
# Experiment instructions

inst = visual.TextStim(win, pos=[0,0], height = 1.2)
inst.setHeight = 0.15
inst.wrapWidth = 20
inst.text = "En este experimento te presentaré una sequencia rápida de estimulos con diferentes orientaciones... "

inst.draw()
win.flip()

event.waitKeys()

inst.text = "Tu tarea es estimar si la media de estimulos presentados esta mas orientado en los ejes cardinales (vertical u horizonal) pulsando "
inst.pos=[0,5]
lineh.ori = 0
linev.ori = 0
linev.draw()
lineh.draw()
inst.draw()
circle.draw()
win.flip()
event.waitKeys(keyList = ["m"])

inst.text = "... o en los ejes diagonales (diagonal derecha o diagonal izquierda)"
inst.pos=[0,3]
lineh.ori = 45
linev.ori = 45
linev.draw()
lineh.draw()
inst.draw()
circle.draw()
win.flip()
event.waitKeys(keyList = ["z"])


win.flip()
event.waitKeys()

#pause until there's a keypress
event.waitKeys()

message2.draw()
text = "Pulsa la barra espaciadora para practicar un ejemplo")
