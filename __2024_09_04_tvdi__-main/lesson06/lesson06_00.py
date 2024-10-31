import datasource
from ttkthemes import ThemedTk
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
import sqlite3

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('Lesson 6 ')

        #=== sytle====
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',30))
        #=== en of style====

        #===topFrame====
        topFrame = ttk.Frame(self,borderwidth=1,relief="groove")
        ttk.Label(topFrame,text='各縣市空氣指標AQI',style='TopFrame.TLabel').pack()
        topFrame.pack(padx=10,pady=(10,0),ipadx=10,ipady=10,expand=True,fill='x')
        
        #==== end topframe======

        #=======bottomframe==========
        bottomFrame = ttk.Frame(self,borderwidth=1,relief="groove",width=500,height=300)
        
        self.select_sitenames = tk.StringVar()

        sitenames= datasource.get_sitenames()
        
        self.sitenames_cb = ttk.Combobox(bottomFrame,textvariable=self.select_sitenames)
        self.sitenames_cb.configure(values=sitenames,state='readonly')
        self.select_sitenames.set('--請選擇站點--')
        self.sitenames_cb.bind('<<ComboboxSelected>>',self.sitename_selected)
        self.sitenames_cb.pack(side='left',anchor='n',pady=5,padx=5)


        columns = ('date', 'county', 'aqi','pm25','status','lat','lon')

        self.tree = ttk.Treeview(bottomFrame, columns=columns, show='headings')

        # define headings
        self.tree.heading('date', text='日期')
        self.tree.heading('county', text='縣市')
        self.tree.heading('aqi', text='AQI')
        self.tree.heading('pm25', text='PM25')
        self.tree.heading('status', text='狀態')
        self.tree.heading('lat', text='緯度')
        self.tree.heading('lon', text='經度')

        self.tree.column('date',width=150,anchor='center')
        self.tree.column('county',width=80,anchor='center')
        self.tree.column('aqi',width=50,anchor='center')
        self.tree.column('pm25',width=50,anchor='center')
        self.tree.column('status',width=80,anchor='center')
        self.tree.column('lat',width=100,anchor='center')
        self.tree.column('lon',width=100,anchor='center')
        
        self.tree.pack(side='right')
        
        
        btn1= ttk.Button(bottomFrame,text='Update',command=self.update_data)
        btn1.pack()
        bottomFrame.pack(padx=10,pady=10,ipadx=10,ipady=10,expand=True,fill='x')
        
        #=======bottomframe==========
    def sitename_selected(self,event):
        selected = self.select_sitenames.get()
        
        for record in self.tree.get_children():
            self.tree.delete(record)
        
        selected_data = self.fetch_data_from_db(selected)

        for one_record in selected_data:
            self.tree.insert('',tk.END,values=one_record)

    def fetch_data_from_db(self,sitename:str)->list:
        conn = sqlite3.connect('AQI_00.db')
        cursor = conn.cursor()

        query = 'SELECT date,county , aqi, pm25,status,lat,lon FROM records WHERE sitename = ?'
        cursor.execute(query,(sitename,))
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data
    def update_data(self):
        conn = sqlite3.connect('AQI_00.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM records')
        conn.commit()

        sitenames = datasource.get_sitenames()
        for sitename in sitenames:
            selected_data = datasource.get_selected_data(sitename)
            datasource.insert_data_into_db(selected_data)
        cursor.close()
        conn.close()

        showinfo("Update","Database Updated ! ")
        self.select_sitenames.set('--請選擇站點--')
        self.sitenames_cb.configure(values = sitenames)

    


def main():
    window=Window(theme='ark')
    window.mainloop()

if __name__=='__main__':
    main()