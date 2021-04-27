'''
code file: appfile.py
date: Apr 2021
commants:

Use:
    REQUIRES execution as root
    Options:
    1.  sudo su into root user
        then execute
    2.  from shell or launcher:
        pkexec python3 ...fullpath.../appfile.py
'''
from tkinter import *
from tkinter.ttk import *  # defaults all widgets as ttk
import os
import shutil
# from tkinter.font import Font
    # myfont = Font(family='Lucida Console', weight = 'bold', size = 20)
from tkinter import filedialog
from tkinter import messagebox
from ttkthemes import ThemedTk  # ttkthemes is applied to all widgets


class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        lbl = Label(self, text='Name', width=15, anchor=E)
        lbl.grid(row=1, column=1)

        lbl = Label(self, text='Version', width=15, anchor=E)
        lbl.grid(row=2, column=1)

        lbl = Label(self, text='Type', width=15, anchor=E)
        lbl.grid(row=3, column=1)

        lbl = Label(self, text='Exec', width=15, anchor=E)
        lbl.grid(row=4, column=1)

        lbl = Label(self, text='Path', width=15, anchor=E)
        lbl.grid(row=5, column=1)

        lbl = Label(self, text='Icon', width=15, anchor=E)
        lbl.grid(row=6, column=1)

        lbl = Label(self, text='Terminal', width=15, anchor=E)
        lbl.grid(row=7, column=1)

        lbl = Label(self, text='Categories', width=15, anchor=E)
        lbl.grid(row=8, column=1)

        lbl = Label(self, text='Comment', width=15, anchor=E)
        lbl.grid(row=9, column=1)

        lbl = Label(self, text='Encoding', width=15, anchor=E)
        lbl.grid(row=10, column=1)

        lbl = Label(self, text='GenericName', width=15, anchor=E)
        lbl.grid(row=11, column=1)

        self.v_name = StringVar()
        # self.v_name.trace("w", self.eventHandler)
        e_name = Entry(self, textvariable=self.v_name, width=30)
        e_name.grid(row=1, column=2, pady=(8, 5))

        self.v_version = StringVar()
        # self.v_version.trace("w", self.eventHandler)
        e_version = Entry(self, textvariable=self.v_version, width=30)
        e_version.grid(row=2, column=2, pady=5)
        self.v_version.set("1.0")

        self.v_type = StringVar()
        # self.v_type.trace("w", self.eventHandler)
        e_type = Entry(self, textvariable=self.v_type, width=30)
        e_type.grid(row=3, column=2, pady=5)
        self.v_type.set("Application")

        self.v_exec = StringVar()
        # self.v_exec.trace("w", self.eventHandler)
        e_exec = Entry(self, textvariable=self.v_exec, width=30)
        e_exec.grid(row=4, column=2, pady=5)

        self.v_path = StringVar()
        # self.v_path.trace("w", self.eventHandler)
        e_path = Entry(self, textvariable=self.v_path, width=30)
        e_path.grid(row=5, column=2, pady=5)

        self.v_icon = StringVar()
        # self.v_icon.trace("w", self.eventHandler)
        e_icon = Entry(self, textvariable=self.v_icon, width=30)
        e_icon.grid(row=6, column=2, pady=5)

        self.v_terminal = StringVar()
        # self.v_terminal.trace("w", self.eventHandler)
        e_terminal = Entry(self, textvariable=self.v_terminal, width=30)
        e_terminal.grid(row=7, column=2, pady=5)
        self.v_terminal.set("false")

        self.v_categories = StringVar()
        # self.v_categories.trace("w", self.eventHandler)
        e_categories = Entry(self, textvariable=self.v_categories, width=30)
        e_categories.grid(row=8, column=2, pady=5)
        self.v_categories.set("Utility")

        self.v_comment = StringVar()
        # self.v_comment.trace("w", self.eventHandler)
        e_comment = Entry(self, textvariable=self.v_comment, width=30)
        e_comment.grid(row=9, column=2, pady=5)

        self.v_encoding = StringVar()
        # self.v_encoding.trace("w", self.eventHandler)
        e_encoding = Entry(self, textvariable=self.v_encoding, width=30)
        e_encoding.grid(row=10, column=2, pady=5)
        self.v_encoding.set("UTF-8")

        self.v_genericname = StringVar()
        # self.v_genericname.trace("w", self.eventHandler)
        e_genericname = Entry(self, textvariable=self.v_genericname, width=30)
        e_genericname.grid(row=11, column=2, pady=5)

        # CHECKBUTTON
        self.vcb_dtop = IntVar()
        cb_dtop = Checkbutton(self, variable=self.vcb_dtop,
                              command=self.enable_user,
                              text='Add to Desktop  User:')
        cb_dtop.grid(row=13, column=2, sticky=E, pady=5)

        # ENTRY for USER NAME
        self.v_user = StringVar()
        # self.v_genericname.trace("w", self.eventHandler)
        self.e_user = Entry(self, textvariable=self.v_user, width=10, state=DISABLED)
        self.e_user.grid(row=13, column=3, sticky=W)

        # BUTTONS
        btn_open_exec = Button(self, text='Open File', command=self.on_open_exec)
        btn_open_exec.grid(row=4, column=3, padx=5)

        btn_open_icon = Button(self, text='Open Icon', command=self.on_open_icon)
        btn_open_icon.grid(row=6, column=3, padx=5)

        btn_save = Button(self, text='S a v e', command=self.on_save)
        btn_save.grid(row=12, column=3, padx=5)
        #

        self.txt_others = Text(self, height=7, width=40, highlightbackground='#000')
        self.txt_others.grid(row=12, column=1, columnspan=2, sticky=EW, pady=5, padx=2)
        self.txt_others.insert(1.0, "# place others in here.\n")

        e_name.focus()
        root.config(bg='#333')

    # KEY BINDINGS
        root.bind("<Control-q>", exit_program)
        #root.bind("<>",)


    # FUNCTIONS

    def on_open_exec(self):
        ''' Get the file name from the system '''
        filename = filedialog.askopenfilename(initialdir="/home/",
                                              title="Select executable file:",
                                              filetypes=(("All Files", "*"),))
        self.v_exec.set(filename)


    def on_open_icon(self):
        ''' Get the file name from the system '''
        filename = filedialog.askopenfilename(initialdir="/usr/share/icons/",
                                              title="Select icon file:",
                                              filetypes=(("All Files", "*"),))
        self.v_icon.set(filename)

    def enable_user(self):
        '''
        Enable user name entry field
        Operator checked "Add to Desktop"
        Operator must also enter user name
        '''
        self.e_user.config(state=NORMAL)

    def on_save(self):
        '''
        concat all entries into one text file
        Save the text file
        Add the ".desktop" extention if missing
        '''
        user = ""
        if self.vcb_dtop.get() == 1:
            user = self.e_user.get()
            if user == "":
                messagebox.showerror("Add to Desktop", "Missing 'User:'")
                return
        user = self.v_user.get()
        filetext = "[Desktop Entry]\n"
        name = self.v_name.get()
        vers = self.v_version.get()
        typ = self.v_type.get()
        exe = self.v_exec.get()
        path = self.v_path.get()
        icon = self.v_icon.get()
        term = self.v_terminal.get()
        cat = self.v_categories.get()
        com = self.v_comment.get()
        enc = self.v_encoding.get()
        gen = self.v_genericname.get()
        other = self.txt_others.get(1.0, "end-1c")
        # Name
        if name == "":
            messagebox.showerror("Debian Create Launcher", "Missing attribute: Name")
            return
        else:
            filetext += "Name=" + name + "\n"
        # Version
        if vers != "":
            filetext += "Version=" + vers + "\n"
        # Type
        if typ == "":
            filetext += "Type=Application\n"
        else:
            filetext += "Type=" + typ + "\n"
        # Exec
        if exe == "":
            messagebox.showerror("Debian Create Launcher", "Missing attribute: Exec")
            return
        else:
            filetext += "Exec=" + exe + "\n"
        # Path
        if path != "":
            filetext += "Path=" + path + "\n"
        # Icon
        if icon != "":
            filetext += "Icon=" + icon + "\n"
        # Terminal
        if term == "":
            filetext += "Terminal=false\n"
        else:
            filetext += "Terminal=" + term + "\n"
        # Categories
        if cat != "":
            filetext += "Categories=" + cat + "\n"
        # Comment
        if com != "":
            filetext += "Comment=" + com + "\n"
        # Encoding
        if enc != "":
            filetext += "Encoding=" + enc + "\n"
        # GenericName
        if gen != "":
            filetext += "GenericName=" + gen + "\n"
        # OTHERS
        if other != "":
            filetext += other + "\n"

        # save the file
        fname = filedialog.asksaveasfilename(confirmoverwrite=True,
                                             initialdir="/usr/share/applications/")
        if not fname.endswith(".desktop"):
            messagebox.showwarning("Save File", "Extention '.desktop' will be added.")
            fname += ".desktop"

        if fname:
            try:
                with open(fname, "w") as f:
                    f.write(filetext)  # contents of the demo Text widget
            except:
                messagebox.showerror("Save File", "Failed to save file\n'%s'" % fname)
                return
            else:
                if self.vcb_dtop.get() == 1:
                    if user != "":
                        base = os.path.basename(fname)
                        dtpath = "/home/" + user + "/Desktop/" + base
                        shutil.copyfile(fname, dtpath)
                        shutil.chown(dtpath, user, user)  # change ownership to user
                messagebox.showinfo("File Saved",
                                    "You may need to reboot")


def exit_program(e):
    ''' Quit Program '''
    root.destroy()


# CHECK FOR ROOT USER
userr = os.environ.get("USER")
if userr != "root":
    messagebox.showinfo("Not root user",
                        "Run as 'root' in order to access ...applications directory.")
    sys.exit()

root = ThemedTk(theme="black")

# change working directory to path for this file
p = os.path.realpath(__file__)
os.chdir(os.path.dirname(p))

root.title("Debian Create Launcher")
root.resizable(0, 0) # no resize & removes maximize button
app = Application(root)
app.mainloop()
