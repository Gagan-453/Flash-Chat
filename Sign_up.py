from tkinter import *
from sqlite3 import *
from tkinter import messagebox
conn = connect(database='flash_chat')
cursor = conn.cursor()
root = Tk()

class signup():
    def __init__(self, root):
        self.signup_window = Toplevel(width=500, height=500, bg='#060606')
        self.signup_window.propagate(0)
        self.signup_window.iconbitmap('required/icon.ico')
        self.signup_window.title('Flash Chat Sign up')
        self.signup_window.resizable(False, False)
        self.heading = Label(self.signup_window, text='Flash Chat   Registration', width=25, bg='#060606', fg='pink', font=('Cambria', 25, 'bold'))
        self.heading.pack()

        self.name_var = StringVar()
        self.name = Entry(self.signup_window, width=25, bg='white', fg='#0565AB', textvariable=self.name_var, validate='key', validatecommand=self.check, font=('Arial Black', 15, 'bold'))
        self.name.place(x=100, y=100)

        self.email_var = StringVar()
        self.email = Entry(self.signup_window, width=30, bg='white', fg='#0565AB', textvariable=self.email_var, validate='key', validatecommand=self.check, font=('Arial Rounded MT Bold', 13))
        self.email.place(x=100, y=150)

        self.password_var = StringVar()
        self.password = Entry(self.signup_window, width=25, bg='white', fg='#151314', textvariable=self.password_var, validate='key', validatecommand=self.check, font=('Times new roman', 15, 'bold'), show='*')
        self.password.place(x=225, y=230)

        self.retype_password_var = StringVar()
        self.retype_password = Entry(self.signup_window, width=25, bg='white', fg='#151314', textvariable=self.retype_password_var, validate='key', validatecommand=self.check, font=('Times new roman', 15, 'bold'), show='*')
        self.retype_password.place(x=225, y=270)

        self.name_lbl = Label(self.signup_window, text='Name:', bg='#060606', fg='#F6F103', font=('Arial', 13, 'bold'))
        self.name_lbl.place(x=20, y=100)

        self.email_lbl = Label(self.signup_window, text='Gmail:', bg='#060606', fg='#F6F103', font=('Arial', 13, 'bold'))
        self.email_lbl.place(x=20, y=150)

        self.passwd_lbl = Label(self.signup_window, text='Password:', bg='#060606', fg='#DAF11A', font=('Arial', 13, 'bold'))
        self.passwd_lbl.place(x=120, y=230)

        self.retype_passwd_lbl = Label(self.signup_window, text='Retype password:', bg='#060606', fg='#DAF11A', font=('Arial', 13, 'bold'))
        self.retype_passwd_lbl.place(x=60, y=270)

        self.note = """NOTE your name is publicly visible..
        NOTE Gmail is used to recover your password in lost cases.."""
        self.notes = Label(self.signup_window, text=self.note, bg='#060606', fg='orange', width=50, font=('Calibri', 12, 'italic'))
        self.notes.place(x=40, y=330)

        self.save = Button(self.signup_window, text='Sign Up', width=13, height=1, bg='#E7F37E', fg='black', activebackground='light green', font=('Calibri', 13, 'bold'), command=self.add_to_database)
        self.save.place(x=30, y=430)

        self.clear = Button(self.signup_window, text='Clear', width=13, height=1, bg='#E7F37E', fg='black', activebackground='light green', font=('Calibri', 13, 'bold'), command=self.clear)
        self.clear.place(x=200, y=430)

        self.back = Button(self.signup_window, text='Back', width=13, height=1, bg='#E7F37E', fg='black', activebackground='light green', font=('Calibri', 13, 'bold'))
        self.back.place(x=360, y=430)

    def clear(self):
        self.name_var.set('')
        self.email_var.set('')
        self.password_var.set('')
        self.retype_password_var.set('')

    def add_to_database(self):
        self.name1 = self.name_var.get()
        self.email1 = self.email_var.get()
        self.password1 = self.password_var.get()
        self.retype_password1 = self.retype_password_var.get()

        if self.name1 == '':
            self.name.config(bg='#FA8273')
            messagebox.showerror('Error in Sign up!', 'Name cannot be empty!')
        elif self.name1.isspace() == True:
            self.name.config(bg='#FA8273')
            messagebox.showerror('Error in Sign up!', 'Name cannot be empty!')
        elif self.email1.strip().endswith('@gmail.com') == False:
            self.email.config(bg='#FA8273')
            messagebox.showerror('Error in Sign up!', 'Invalid mail ID')
        elif self.password1.isalpha():
            self.password.config(bg='#FA8273')
            messagebox.showerror('Error in Sign up', 'Your Password only contains Alphabets try including some numbers..')
        elif self.password1.isdigit():
            self.password.config(bg='#FA8273')
            messagebox.showerror('Error in Sign up!', 'Your password contains only number, try including some alphabets..')
        elif self.password1 == '':
            self.password.config(bg='#FA8273')
            messagebox.showerror('Error in Sign up!', 'Password cannot be empty..')
        elif self.password1.isspace == True:
            self.password.config(bg='#FA8273')
            messagebox.showerror('Error in Sign up!', 'Password cannot be empty..')
        elif self.retype_password1 == '':
            self.retype_password.config(bg='#FA8273')
            messagebox.showerror('Error in Sign up!', 'Please retype the password..')
        elif self.retype_password1 != self.password1:
            self.retype_password.config(bg='#FA8273')
            messagebox.showerror('Error in Sign up!', 'Passwords do not match! Try again')

        else:
            self.insert_info = """INSERT INTO user_data
            (NAME, PASSWORD, GMAIL)
            VALUES(?, ?, ?)"""
            self.data = (self.name1, self.password1, self.email1)
            cursor.execute(self.insert_info, self.data)
            conn.commit()

            cursor.execute('select * from user_data')
            print(cursor.fetchall())
            conn.close()

    def check(self):
        if self.name.get().isspace()==False or self.name.get()!='':
            self.name.config(bg='#76FA73')

        if self.email.get().endswith('@gmail.com') and self.email.get()!='':
            self.email.config(bg='#76FA73')

        if (self.password.get().isalpha() != True or self.password.get().isalnum() != True) and self.password.get() != '':
            self.password.config(bg='#76FA73')

        if self.retype_password.get().strip() == self.password:
            self.retype_password.config(bg='#76FA73')

        return True


obj = signup(root)
root.mainloop()