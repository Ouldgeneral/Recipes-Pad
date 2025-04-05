#<--*--RecipesPadPro--built-by-Malick_Ould_Hamdi--*-->
from queue import LifoQueue as stack
from tkinter import*
from tkinter import filedialog
from tkinter import messagebox as box
undo_stack=stack()
redo_stack=stack()
file=''
file_container=''
file_types={'txt':'PleinText','html':'HTML' ,'htm':'HTML','js':'JavaScript','java':'Java','cpp':'C++',
            'c':'C','asm':'Assembly','css':'CSS','cs':'C#','php':'PHP','py':'Python','sh':'Shell'}
def filetype():
  file_name=file.split('/')
  file_name=file_name[-1]
  file_name=file_name.split('.')
  window.title(f'{file_name[0]}-Recipe')
  try:
    type['text']=file_types[file_name[-1]]
    type['fg']='green'
  except KeyError:
    type['text']='Unknown'
    type['fg']='red'
def save_file_as():
  global file
  file=filedialog.asksaveasfilename(title="Enter file name",filetypes=[('*','*')])
  save_file()
def clear_stack():
    global undo_stack,redo_stack
    redo_stack=stack()
    undo_stack=stack()
def create_new_file():
  clear_stack()
  global file
  file=filedialog.asksaveasfilename(title="Enter new file name",filetypes=[('*','*')])
  show_file()
def save_file():
  try:
      with open(file,'w') as the_file:
        the_file.write(file_container.get('1.0',END))
  except PermissionError:
      box.showwarning('Permission Denied','Write Failure ')
def show_file():
  filetype()
  file_container.delete('1.0',END)
  try:
    text=open(file,"r")
    file_container.insert(INSERT,text.read())
    undo_stack.put(text.read())
    text.close()
  except FileNotFoundError:file_container.insert(INSERT,'')
def read_file():
  clear_stack()
  global file
  file=filedialog.askopenfilename(title="Open file",filetypes=[('*','*')])
  show_file()
def line_count():
  lines=len(file_container.get('1.0',END).splitlines())
  lines=str(lines)
  line['text']=lines
def undo():
  global undo_stack,redo_stack
  if undo_stack.empty():return
  current=file_container.get('1.0',END)
  text=undo_stack.get()
  update(text)
  redo_stack.put(current)
def redo():
  global undo_stack,redo_stack
  if redo_stack.empty():return
  current=file_container.get('1.0',END)
  text=redo_stack.get()
  update(text)
  undo_stack.put(current)
def update(text):
  file_container.delete('1.0',END)
  file_container.insert(INSERT,text)
def on_return(event):
  line_count()
  txt=file_container.get('1.0',END)
  undo_stack.put(txt)
  
#Program main entry
window=Tk()
window.title("Recipes Pad Pro")
file_container=Text(window)
file_container.pack(side=TOP,fill=BOTH,expand=YES)
buttons_area=Frame(window)
buttons_area.pack(side=TOP,fill=BOTH,expand=YES)
my_buttons={'Save':save_file,'Read':read_file,'Save as':save_file_as,'New file':create_new_file,'Quit':window.quit}
for button in my_buttons:
  button=Button(buttons_area,text=button,command=lambda i=my_buttons[button]:i())
  button.pack(side=LEFT,fill=BOTH,expand=YES)
line=Label(buttons_area,text='')
line.pack(side=LEFT)
type=Label(buttons_area,text='')
type.pack(side=LEFT)
line_count()
window.bind('<Return>',lambda event:on_return(event))
window.bind('<Control-s>', lambda event:save_file())
window.bind('<Control-o>', lambda event:read_file())
window.bind('<Control-z>',lambda event:undo())
window.bind('<Control-y>',lambda event:redo())
window.bind('<Control-n>',lambda event:create_new_file())
window.mainloop()
    
