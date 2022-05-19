from tkinter.filedialog import askopenfile
import database as d
from tkVideoPlayer import TkinterVideo
import tkinter as Tk

import b 
import time

window = Tk.Tk()
window.title("Junction")
window.geometry("1920x1080")
window.configure(bg="green")

"""
def open_file():
    file = askopenfile(mode='r', filetypes=[
                       ('Video Files', ["*.mp4"])])
    if file is not None:
        global filename
        filename = file.name
        global videoplayer
        videoplayer = TkinterVideo(master=window, scaled=True, pre_load=False)
        videoplayer.load(r"{}".format(filename))
        #videoplayer.pack(expand=True, fill="both")
        #videoplayer.grid(row = 2, column = 2, pady = 2,width=30)
        videoplayer.place( height=200, width=300 , x=100,y=100)
        videoplayer.play()
 
 
 
def playAgain():
    print(filename)
    videoplayer.play()
 
def StopVideo():
    print(filename)
    videoplayer.stop()
 
def PauseVideo():
    print(filename)
    videoplayer.pause()
    
 
# center this label
lbl1 = Tk.Label(window, text="Tkinter Video Player", bg="orange red",
             fg="white", font="none 24 bold")
lbl1.config(anchor=Tk.CENTER)
lbl1.pack()
#lbl1.grid(row = 0, column = 10, pady = 2,sticky='E')
 
openbtn = Tk.Button(window, text='Open', command=lambda: open_file())
openbtn.pack(side=Tk.TOP, pady=2)
 
playbtn = Tk.Button(window, text='Play Video', command=lambda: playAgain())
playbtn.pack(side=Tk.TOP, pady=3)
 
stopbtn = Tk.Button(window, text='Stop Video', command=lambda: StopVideo())
stopbtn.pack(side=Tk.TOP, padx=4)
 
pausebtn = Tk.Button(window, text='Pause Video', command=lambda: PauseVideo())
pausebtn.pack(side=Tk.TOP, padx=5)

"""
lbl1 = Tk.Label(window, text="Traffic management System", bg="orange red",
             fg="white", font="none 16 bold")
#lbl1.config(anchor=Tk.E)
#lbl1.pack()
lbl1.place(x=760,y=440)
 
startall = Tk.Button(window, text='Play', command=lambda: start())
#open1.pack(side=Tk.TOP, pady=2)
startall.place(x=10,y=10)

stopall = Tk.Button(window, text='Calculate ', command=lambda: junction())
#open1.pack(side=Tk.TOP, pady=2)
stopall.place(x=10,y=60)

printall = Tk.Button(window, text='Display database ', command=lambda: d.printall())
#open1.pack(side=Tk.TOP, pady=2)
printall.place(x=10,y=110)



open1 = Tk.Button(window, text='Open', command=lambda: open_1())
#open1.pack(side=Tk.TOP, pady=2)
open1.place(x=650,y=150)

open2 = Tk.Button(window, text='Open', command=lambda: open_2())
open2.place(x=220,y=300)

open3 = Tk.Button(window, text='Open', command=lambda: open_3())
open3.place(x=650,y=820)

open4 = Tk.Button(window, text='open', command=lambda: open_4())
open4.place(x=1650,y=300)

#open5 = Tk.Button(window, text='Open image clear', command=lambda: open_img_c())
#open5.place(x=580,y=370)
frame_1 = Tk.Frame(window, bg='#c4ffd2', width=50, height=50)
frame_1.place(x=1170,y=150)
label_1 = Tk.Label(frame_1, text='Number of vehicle/Timer')
label_1.pack(side=Tk.LEFT,expand=False)
text1 = Tk.Text(frame_1, height=1,width=15)
text1.pack(side=Tk.LEFT,expand=False)
#text1.config(state='normal')
text1_2 = Tk.Text(frame_1, height=1,width=5)
text1_2.pack(side=Tk.BOTTOM,expand=False)

frame_2 = Tk.Frame(window, bg='#c4ffd2', width=50, height=50)
frame_2.place(x=30,y=705)
label_2 = Tk.Label(frame_2, text='Number of vehicle/Timer')
label_2.pack(side=Tk.LEFT)
text2 = Tk.Text(frame_2, height=1,width=15)
text2.pack(side=Tk.LEFT)
text2.config(state='normal')
text2_2 = Tk.Text(frame_2, height=1,width=5)
text2_2.pack(side=Tk.BOTTOM,expand=False)


frame_3 = Tk.Frame(window, bg='#c4ffd2', width=50, height=50)
frame_3.place(x=1170,y=820)
label_3 = Tk.Label(frame_3, text='Number of vehicle/Timer')
label_3.pack(side=Tk.LEFT)
text3 = Tk.Text(frame_3, height=1,width=15)
text3.pack(side=Tk.LEFT)
text3.config(state='normal')
text3_2 = Tk.Text(frame_3, height=1,width=5)
text3_2.pack(side=Tk.BOTTOM,expand=False)

