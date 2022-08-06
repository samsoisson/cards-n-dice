from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("UI on python")
#button
'''
def myClick():
    myLabel = Label(root,text="Hello "+e.get())
    myLabel.pack()

myButton = Button(root,text="Click",command=myClick,fg="blue",bg="red")
myButton.pack()

#text input
e= Entry(root,width=50,bg="cyan",fg="#000000",borderwidth=5)
e.pack()
e.insert(0,"Enter your name")
'''

#calculator
'''
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)
def button_add():
    first = e.get()
    global f_num
    f_num = int(first)
    e.delete(0,END)
def button_equal():
    second = e.get()
    e.delete(0,END)
    e.insert(0,f_num+int(second))

button1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
buttonadd = Button(root,text="+",padx=39,pady=20,command=lambda: button_add())
buttonequal = Button(root,text="=",padx=91,pady=20,command=lambda: button_equal())
buttonclear = Button(root,text="Clear",padx=79,pady=20,command=lambda: button_clear())

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
button0.grid(row=4,column=0)
button0.grid(row=4,column=0)
buttonclear.grid(row=4,column=1,columnspan=2)
buttonadd.grid(row=5,column=0)
buttonequal.grid(row=5,column=1,columnspan=2)
'''
#root.iconbitmap('c:/Python Stuff/picture.ico') ICON
img = ImageTk.PhotoImage(Image.open('portrait.png'))
label = Label(image=img,width=230,height=230,pady=20)
status = Label(root,text='Score:'+str(69),bd=1,relief=SUNKEN,fg="red",anchor=N)
label.pack(pady=10)
status.pack()
root.mainloop()