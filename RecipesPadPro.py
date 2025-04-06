from tkinter import *
from  tkinter  import  filedialog 
from tkinter import messagebox as box 
import os 
import subprocess 
from  queue  import LifoQueue as stack 
class Recipes:
  def __init__(self, root):
    self.root=root
    self.undo_stack=stack()
    self.redo_stack=stack()
    self.file_name=None
    self.file_path=None
  def ui(self):
    self.title("Recipes  Pad Pro")
    self.top_frame=Frame(self.root)
    self.top_frame.pack(side=TOP,expand=YES,fill=BOTH)
    self.option=StringVar()
    self.file_options=['New file ^N','Open a file ^O','Close file ^P','Save file ^S','Save as ^Q']
    self.file_operations=OptionMenu(self.root,self.option,*self.file_options,command=self.file_functions)
    self.file_operations.pack(side=LEFT)
    self.run_code=Button(self.top_frame,text='Run',fg='green',command=self.run)
    self.run_code.pack(side=LEFT)
    self.text_area=Text(self.root)
    self.text_area.pack(side=TOP, fill=BOTH, expand=YES)
    self.bottom_frame=Frame(self.root)
    self.bottom_frame.pack(side=TOP,expand=YES,fill=BOTH)
    self.file_type=Label(self.bottom_frame)
    self.file_type.pack(side=RIGHT)
  def file_functions(self):
    target_function=self.file_options.get()
    functions={'New file ^N':self.new,'Open a file ^O':self.open_file,'Close file ^P':self.close,
    'Save file ^S':self.save,'Save as ^Q':sel.save_as}
    return functions[target_function]
  def open_file(self):
    self.file_name=filedialog.askopenfilename(title="Open file",filetypes=[('*','.*')])
    if len(self.file_name)==0:return
    with open(self.file_name,'r') as file:
      self.text_area.delete('1.0',END)
      self.text_area.insert(INSERT,file.read())
  def save(self):
    try:
      with open(self.file_name,'w') as file:
        self.file_name.write(self.text_area.get('1.0',END))
    except PermissionError:box.showwarning('Permission  Denied','Write  Failure PermissionError')
      return 
  def save_as(self):
    self.file_name=filedialog.asksaveasfilename(title="Enter  file  name",filetypes=[('*','*')])
    if len(self.file_name)==0:return 
    self.save()
    
