from tkinter import *
# from tkinter import as Tkinter
import time

# Our GUI is defined here
root = Tk()  # best to use root so you have menus!
root.title("Demo Stopwatch");
f = Frame(root); # f for frame!
f.pack(anchor = 'center', pady = 5);
root.minsize(width=260, height=80);
# root.geometry("200x300");
 
stop_start = False; # we haven't started yet

def btnstop():
    global stop_start
    stopBtn['state'] = 'disabled' # disable the stop button once clicked
    startBtn['state'] = 'normal'  # on click start button should be available
    stop_start = False # stopwatch is paused
 
def btnstart():
    global stop_start
    
    stop_start = True # stopwatch is running
    oldtime = time.time() # get current timestamp includes milisecs
    
    # initialising values for minutes and hours
    mins = 0; hrs = 0;
    not_Sixty = 0; not_Sixty_mins = 0;
    minsReplacer = ""; secsReplacer = "";
    
    # we need to be in a loop to be able to count up or down, here up
    while (stop_start):
        root.update() # update the GUI
        secs = time.time() - oldtime # constantly display new remains seconds
        
        startBtn['state'] = 'disabled' # on click stop button should be available
        stopBtn['state'] = 'normal' # disable the start button once clicked
    
        # setting some values to start
        cur_secs = secs - not_Sixty;
        cur_mins = mins - not_Sixty_mins;
 
        # operations to display 0 or 00 
        if cur_secs < 10:
            secsReplacer = "0"
        else:
            secsReplacer = ""
 
        if mins < 10:
            minsReplacer = ""
        else:
            minsReplacer = ""
 
        # timer counting operations
        if cur_mins == 60:
            not_Sixty_mins += 60
            hrs += 1
 
        if cur_secs > 60:
            not_Sixty += 60
            mins += 1

        # label displays current time elapsed
        t_Start.config(text = str(hrs) + ":" + minsReplacer +
                       str(cur_mins) + ":" + secsReplacer +
                       str(round(cur_secs, 1)));

# label creation to displayed whatever we want at the start
"""Pack packs widgets in rows or columns. We can use options like fill,
 expand, and side to control this geometry manager."""
t_Start = Label(f, text = "00:00:00", font = ('Comic Sans MS', 20, 'bold')); t_Start.pack();

# buttons creation
startBtn = Button(f, text = "Start",
                  width = 6, font = ('Comic Sans MS', 10, 'bold'),
                  command = lambda: btnstart()); startBtn.pack(side = "left");
stopBtn = Button(f, text = "Stop",
                 width = 6, state = 'disabled',
                 font = ('Comic Sans MS', 10, 'bold'),
                 command = btnstop); stopBtn.pack(side = "left");
quitBtn = Button(f, text = "Quit",
                 width = 6,
                 font = ('Comic Sans MS', 10, 'bold'),
                 command = root.destroy); quitBtn.pack(side = "left");

# run the GUI App
root.mainloop()