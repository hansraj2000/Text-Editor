import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

main_application=tk.Tk()
main_application.geometry('1100x600')
main_application.title('WR Pad')
main_application.wm_iconbitmap('icon.ico')

# **************************main menu***********************************
main_menu=tk.Menu()

file=tk.Menu(main_menu,tearoff=False)
# adding file Icons
newicon=tk.PhotoImage(file="icons2/new.png")
openicon=tk.PhotoImage(file='icons2/open.png') 
saveicon=tk.PhotoImage(file='icons2/save.png') 
save_asicon=tk.PhotoImage(file='icons2/save_as.png') 
exiticon=tk.PhotoImage(file='icons2/exit.png')


edit=tk.Menu(main_menu,tearoff=False)
# adding edit Icons
copyicon=tk.PhotoImage(file="icons2/copy.png")
pasteicon=tk.PhotoImage(file="icons2/paste.png")
cuticon=tk.PhotoImage(file="icons2/cut.png")
clear_allicon=tk.PhotoImage(file="icons2/clear_all.png")
findicon=tk.PhotoImage(file="icons2/find.png")


view=tk.Menu(main_menu,tearoff=False)
# adding view Icons
tool_baricon=tk.PhotoImage(file='icons2/tool_bar.png')
status_baricon=tk.PhotoImage(file='icons2/status_bar.png')


Color=tk.Menu(main_menu,tearoff=False)
# adding color icons
light_defaulticon=tk.PhotoImage(file='icons2/light_default.png')
light_plusicon=tk.PhotoImage(file='icons2/light_plus.png')
darkicon=tk.PhotoImage(file='icons2/dark.png')
redicon=tk.PhotoImage(file='icons2/red.png')
monokaiicon=tk.PhotoImage(file='icons2/monokai.png')
night_blueicon=tk.PhotoImage(file='icons2/night_blue.png')

color_theme=tk.StringVar()
color_icons=(light_defaulticon,light_plusicon,darkicon,redicon,monokaiicon,night_blueicon)

dict_color={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
}

# cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=Color)

# --------------------------end main menu-------------------------------


# **************************toolbar*************************************
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

# font box
font_tuples=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=40,textvariable=font_family,state='readonly')
font_box['values']=font_tuples
font_box.current(font_tuples.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

# size_box
size_var=tk.IntVar()
size_box=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
size_box['values']=tuple(range(2,101,2))
size_box.current(2)
size_box.grid(row=0,column=1,padx=5)

# Bold Button
bold_icon=tk.PhotoImage(file='icons2/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=3)
# Italic Button
italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=3)
# underline Button
underline_icon=tk.PhotoImage(file='icons2/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=3)
# font color icon
font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=3)
# align left
align_left_icon=tk.PhotoImage(file='icons2/align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=3)
# align center
align_center_icon=tk.PhotoImage(file='icons2/align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=3)
# align right
align_right_icon=tk.PhotoImage(file='icons2/align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=3)

# --------------------------end toolbar---------------------------------


# **************************text editor*********************************

text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set) 

# font family and font size functionality
current_font_family='Arial'
current_font_size=12

def change_font(event=None):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
size_box.bind("<<ComboboxSelected>>",change_fontsize)

text_editor.configure(font=("Arial",12))

# # # # Buttons functionality # # # # # # # #  
# # Bold button functionality
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command=change_bold)

# # italic button functionality
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_btn.configure(command=change_italic)

# # underline button functionality
def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_btn.configure(command=change_underline)

# # color font button functionality
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=change_font_color)

# # align functionality
# align left
def align_left():
    text_centent=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_centent,'left')
align_left_btn.configure(command=align_left)

# align right
def align_right():
    text_centent=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_centent,'right')
align_right_btn.configure(command=align_right)

# align center
def align_center():
    text_centent=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_centent,'center')
align_center_btn.configure(command=align_center)
# --------------------------end text editor-----------------------------


# **************************status bar**********************************
status_bar=ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Character: {characters}   Words: {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)
# --------------------------end status bar------------------------------


# **************************main menu functionality*********************

# # Variable
url=''

## new functionality
def new(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)

## open functionality
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('text file','*.txt'),('all file','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

## save file functionality
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('text file','*.txt'),('all file','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

## save as functionality
def save_as(event=None):
    global url
    try:
        content=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('text file','*.txt'),('all file','*,*')))
        url.write(content)
        url.close()
    except:
        return

## exit functionality
def exit(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save this file before exit ?')
            if mbox is True:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension='*.txt',filetypes=(('text files','*.txt'),('all files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return 
                

# adding file commands
file.add_command(label='New',image=newicon,compound=tk.LEFT,accelerator='Ctrl+N',command=new)
file.add_command(label='Open',image=openicon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
file.add_command(label='Save',image=saveicon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)
file.add_command(label='Save As',image=save_asicon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as)
file.add_command(label='Exit',image=exiticon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit)


############### find functionality
def find_func(event=None):
    find_win=tk.Toplevel()
    find_win.geometry('400x250+500+200')
    find_win.title('Find & Replace')
    find_win.resizable(0,0)

    def find():
        word=find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
    
    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    ## frame
    find_frame=ttk.LabelFrame(find_win,text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    find_label=ttk.Label(find_frame,text='Find :')
    replace_label=ttk.Label(find_frame,text='Replace :')

    ## entry
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)

    ## buttons
    find_btn=ttk.Button(find_frame,text='Find',command=find)
    replace_btn=ttk.Button(find_frame,text='Replace',command=replace)

    ## label grid
    find_label.grid(row=0,column=0,padx=4,pady=4,sticky=tk.W)
    replace_label.grid(row=1,column=0,padx=4,pady=4,sticky=tk.W)

    ## entry grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    ## buttons grid
    find_btn.grid(row=2,column=0,padx=8,pady=4)
    replace_btn.grid(row=2,column=1,padx=8,pady=4)

    find_win.mainloop()
    
# adding edit commands
edit.add_command(label='Copy',image=copyicon,compound=tk.LEFT,accelerator='Ctrl+C',command=text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=pasteicon,compound=tk.LEFT,accelerator='Ctrl+V',command=text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cuticon,compound=tk.LEFT,accelerator='Ctrl+X',command=text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All',image=clear_allicon,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',image=findicon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)

# adding view checkbtn
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        # status_bar.pack(side=tk.Button)
        show_toolbar=True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True


view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=0,variable=show_toolbar,image=tool_baricon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1,offvalue=False,variable=show_statusbar,image=status_baricon,compound=tk.LEFT,command=hide_statusbar)

# adding color theme
def change_color():
    choose_color=color_theme.get()
    choosen_theme=dict_color.get(choose_color)
    fg_color,bg_color=choosen_theme[0],choosen_theme[1]
    text_editor.config(bg=bg_color,fg=fg_color)

count=0
for i in dict_color:
    Color.add_radiobutton(label=i,image=color_icons[count],variable=color_theme,compound=tk.LEFT,command=change_color)
    count+=1

# --------------------------end main menu functionality-----------------

main_application.config(menu=main_menu)

# # # binding shortcut keys
main_application.bind("<Control-n>",new)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",save_as)
main_application.bind("<Control-q>",exit)
main_application.bind("<Control-f>",find_func)

main_application.mainloop()