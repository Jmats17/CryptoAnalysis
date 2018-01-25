from Tkinter import *

root = Tk()
root.geometry('250x250')
theLabel = Label(root, text="Cryptocurrency Analysis")
theLabel.pack()

'''topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)'''


nLabel = Label(root, text='Enter Crypto Name')
nLabel.pack()
nEntry = Entry(root)
nEntry.pack()
tickerLabel = Label(root, text='Enter Ticker Symbol')
tickerLabel.pack()
tickerEntry = Entry(root)
tickerEntry.pack()

button1 = Button(text='Analyze')
button1.pack()


root.mainloop()
