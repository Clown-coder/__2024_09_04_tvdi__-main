from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('Lesson 4 ')
        style = ttk.Style(self)
        style.configure('button.TButton',font=('Helvetica',30))
        topFrame = ttk.Frame(self,borderwidth=1,relief="groove")
        topFrame.pack(padx=10,pady=(10,0),ipadx=10,ipady=10,expand=True,fill='x')
        btn1 = ttk.Button(topFrame,text='botton 01')
        btn1.pack(side='left',expand=True,fill='x',padx=10)
        btn2 = ttk.Button(topFrame,text='botton 02')
        btn2.pack(side='left',expand=True,fill='x',padx=10)
        btn3 = ttk.Button(topFrame,text='botton 03')
        btn3.pack(side='left',expand=True,fill='x',padx=10)
        bottomFrame = ttk.Frame(self,borderwidth=1,relief="groove",width=500,height=300)
        bottomFrame.pack(padx=10,pady=10,ipadx=10,ipady=10,expand=True,fill='x')
        
        bottomFrame1 = ttk.Frame(bottomFrame,borderwidth=1,relief="groove",width=500,height=300)
        bottomFrame1.pack(padx=10,pady=10,ipadx=10,ipady=10,expand=True,fill='x',side='left')
        
        
        btn4 = ttk.Button(bottomFrame1,text='botton 04',style='button.TButton')
        btn4.pack(side='top',expand=True,fill='x',padx=10)
        btn5 = ttk.Button(bottomFrame1,text='botton 05')
        btn5.pack(side='top',expand=True,fill='x',padx=10,pady=15)
        btn6 = ttk.Button(bottomFrame1,text='botton 06')
        btn6.pack(side='top',expand=True,fill='x',padx=10,pady=15)

        bottomFrame2 = ttk.Frame(bottomFrame,borderwidth=1,relief="groove",width=500,height=300)
        bottomFrame2.pack(padx=10,pady=10,ipadx=10,ipady=10,expand=True,fill='x',side='left')
        

        btn7 = ttk.Button(bottomFrame2,text='botton 07',style='button.TButton')
        btn7.pack(side='top',expand=True,fill='x',padx=10)
        btn8 = ttk.Button(bottomFrame2,text='botton 08')
        btn8.pack(side='top',expand=True,fill='x',padx=10,pady=15)
        btn9 = ttk.Button(bottomFrame2,text='botton 09',style='button.TButton')
        btn9.pack(side='top',expand=True,fill='x',padx=10)

        bottomFrame3 = ttk.Frame(bottomFrame,borderwidth=1,relief="groove",width=500,height=300)
        bottomFrame3.pack(padx=10,pady=10,ipadx=10,ipady=10,expand=True,fill='x',side='left')
        

        btn10 = ttk.Button(bottomFrame3,text='botton 10',style='button.TButton')
        btn10.pack(side='top',expand=True,fill='x',padx=10)
        btn11 = ttk.Button(bottomFrame3,text='botton 11',style='button.TButton')
        btn11.pack(side='top',expand=True,fill='x',padx=10)
        btn12 = ttk.Button(bottomFrame3,text='botton 12',style='button.TButton')
        btn12.pack(side='top',expand=True,fill='x',padx=10)





def main():
    window=Window(theme='ark')
    window.mainloop()

if __name__=='__main__':
    main()