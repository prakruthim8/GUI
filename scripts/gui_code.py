# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:35:17 2022

@author: prakr
"""
import string
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
from tkinter.filedialog import askopenfilename
import time
from script import main_script
import os


ws = Tk()
ws.title('PythonGuides')
ws.geometry('450x200') 
def open_file():
    global file_name
    file_path = askopenfilename(filetypes=[("Excel files", ".csv")])
    file_name= os.path.basename(file_path)
    #print(file_name)
    if file_path is not None:
        #global data
        data = file_name
        main_script(data)
#os.path.basename("path/to/file/sample.txt")
#print(file_name)
#choose file
msbtn = Button(ws, text ='Upload File', command = lambda:open_file()) 
#file_label = tk.Label(ws, text = 'Upload file', font=('calibre',10, 'bold'))
msbtn.grid(row=7, column=3)
#file_label.grid(row=5,column=0)

#no of flies
# def display_text(string):
#    string= time_entry.get()

#print(string) 
time_var=tk.StringVar()
time_label = tk.Label(ws, text = 'Time interval', font=('calibre',10, 'bold'))
time_label2 = tk.Label(ws, text = 'to', font=('calibre',8, 'normal'))

time_entry = tk.Entry(ws,textvariable = time_var, font=('calibre',7,'normal'))
time_entry2 = tk.Entry(ws,textvariable = time_var, font=('calibre',7,'normal'))

def get_time():
    input_time= time_entry.get()
    print(input_time)
    


date_var=tk.StringVar()
date_label = tk.Label(ws, text = 'Date', font=('calibre',10, 'bold'))
date_label2 = tk.Label(ws, text = 'to', font=('calibre',8, 'normal'))
date_entry = Entry(ws,textvariable = date_var, font=('calibre',7,'normal'))
date_entry2 = Entry(ws,textvariable = date_var, font=('calibre',7,'normal'))

def get_date():
    input_date= date_entry.get()
    print(input_date)
    #print("output {}".format(input_date))

gen_var=tk.StringVar()
gen_label = tk.Label(ws, text = 'No of flies per genotype', font=('calibre',10, 'bold'))
gen_entry = tk.Entry(ws,textvariable = gen_var, font=('calibre',10,'normal'))

def get_genotype():
    global input_fly_number
    input_fly_number= gen_entry.get()

    print(input_fly_number)
    


time_entry.grid(row=1,column=1)
time_entry2.grid(row=1,column=3)
time_label.grid(row=1,column=0)
time_label2.grid(row=1,column=2)
date_entry.grid(row=0,column=1)
date_entry2.grid(row=0,column=3)
date_label.grid(row=0,column=0)
date_label2.grid(row=0,column=2)
gen_entry.grid(row=4,column=1)
gen_label.grid(row=4,column=0)





ws.mainloop()