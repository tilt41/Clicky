import win32api, win32con, sys


mode = sys.argv[1]  #Tells what mode you want to use
clicks = int(sys.argv[2]) #Tells the numbers of clicks 
clickct = 0
levelct = 0

def click(x,y): 
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

if mode == '-r': # This mode will click in only one location 
	for _ in range(clicks):
		clickct = clickct + 1
		click(1300,405) #Coordinates of screen
		print clickct
elif mode == '-L': # This mode will click in one location and every 100 clicks it will click a different location 
	for _ in range(clicks):
		clickct = clickct + 1
		levelct += 1
		click(1305,351) #Coordinates of screen
		if (levelct == 100):
			click(1375,75) #Coordinates of screen
			levelct = 0
		print clickct
else:
	print "Use -r or -L for mode"
