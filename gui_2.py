from Tkinter import Tk,PhotoImage,Button,LEFT,mainloop
from time import sleep, strftime, time
import tkFont
import logging
import tkMessageBox

STOCK_HEADSETS = 1
STOCK_MOUSES = 1
STOCK_KEYBOARDS = 1
STOCK_CABLES = 1
DOOR_HEADSETS = 1
DOOR_MOUSES = 2
DOOR_KEYBOARDS = 3
DOOR_CABLES = 4

def end_fullscreen(self, event=None):
	win.state = False
	win.attributes("-fullscreen", False)
	win.geometry("200x200")
	return "break"

logging.basicConfig(filename='logfile.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
win = Tk()
win.attributes("-fullscreen", True)
win.bind("<Escape>", end_fullscreen)
myFont = tkFont.Font(family = 'Helvetica', size = 24, weight = 'bold')

#python don't have switch or case
def decrement_stock(num_door):
	global STOCK_HEADSETS
	global STOCK_MOUSES
	global STOCK_KEYBOARDS
	global STOCK_CABLES
	if num_door == DOOR_HEADSETS:
		STOCK_HEADSETS -= 1
		if STOCK_HEADSETS == 0:
			headsetButton.config(state="disabled")
	elif num_door == DOOR_MOUSES:
		STOCK_MOUSES -= 1
		if STOCK_MOUSES == 0:
			mouseButton.config(state="disabled")
	elif num_door == DOOR_KEYBOARDS:
		STOCK_KEYBOARDS -= 1
		if STOCK_KEYBOARDS == 0:
			keyboardButton.config(state="disabled")
	elif num_door == DOOR_KEYBOARDS:
		STOCK_CABLES -= 1
		if STOCK_CABLES == 0:
			cableButton.config(state="disabled")
	else:
		print("There door is not ")
	

def remove_devise(username, call, num_door):
	print(call + " button pressed")
	logging.info(call + " button pressed")
	result = tkMessageBox.askyesno(call,"Do you want a new " + call + "?")
	print(result)
	if result:
		decrement_stock(num_door)
		logging.info("A " + call + " was getting by " + username + ".")
	else: 
		logging.info(call + " cancel.")

def headset():
	remove_devise("bpump","Headset",1)

def mouse():
	remove_devise("bpump","Mouse",2)

def keyboard():
	remove_devise("bpump","Keyboard",3)

def cable():
	remove_devise("bpump","Cable",4)

def exitProgram():
	print("Exit Button pressed")
	logging.info('Exit Button pressed.')        
	win.quit()

#win.title("First GUI")
#win.geometry('800x480')
logging.info('Starting...')

#exitButton  = Button(win, text = "EXIT", font = myFont, command = exitProgram, height =2 , width = 6) 
#exitButton.pack(side = BOTTOM)

imgheadset=PhotoImage(file=r"C:\Users\fernando.diaz\Documents\IoT\Icons\headsetgif.gif")
headsetButton = Button(win, image=imgheadset,text = "HEADSET", font = myFont, command = headset, height =200 , width = 200)
#, state=DISABLED
headsetButton.pack(side=LEFT)

imgmouse=PhotoImage(file=r"C:\Users\fernando.diaz\Documents\IoT\Icons\mousegif.gif")
mouseButton = Button(win,image=imgmouse, text = "MOUSE", font = myFont, command = mouse, height =200 , width = 200)
mouseButton.pack(side = LEFT)

imgkeyboard=PhotoImage(file=r"C:\Users\fernando.diaz\Documents\IoT\Icons\keyboardgif.gif")
keyboardButton = Button(win,image=imgkeyboard, text = "KEYBOARD", font = myFont, command = keyboard, height =200 , width = 200)
keyboardButton.pack(side = LEFT)

imgcable=PhotoImage(file=r"C:\Users\fernando.diaz\Documents\IoT\Icons\cablegif.gif")
cableButton = Button(win,image=imgcable, text = "CABLE", font = myFont, command = cable, height =200 , width = 200)
cableButton.pack(side = LEFT)


try:
    win.mainloop()
finally:
	print("Close Button pressed")
	logging.info('Close Button pressed.')        
	win.quit()

