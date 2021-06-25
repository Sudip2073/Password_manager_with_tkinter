#This is a password generator
import random
from tkinter import *

class assignment:
    
    def generate(self):
        self.Uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.Lowercase= self.Uppercase.lower()
        self.Digits='0123456789'
        self.Symbol="/*-+.?/;:\][{}&%$#@!"
        self.all=""
        # self.all= self.Uppercase+self.Lowercase+self.Digits+self.Symbol
        
        
        if self.var1.get() ==1:
            self.all+= self.Uppercase+self.Lowercase+self.Digits+self.Symbol
            print("all")

        if self.var2.get()== 1:
            self.all+= self.Uppercase
            print("Uppercase")

        if self.var3.get() ==1:
            self.all+= self.Lowercase
            print('Lower')

        if self.var4.get() == 1:
            self.all+= self.Digits
            print("digit")
        
        if self.var5.get() == 1:
            self.all+= self.Symbol
            print('symbol')
        
        self.length= int(self.entrylen.get())
        self.password= "".join(random.sample(self.all,self.length))
        print('Yes')
        self.entrypasswor.insert(0,self.password)
        print(self.password)
               
        # if any(self.exc.isupper() for self.exc in self.all) and any(self.exc.isdigit() for self.exc in self.all) and any(self.exc.lower() for self.exc in self.all):
        #     self.password= "".join(random.sample(self.all,self.length))
        #     print('Yes')
        #     self.entrypasswor.insert(0,self.password)
        #     print(self.password)
        # else:
        #     self.password= "".join(random.sample(self.all,self.length))
        #     self.entrypasswor.insert(0,"null")
        #     print('NO')
        #     print(self.password)


            
                
    
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
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()

        self.All = Checkbutton(self.frame, text='Use all',variable=self.var1, onvalue=1, offvalue=0 )
        self.All.grid(row=0, column=1, pady=10, padx=20)

        self.uppercase = Checkbutton(self.frame, text='Uppercase',variable=self.var2, onvalue=1, offvalue=0)
        self.uppercase.grid(row=0, column=2, pady=10, padx=20)

        self.lowercase = Checkbutton(self.frame, text='Lowercase', variable=self.var3, onvalue=1, offvalue=0)
        self.lowercase.grid(row=0, column=3, pady=10, padx=20)

        self.digit = Checkbutton(self.frame, text='Digit', variable=self.var4, onvalue=1, offvalue=0)
        self.digit.grid(row=1, column=1, pady=10, padx=20)

        self.symbols = Checkbutton(self.frame, text='Symbols', variable=self.var5, onvalue=1, offvalue=0)
        self.symbols.grid(row=1, column=3, pady=10, padx=20)
        

root = Tk()
root.title("!!!!Password_generator!!!!")
root.geometry('680x400')
root.resizable(0,0)
abc = assignment(root)
root.mainloop()

