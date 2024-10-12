from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,askopenfile,asksaveasfilename
import subprocess
import os

win = Tk()
win.title('Python')
win.geometry('1280x950')
win.configure(bg="#323846")
win.resizable(False,False)

file_path=''
def set_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path,'r') as file:
        code = file.read()
        code_input.delete('1.0',END)
        code_input.insert('1.0',code)
        set_path(path)
def save():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files','*py')])
    else:
        path= file_path
    with open(path,'w') as file:
        code = code_input.get('1.0',END)
        file.write(code)
        set_path(path)
def run():
    if file_path=='':
        messagebox.showerror('Python IDLE','Save Your Code')
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output , error = process.communicate()
    code_output.insert('1.0',output)
    code_output.insert('1.0',error)

imgae_icon = PhotoImage(file=r'images//logo.png')
win.iconphoto(False,imgae_icon)

code_input=Text(win,font=('cosolas 18'))
code_input.place(x=190,y=0,width=680,height=720)

code_output=Text(win,font=('cosolas 15'),bg="#323846",fg='light green')
code_output.place(x=870,y=0,width=420,height=720)

Open = PhotoImage(file='images//open.png')
Save = PhotoImage(file='images//save.png')
Run = PhotoImage(file='images//run.png')
open_button = Button(win,image=Open,command=open_file,bg="#323846",bd=0)
open_button.place(x=30,y=30)
save_button = Button(win,image=Save,command=save,bg="#323846",bd=0)
save_button.place(x=30,y=145)
run_button = Button(win,image=Run,command=run,bg="#323846",bd=0)
run_button.place(x=30,y=260)














win.mainloop()