import pyautogui
from tkinter import *

GUI = Tk()
GUI.title("Mouse Locator")
GUI.geometry("300x130")

# Window always on top
GUI.wm_attributes("-topmost", 1)

ML_welcome = Label(GUI, text="Mouse Locator", font=("Courier", 14, "bold"))
ML_welcome.pack(pady=10, padx=60)

position_text = Entry(GUI, font=("Courier", 12))
position_text.pack(pady=2)

colour_text = Entry(GUI, font=("Courier", 12))
colour_text.pack(pady=2)

def update():
	# Updating mouse position "X: 0 Y: 0"
	position_text.delete(0, END)
	x, y = pyautogui.position()
	positionStr = 'X: ' + str(x) + ' Y: ' + str(y)
	position_text.insert(0, positionStr)
	# Select the text to be able to copy it.
	position_text.select_range(0, END)

	# Updating pixel colours "(r, g, b)"
	colour_text.delete(0, END)
	pix = pyautogui.pixel(x, y)
	positionStr2 = str(pix)
	colour_text.insert(0, positionStr2)
	# Select the text to be able to copy it.
	colour_text.select_range(0, END)

	# Update the information - Default: 10 ms
	position_text.after(10, update)


update()

GUI.mainloop()
