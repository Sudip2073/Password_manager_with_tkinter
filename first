#This is a password generator
import random
from tkinter import *
from tkinter import ttk


class assignment:
    
    def generate(self):
        self.Uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.Lowercase= self.Uppercase.lower()
        self.Digits='0123456789'
        self.Symbol="/*-+.?/;:\][{}&%$#@!"
        self.all=""
        # self.all= self.Uppercase+self.Lowercase+self.Digits+self.Symbol
        
        
        if self.var.get() =="all":
            self.all+= self.Uppercase+self.Lowercase+self.Digits+self.Symbol
            print("all")

        if self.var.get()== "Upper":
            self.all+= self.Uppercase
            print("Uppercase")

        if self.var.get() =="Lower":
            self.all+= self.Lowercase
            print('Lower')

        if self.var.get() == "Digit":
            self.all+= self.Digits
            print("digit")
        
        if self.var.get() == "Symbols":
            self.all+= self.Symbol
            print('symbol')
        
        self.length= int(self.entrylen.get())
               
        if any(self.exc.isupper() for self.exc in self.all) and any(self.exc.isdigit() for self.exc in self.all) and any(self.exc.isdigit() for self.exc in self.all):
            self.password= "".join(random.sample(self.all,self.length))
            print('Yes')
            self.entrypasswor.insert(0,self.password)
        else:
                self.entrypasswor.insert(0,"null")
                print('NO')
                

        

    
    def __init__(self, root):
        self.root = root
        # ==============Button frame=========
        self.frame = Frame(self.root, bd=4,  relief=RIDGE)
        self.frame.place(x=20, y=30, width=630, height=300)

        self.options = Label(self.frame, text='Options =>',font='times 12 bold italic').grid(row=0, column=0, padx=15, pady=15)
        
        self.len= Label(self.frame, text='Length of password =>',font='times 12 bold italic').grid(row=3, column=0, padx=15, pady=15)
        self.entrylen= Entry(self.frame, font='times 12 bold italic',width=15)
        self.entrylen.grid(row=3, column=1, padx=15, pady=15)
        
        self.passw= Label(self.frame, text='Your password =>',font='times 12 bold italic').grid(row=5, column=0, padx=15, pady=15)
        self.entrypasswor= Entry(self.frame,font='times 12 bold italic',width=15)
        self.entrypasswor.grid(row=5, column=1, padx=15, pady=15)

        self.button = Button(self.frame, text='Generate',font='times 12 bold italic', command= self.generate, width=10, height=1).grid(row=4,column=0)
        #==========options=========
        self.var = StringVar()
    
        self.All = ttk.Radiobutton(self.frame, text='Use all',variable=self.var, value='all' )
        self.All.grid(row=0, column=1, pady=10, padx=20)

        self.uppercase = ttk.Radiobutton(self.frame, text='Uppercase',variable=self.var, value='Upper')
        self.uppercase.grid(row=0, column=2, pady=10, padx=20)

        self.lowercase = ttk.Radiobutton(self.frame, text='Lowercase', variable=self.var, value="Lower")
        self.lowercase.grid(row=0, column=3, pady=10, padx=20)

        self.digit = ttk.Radiobutton(self.frame, text='Digit', variable=self.var, value="Digit")
        self.digit.grid(row=1, column=1, pady=10, padx=20)

        self.symbols = ttk.Radiobutton(self.frame, text='Symbols', variable=self.var, value="Symbols")
        self.symbols.grid(row=1, column=3, pady=10, padx=20)
        

root = Tk()
root.title("!!!!Password_generator!!!!")
root.geometry('680x400')
root.resizable(0,0)
abc = assignment(root)
root.mainloop()

