#<--*--RecipesPadPro--built-by-Malick_Ould_Hamdi--*-->
from queue import LifoQueue as stack
from tkinter import*
from tkinter import filedialog
undo_stack=stack()
redo_stack=stack()
empty_stack=stack()
file=''
file_container=''
def save_file_as():
  global file
  file=filedialog.asksaveasfilename(title="Enter file name",filetypes=[('*','*')])
  save_file(file,file_container.get('1.0',END))
def clear_stack():
    global undo_stack,redo_stack
    redo_stack=empty_stack
    undo_stack=empty_stack
def create_new_file():
  clear_stack()
  global file
  file=filedialog.asksaveasfilename(title="Enter new file name",filetypes=[('*','*')])
  file_container.delete('1.0',END)
  file_container.insert(INSERT,'')
def save_file():
  with open(file,'w') as the_file:
    the_file.write(file_container.get('1.0',END))
def show_file():
  file_container.delete('1.0',END)
  file_container.insert(INSERT,file)
def read_file():
  clear_stack()
  global file
  file=filedialog.askopenfilename(title="Open file",filetypes=[('*','*')])
  with open(file,'r') as file:
    show_file()
def line_count():
  lines=sum(1 for line in file_container.get('1.0',END))
  lines=str(lines)
  line['text']=lines
def undo():
  global undo_stack,redo_stack
  if undo_stack.empty():return
  text=undo_stack.get()
  swap(text)
  redo_stack.put(text)
def swap(x):
  global file
  y=file
  file=x
  show_file()
  file=y
def redo():
  global undo_stack,redo_stack
  if redo_stack.empty():return
  text=redo_stack.get()
  swap(text)
  undo_stack.put(text)
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
lines=Label(buttons_area,text='')
lines.pack(side=LEFT)
line_count()
window.bind('<Return>',lambda event:line_count())
window.bind('<Control-s>', lambda event:save_file())
window.bind('<Control-o>', lambda event:read_file())
window.bind('<Return>', lambda event:undo_stack.put(file_container.get('1.0',END)))
window.bind('<Control-z>',lambda event:undo())
window.bind('<Control-y>',lambda event:redo())
window.bind('<Control-n>',lambda event:create-new_file())
window.mainloop()
    