frame_4 = Tk.Frame(window, bg='#c4ffd2', width=50, height=50)
frame_4.place(x=1450,y=700)
label_4 = Tk.Label(frame_4, text='Number of vehicle/Timer')
label_4.pack(side=Tk.LEFT)
text4 = Tk.Text(frame_4, height=1,width=15)
text4.pack(side=Tk.LEFT)
text4.config(state='normal')
text4_2 = Tk.Text(frame_4, height=1,width=5)
text4_2.pack(side=Tk.BOTTOM,expand=False)

def open_1():
    file = askopenfile(mode='r', filetypes=[
                       ('Video Files', ["*.mp4"])])
    if file is not None:
        #global filename
        filename = file.name
        global videoplayer1
        videoplayer1 = TkinterVideo(master=window, scaled=True, pre_load=False)
        videoplayer1.load(r"{}".format(filename))
        #videoplayer.pack(expand=True, fill="both")
        #videoplayer.grid(row = 2, column = 2, pady = 2,width=30)
        videoplayer1.place( height=300, width=400 , x=760,y=10)
        


def open_2():
    file = askopenfile(mode='r', filetypes=[
                       ('Video Files', ["*.mp4"])])
    if file is not None:
        filename = file.name
        global videoplayer2
        videoplayer2 = TkinterVideo(master=window, scaled=True, pre_load=False)
        videoplayer2.load(r"{}".format(filename))
        #videoplayer.pack(expand=True, fill="both")
        #videoplayer.grid(row = 2, column = 2, pady = 2,width=30)
        videoplayer2.place( height=300, width=400 , x=50,y=365)
        

def open_3():
    file = askopenfile(mode='r', filetypes=[
                       ('Video Files', ["*.mp4"])])
    if file is not None:
        filename = file.name
        global videoplayer3
        videoplayer3 = TkinterVideo(master=window, scaled=True, pre_load=False)
        videoplayer3.load(r"{}".format(filename))
        #videoplayer.pack(expand=True, fill="both")
        #videoplayer.grid(row = 2, column = 2, pady = 2,width=30)
        videoplayer3.place( height=300, width=400 , x=760,y=660)
        

def open_4():
    file = askopenfile(mode='r', filetypes=[
                       ('Video Files', ["*.mp4"])])
    if file is not None:
        filename = file.name
        global videoplayer4
        videoplayer4 = TkinterVideo(master=window, scaled=True, pre_load=False)
        videoplayer4.load(r"{}".format(filename))
        #videoplayer.pack(expand=True, fill="both")
        #videoplayer.grid(row = 2, column = 2, pady = 2,width=30)
        videoplayer4.place( height=300, width=400 , x=1450,y=365)
        
def start():
    videoplayer1.play()
    videoplayer2.play()
    videoplayer3.play()
    videoplayer4.play()
    




"""
def open_img_c():
    img = ImageTk.PhotoImage(file=r"clear.png")
    labels=ImageTk.Label(window, image=img)
    #label=Label(TK, image=img)
    labels.place(x=760,y=440,height=200,width=200)
    """


def junction():
     #while True :
        #phase 1
        c=b.send(775,70, 400, 300)
        
        #text1.insert('1.0', c)
        text1.delete(1.0,'end')   
        text1.insert(Tk.INSERT, c[:5])
        text1_2.delete(1.0,'end')   
        text1_2.insert(Tk.INSERT, c[5])
       # if c[5]!=0:
        #time.sleep(3)
        l=1
        d.insert_data(c,l)    


        
        c=b.send(65,415, 400, 300)
        
        #text1.insert('1.0', c)
        text2.delete(1.0,'end')   
        text2.insert(Tk.INSERT, c[:5])
        text2_2.delete(1.0,'end')   
        text2_2.insert(Tk.INSERT, c[5])
        #if c[5]!=0:
        #.sleep(3)
        l=2
        d.insert_data(c,l) 


        c=b.send(775,720, 400, 300)
        
        #text1.insert('1.0', c)
        text3.delete(1.0,'end')   
        text3.insert(Tk.INSERT, c[:5])
        text3_2.delete(1.0,'end')   
        text3_2.insert(Tk.INSERT, c[5])
        #if c[5]!=0:
        #.sleep(3)
        l=3
        d.insert_data(c,l) 


        c=b.send(1465,425, 400, 300)
        
        #text1.insert('1.0', c)
        text4.delete(1.0,'end')   
        text4.insert(Tk.INSERT, c[:5])
        text4_2.delete(1.0,'end')   
        text4_2.insert(Tk.INSERT, c[5])
        #if c[5]!=0:
        time.sleep(3)
        #junction()
        l=4
        d.insert_data(c,l) 


window.mainloop()