from tkinter import *

root = Tk()

class MyLabel:
    def __init__(self, text):
#        self.text = input("Label contents: ")
        self.text = text
        self.main = Label(root, text=self.text)

#    def place(self):
    def place(self, row, col):
        place = self.main
#        row = input("Row: ")
#        col = input("Column: ")
        place.grid(row=row,column=col)


new_button = MyLabel("New Button")
new_button.place(3,1)



# creating a label widget
myLabel1 = Label(root, text="Hello World! This is my text box that I can say everything I want to in the world")
myLabel2 = Label(root, text="My name is Dane")
myLabel3 = Label(root, text=" ")


# putting it onto the screen
#myLabel.pack()
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=2)
myLabel3.grid(row=1,column=1)


# for widgets all you need to do is define it then pack it

root.mainloop()
