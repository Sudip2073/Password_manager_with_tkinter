#This is a password generator
import random
from tkinter import *
import pyperclip
from tkinter import ttk



class assignment:
    def Copy(self):
        pyperclip.copy(self.entrypasswor.get())

    def generate(self):
        self.Uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.Lowercase= self.Uppercase.lower()
        self.Digits='0123456789'
        self.Symbol="/*-+.?/;:\][{}&%$#@!"
        self.all=""
        # self.all= self.Uppercase+self.Lowercase+self.Digits+self.Symbol
        
        
        if self.var1.get() ==1:
            self.all+= self.Uppercase+self.Lowercase+self.Digits+self.Symbol
            #print("all")

        if self.var2.get()== 1:
            self.all+= self.Uppercase
            #print("Uppercase")

        if self.var3.get() ==1:
            self.all+= self.Lowercase
            #print('Lower')

        if self.var4.get() == 1:
            self.all+= self.Digits
            #print("digit")
        
        if self.var5.get() == 1:
            self.all+= self.Symbol
            #print('symbol')
        else:
            self.entrypasswor.delete(0,END)
            self.entrypasswor.insert(0,"Invalid option")
        self.all=self.all*3
        self.length= (self.ab.get())
        # self.password= "".join(random.sample(self.all,self.length))
        
        # self.entrypasswor.insert(0,self.password)
              
        if any(self.exc.isupper() for self.exc in self.all) and any(self.exc.isdigit() for self.exc in self.all) and any(self.exc.lower() for self.exc in self.all):
            self.password= "".join(random.sample(self.all,self.length))
            print('Yes')
            self.entrypasswor.delete(0,END)
            self.entrypasswor.insert(0,self.password)
            print(self.password)
        else:
            self.password= "".join(random.sample(self.all,self.length))
            self.entrypasswor.delete(0,END)
            self.entrypasswor.insert(0,"Weak Password Combination")
            print('NO')
            print(self.password)

    
    def print_value(self,val):
        #print (val)
        self.value.config(text=val)
    
    def __init__(self, root):
        self.root = root

        #=====logo========
        self.canvas =Canvas(self.root,width=500, height=500)
        self.canvas.pack()
        self.logo= PhotoImage(file= 'D:\\King1\\Desktop\\New folder\\Passgen.png')
        self.canvas.create_image(0,0,anchor='nw', image= self.logo)


        # ==============Button frame=========
        self.frame = Frame(self.root, bd=2 , relief=RIDGE)
        self.frame.place(x=30, y=470, width=650, height=230)

        self.options = Label(self.frame, text='Options =>',font='times 12 bold italic').grid(row=0, column=0, padx=15, pady=15)
        
        self.len= Label(self.frame, text='Length of password =>',font='times 12 bold italic').place(x=10, y=110)
        # self.entrylen= Entry(self.frame, font='times 12 bold italic',width=15)
        # self.entrylen.grid(row=3, column=1, padx=15, pady=15)
            

        self.passw= Label(self.frame, text='Your password =>',font='times 12 bold italic').place(x=10, y=160)
        self.entrypasswor= Entry(self.frame,font='times 12 bold italic',width=25)
        self.entrypasswor.place(x=150, y=160)

        self.button = Button(self.frame, text='Generate',font='times 12 bold italic', command= self.generate, width=10, height=1).place(x=430, y=110)
        self.copy = Button(self.frame, text='Copy',font='times 12 bold italic', command= self.Copy, width=10, height=1).place(x=430, y=155)
        #==========options=========
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.ab=IntVar()

        self.All = Checkbutton(self.frame,font='times 12 bold italic', text='Use all',variable=self.var1, onvalue=1, offvalue=0 )
        self.All.place(x=200, y=15)

        self.uppercase = Checkbutton(self.frame,font='times 12 bold italic', text='Uppercase',variable=self.var2, onvalue=1, offvalue=0)
        self.uppercase.place(x=350, y=15)

        self.lowercase = Checkbutton(self.frame,font='times 12 bold italic', text='Lowercase', variable=self.var3, onvalue=1, offvalue=0)
        self.lowercase.place(x=500, y=15)

        self.digit = Checkbutton(self.frame,font='times 12 bold italic', text='Digit', variable=self.var4, onvalue=1, offvalue=0)
        self.digit.place(x=275, y=60)

        self.symbols = Checkbutton(self.frame,font='times 12 bold italic', text='Symbols', variable=self.var5, onvalue=1, offvalue=0)
        self.symbols.place(x=475, y=60)
        
    
        #=============slider and it's value=======
        self.slider = ttk.Scale(self.frame, from_=0, to=128,  orient='horizontal', variable=self.ab, command=self.print_value).place(x=180, y=110)
        
        self.value = Label(self.frame,text="" ,font='times 12 bold italic')
        self.value.place(x=290, y=110)


        
                


root = Tk()
root.title("!!!!Password_generator!!!!")
root.geometry('710x720')
root.resizable(0,0)
abc = assignment(root)
root.mainloop()

