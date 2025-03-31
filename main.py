#<--*--RecipesPadPro--built-by-Malick_Ould_Hamdi--*-->
from tkinter import*
from tkinter import filedialog
file=''
file_container=''
def save_file_as():
  global file
  file=filedialog.asksaveasfilename(title="Enter file name",filetypes=[('*','*')])
  save_file(file,file_container.get())
def create_new_file():
  global file
  file=filedialog.asksaveasfilename(title="Enter new file name",filetypes=[('*','*')])
  file_container.delete('1.0',END)
  file_container.insert(INSERT,'')
def save_file():
  with open(file,'w') as the_file:
    the_file.write(file_container.get('1.0',END))
def read_file():
  global file
  file=filedialog.askopenfilename(title="Open file",filetypes=[('*','*')])
  with open(file,'r') as file:
    file_container.delete('1.0',END)
    file_container.insert(INSERT,file.read())
def commands(event,number):
  global file,file_container
  if number==1:return save_file(file,file_container.get())
  if number==2:return read_file(file_container)
  if number==3:return save_file_as()
  if number==4 return create_new_file()
  if number==5:return window.quit()
#Program main entry
window=Tk()
window.title("Recipes Pad Pro")
file_container=Text(window)
file_container.pack(side=TOP,fill=BOTH,expand=YES)
buttons_area=Frame(window)
buttons_area.pack(side=TOP,fill=BOTH,expand=YES)
my_buttons={'Run':0,'Save':1,'Read':2,'Save as':3,'New file':4,'Quit':5}
for button in my_buttons:
  button=Button(buttons_area,text=button,command=lambda i=my_buttons[button]:commands(event=None,number=i))
  button.pack(side=LEFT,fill=BOTH,expand=YES)
window.bind('Control-s',commands(number=1))
window.bind('Control-o',command(number=2))
window.mainloop()
    
