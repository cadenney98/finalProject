from tkinter import *

root = Tk()

def pressZero() :
    first = first+"0"
    result = Label(root, text=str(first))
    result.grid(row="0",column="1")
def pressOne() :
    first = first+"1"
    result = Label(root, text=str(first))
    result.grid(row="0",column="1")
def pressTwo() :
    first = first+"2"
    result = Label(root, text=str(first))
    result.grid(row="0",column="1")
def pressThree() :
    first = first+"3"
    result = Label(root, text=str(first))
    result.grid(row="0",column="1")
def pressFour() :
    first = first+"4"
    result = Label(root, text=str(first))
    result.grid(row="0",column="1")
def pressFive() :
    first = first+"5"
    result = Label(root, text=str(first))
    result.grid(row="0",column="1")
def pressSix() :
    first = first+"6"
    result = Label(root, text=str(first))
    result.grid(row="0",column="1")
def pressSeven() :
    first = first+"7"
    result = Label(root, text=str(first))
    result.grid(row="0",column="1")
def pressEight() :
    first = first+"8"
    result = Label(root, text=str(first))
    result.grid(row="0",column="1")
def pressNine() :
    first = first+"9"
    result = Label(root, text=str(first))
    result.grid(row="0",column="1")

signedButton = Button(root, text="+/-", padx="5",pady="5")
sevenButton = Button(root, text="7", padx="10",pady="10",command=pressSeven) 
eightButton = Button(root, text="8", padx="10",pady="10",command=pressEight)
nineButton = Button(root, text="9", padx="10",pady="10",command=pressNine)
fourButton = Button(root, text="4", padx="10",pady="10",command=pressFour)
fiveButton = Button(root, text="5", padx="10",pady="10",command=pressFive)
sixButton = Button(root, text="6", padx="10",pady="10",command=pressSix)
oneButton = Button(root, text="1", padx="10",pady="10",command=pressOne)
twoButton = Button(root, text="2", padx="10",pady="10",command=pressTwo)
threeButton = Button(root, text="3", padx="10",pady="10",command=pressThree)
zeroButton = Button(root, text="0", padx="10",pady="10",command=pressZero)

signedButton.grid(row="0",column="0")
sevenButton.grid(row="1",column="0")
eightButton.grid(row="1",column="1")
nineButton.grid(row="1",column="2")
fourButton.grid(row="2",column="0")
fiveButton.grid(row="2",column="1")
sixButton.grid(row="2",column="2")
oneButton.grid(row="3",column="0")
twoButton.grid(row="3",column="1")
threeButton.grid(row="3",column="2")
zeroButton.grid(row="4",column="0")

first="0"

root.mainloop()
