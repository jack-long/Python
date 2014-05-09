from Tkinter import *

class Calculater(object):
    '''A Simple calulater GUI using OOP'''
    def __init__(self, window):
        # The model.
        self.text = StringVar()
        self.text.set(u"")
        self.number = StringVar()
        self.number.set('')
        self.result = DoubleVar()
        self.result.set(0)
        self.tempResult = DoubleVar()
        self.tempResult.set(0)
        self.operator = StringVar()
        self.operator.set('')
        self.tempOperator = StringVar()
        self.tempOperator.set('')
        self.start = BooleanVar()
        self.start.set(True)
        self.check = BooleanVar()
        self.check.set(False)
        self.wait = BooleanVar()
        self.wait.set(False)
        
        self.buttons = {}
        self.label = Label(window, textvariable=self.text, bg="white", width=16)
        self.label.grid(row=0, column=0, columnspan=4)
        self.buttons['c'] = Button(window, text='C', command=lambda: self.Clear())
        self.buttons['c'].grid(row=0, column=4)

        self.frame = Frame(window, borderwidth=1)
        self.frame.grid(row=2, column=3)

        for i in range(10):
           self.buttons[i] = Button(self.frame, text=i, command=lambda num=i: self.numberClick(num))
           self.buttons[i].grid(row=(9-i)/3, column=abs(i-1)%3)

        r = 0
        for i in ['+', '-', '*','/']:
            self.buttons[i] = Button(self.frame, text=i, command=lambda i=i: self.operatorClick(i))
            self.buttons[i].grid(row=r, column=3)
            r += 1

        self.buttons['.'] = Button(self.frame, text='.', command=lambda: self.numberClick('.'))
        self.buttons['.'].grid(row=3, column=0)
        self.buttons['='] = Button(self.frame, text='=', command=lambda: self.Result())
        self.buttons['='].grid(row=3, column=2)
        
    # Controllers.
    def Clear(self):
        self.text.set(u'')
        self.number.set('')
        self.operator.set('')
        self.result.set(0)
        self.tempOperator.set(False)
        self.tempResult.set(False)
        self.start.set(True)
        self.check.set(False)
        self.wait.set(False)
        
    def Calculate(self, a, b, operator):
        if operator == '+':
            self.result.set(a + b)
        elif operator == '-':
            self.result.set(a - b)
        elif operator == '*':
            self.result.set(a * b)
        elif operator == '/':
            self.result.set(a / b)
                
    def Result(self):
        if self.number.get() and self.operator.get():
            self.Calculate(self.result.get(), float(self.number.get()), self.operator.get())
            if self.wait.get():
                self.Calculate(self.tempResult.get(), self.result.get(), self.tempOperator.get())
                self.check.set(False)
                self.wait.set(False)
            if self.result.get()%1 == False:
                self.text.set(str(int(self.result.get())))
            else:
                self.text.set(str(self.result.get()))
            self.number.set(self.result.get())
            self.operator.set('')
            self.start.set(True)
            
    def operatorClick(self, key):       
        if self.number.get() != '':
            if self.operator.get() == '':
                self.result.set(float(self.number.get()))
                if key in ['+','-']:
                    self.check.set(True)
            else:
                if self.check.get() and (key in ['*','/']):
                    self.tempResult.set(self.result.get())
                    self.tempOperator.set(self.operator.get())
                    self.result.set(float(self.number.get()))
                    self.check.set(False)
                    self.wait.set(True)
                else:
                    self.Calculate(self.result.get(), float(self.number.get()), self.operator.get())    
                    if key in ['+','-']:
                        self.check.set(True)
                        if self.wait.get():
                            self.Calculate(self.tempResult.get(), self.result.get(), self.tempOperator.get())
                            self.wait.set(False)
            self.operator.set(key)
            self.text.set(self.text.get() + key)
            self.number.set('')
                
    def numberClick(self, key):
        if self.operator.get()=='' and self.start.get():
            self.number.set(str(key))
            self.text.set(str(key))
            self.start.set(False)
        else:
            if not ((str(key)=='.') and float(self.number.get())%1):
                self.number.set(self.number.get() + str(key))
                self.text.set(self.text.get() + str(key))
                
if __name__ == '__main__':
    window = Tk()
    myapp = Calculater(window)
    window.mainloop()              
