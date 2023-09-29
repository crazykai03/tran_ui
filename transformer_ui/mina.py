# Import module
from tkinter import *
from PIL import ImageTk , Image
import threading
import time
lock_press_time =0
lock_hold= False
hold_time =0
lock_state = True
pre_function_time =0
rf_tran_data = ""


def uppress(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(up_btn, image = up_tap)

def uprelease(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(up_btn, image=up_normal)

def edgepress(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(light_edge, image = edge_light_tap)

def edgerelease(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(light_edge, image=edge_light_normal)
def stoppress(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(stop, image = stop_tap)

def stoprelease(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(stop, image=stop_normal)

def downpress(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(down, image = down_tap)

def downrelease(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(down, image=down_normal)
def edgebtnpress(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(light_btn, image = bottom_light_tap)

def edgebtnrelease(event):
    global pre_function_time
    pre_function_time = time.time()
    canvas1.itemconfig(light_btn, image=bottom_light_normal)

def lockpress(event):
    global  button1 ,lock_press_time , lock_hold , lock_state
    lock_hold = True
    canvas1.itemconfig(lock, image = lock_tap)
    lock_state = True
    lock_press_time= time.time()
def lockrelease(event):
    global btn1 , lock_press_time , lock_hold ,lock_state
    lock_hold = False
    print(time.time()-lock_press_time)
    if (lock_state==True):
        canvas1.itemconfig(lock, image=lock_normal)



def lock_all_btn():
    canvas1.itemconfig(up_btn, image=up_normal)
    canvas1.itemconfig(light_edge, image=edge_light_normal)
    canvas1.itemconfig(stop, image=stop_normal)
    canvas1.itemconfig(down, image=down_normal)
    canvas1.itemconfig(light_btn, image=bottom_light_normal)
    canvas1.itemconfig(lock, image=lock_normal)






def mylog():
    global  lock_press_time , lock_state , pre_function_time
    if (time.time() - lock_press_time >=2 and lock_hold==True):
        canvas1.itemconfig(lock, image=unllock_lock_tap)
        lock_state = False
        pre_function_time = time.time()
    elif (time.time() - pre_function_time >=30  and lock_state == False ):
        canvas1.itemconfig(lock, image=lock_normal)
        lock_state = True




    threading.Timer(1, mylog).start()


# Create object
root = Tk()

# Adjust size
root.geometry("800x480")

# Add image file
bg = PhotoImage(file="bgimg.png")
#oodles = PhotoImage(file="oodles.png")
up_normal= PhotoImage(file="up-default.png")
up_tap= PhotoImage(file="up-tap.png")
edge_light_normal= PhotoImage(file="edgeLight-default.png")
edge_light_tap= PhotoImage(file="edgeLight-tap.png")
stop_normal= PhotoImage(file="stop-default.png")
stop_tap= PhotoImage(file="stop-tap.png")
down_normal= PhotoImage(file="down-default.png")
down_tap= PhotoImage(file="down-tap.png")
bottom_light_normal= PhotoImage(file="bottomLight-default.png")
bottom_light_tap= PhotoImage(file="bottomLight-tap.png")
lock_normal= PhotoImage(file="lock-default.png")
lock_tap= PhotoImage(file="lock-tap.png")
unllock_lock_tap= PhotoImage(file="unlock-tap.png")





# Create Canvas
canvas1 = Canvas(root, width=800,
                 height=480,bd=0, highlightthickness=0 , bg="#2B2E35")

canvas1.pack(fill="both", expand=True)

# Display image
#canvas1.create_image(0, 0, image=bg,anchor="nw")






offset = 108



# Display Buttons
up_btn = canvas1.create_image(60+offset,16+offset,image=up_normal)
light_edge = canvas1.create_image(292+offset,16+offset,image=edge_light_normal)
stop = canvas1.create_image(524+offset,16+offset,image=stop_normal)
down = canvas1.create_image(60+offset,248+offset,image=down_normal)
light_btn  = canvas1.create_image(292+offset,248+offset,image=bottom_light_normal)
lock = canvas1.create_image(524+offset,248+offset,image=lock_normal)
#label_oodles=canvas1.create_image(150,70,image=oodles)


canvas1.tag_bind(up_btn,'<Button-1>', uppress)
canvas1.tag_bind(up_btn,'<ButtonRelease-1>', uprelease)
canvas1.tag_bind(light_edge,'<Button-1>', edgepress)
canvas1.tag_bind(light_edge,'<ButtonRelease-1>', edgerelease)
canvas1.tag_bind(stop,'<Button-1>', stoppress)
canvas1.tag_bind(stop,'<ButtonRelease-1>', stoprelease)
canvas1.tag_bind(down,'<Button-1>', downpress)
canvas1.tag_bind(down,'<ButtonRelease-1>', downrelease)
canvas1.tag_bind(light_btn,'<Button-1>', edgebtnpress)
canvas1.tag_bind(light_btn,'<ButtonRelease-1>', edgebtnrelease)
canvas1.tag_bind(lock,'<Button-1>', lockpress)
canvas1.tag_bind(lock,'<ButtonRelease-1>', lockrelease)







mylog()


# Execute tkinter
root.overrideredirect(True)

root.mainloop()