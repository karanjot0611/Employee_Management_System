from customtkinter import *
from PIL import Image
from tkinter import ttk, VERTICAL, messagebox
import os
import database

#Functionality

def delete_all():
    result = messagebox.askyesno('Confirm','Do you really want to delete all the records?')
    if result:
        database.deleteall_records()
    else:
        pass
def show_all():
    treeview_data()
    searchBox.set('Search By')
    searchEntry.delete(0,END)
def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Enter Value to Search')
    elif searchBox.get()=='Search By':
        messagebox.showerror('Error', 'Select an option for Search!')
    else:
        searched_data = database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('', END, values=employee)
def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data for Deletion')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('Error', 'Data is Deleted')
def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to Update')
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is updated.')

def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])
def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    roleBox.set('Web Developer')
    genderBox.set('Male')
    salaryEntry.delete(0,END)
def treeview_data():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)
def add_employee():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error','All Fields are Required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error', 'Id already exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error', 'Invalid Id Format. Use "EMP" followed by a Number. eg-EMP1')
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is Added Successfully')
# Window setup
window = CTk()
window.title('Employee Management System')
window.geometry('930x580')
window.resizable(0, 0)
window.configure(fg_color='#161C30')

# Configure grid weights for better distribution
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)
window.grid_rowconfigure(1, weight=1)

# Load image safely (without this if image is not present in same folder it will show error)
if os.path.exists('bg.jpg'):
    logo = CTkImage(Image.open('bg.jpg'), size=(930, 158))
else:
    logo = None

logoLabel = CTkLabel(window, image=logo, text='')
logoLabel.grid(row=0, column=0, columnspan=2, sticky='nsew')

# Left Frame
leftFrame = CTkFrame(window, fg_color='#161C30')
leftFrame.grid(row=1, column=0, padx=(20, 10), pady=(5) ,sticky='nsew')
leftFrame.grid_rowconfigure(0, weight=1)

# ID
CTkLabel(leftFrame, text='Id', font=('arial', 18, 'bold'), text_color='white').grid(row=0, column=0, padx=20, pady=15, sticky='w')
idEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
idEntry.grid(row=0, column=1)

# Name
CTkLabel(leftFrame, text='Name', font=('arial', 18, 'bold'), text_color='white').grid(row=1, column=0, padx=20, pady=15, sticky='w')
nameEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
nameEntry.grid(row=1, column=1)

# Phone
CTkLabel(leftFrame, text='Phone', font=('arial', 18, 'bold'), text_color='white').grid(row=2, column=0, padx=20, pady=15, sticky='w')
phoneEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
phoneEntry.grid(row=2, column=1)

# Role
CTkLabel(leftFrame, text='Role', font=('arial', 18, 'bold'), text_color='white').grid(row=3, column=0, padx=20, pady=15, sticky='w')
roleBox = CTkComboBox(leftFrame, values=['Web Developer', 'Cloud Engineer', 'DevOps Engineer', 'Cybersecurity Eng.',
                                         'IT Support', 'UI/UX Designer', 'Data Scientist', 'Business Analyst'],
                      font=('arial', 15, 'bold'), width=180, state='readonly')
roleBox.grid(row=3, column=1)
roleBox.set('Web Developer')

# Gender
CTkLabel(leftFrame, text='Gender', font=('arial', 18, 'bold'), text_color='white').grid(row=4, column=0, padx=20, pady=15, sticky='w')
genderBox = CTkComboBox(leftFrame, values=['Male', 'Female', 'Others'], font=('arial', 15, 'bold'), width=180, state='readonly')
genderBox.grid(row=4, column=1)
genderBox.set('Male')

# Salary
CTkLabel(leftFrame, text='Salary', font=('arial', 18, 'bold'), text_color='white').grid(row=5, column=0, padx=20, pady=15, sticky='w')
salaryEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
salaryEntry.grid(row=5, column=1)

# Right Frame
rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1, sticky='nsew', padx=(10,10), pady=(15,20))
rightFrame.grid_rowconfigure(0, weight=0)
rightFrame.grid_rowconfigure(1, weight=1)
rightFrame.grid_columnconfigure((0,1,2,3), weight=1)

# Search section
searchBox = CTkComboBox(rightFrame, values=['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary'], state='readonly')
searchBox.grid(row=0, column=0, padx=5, pady=5, sticky='w')
searchBox.set('Search By')

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

searchButton = CTkButton(rightFrame, text='Search', width=100,command=search_employee)
searchButton.grid(row=0, column=2, padx=5, pady=5)

showallButton = CTkButton(rightFrame, text='Show All', width=100, command=show_all)
showallButton.grid(row=0, column=3, padx=5, pady=5)

# Treeview
tree = ttk.Treeview(rightFrame, height=13)
tree.grid(row=1, column=0, columnspan=4, sticky='nsew', pady=(5, 0))


tree['columns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')
for col in tree['columns']:
    tree.heading(col, text=col)
    tree.column('Id', width=60,anchor='center')
    tree.column('Name', width=120,anchor='center')
    tree.column('Phone', width=80,anchor='center')
    tree.column('Role', width=120,anchor='center')
    tree.column('Gender', width=90,anchor='center')
    tree.column('Salary', width=100,anchor='center')
tree.config(show='headings')

style = ttk.Style()
style.configure('Treeview.Heading', font=('arial', 16, 'bold'))
style.configure('Treeview', font=('arial', 10, 'bold'),rowheight=30,background="#161C30",foreground='white')

scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1, column=4, sticky='ns')
tree.config(yscrollcommand=scrollbar.set)

# Buttons
buttonFrame = CTkFrame(window, fg_color='#161C30')
buttonFrame.grid(row=2, column=0, columnspan=2, pady=5)
buttonFrame.grid_columnconfigure((0,1,2,3,4), weight=1)

newButton= CTkButton(buttonFrame, text='New Employee', font=('arial', 15, 'bold'), width=160,corner_radius=15,command=lambda: clear(True)).grid(row=0, column=0, pady=5, padx=5)
addButton= CTkButton(buttonFrame, text='Add Employee', font=('arial', 15, 'bold'), width=160,corner_radius=15,command = add_employee).grid(row=0, column=1, pady=5, padx=5)
updateButton= CTkButton(buttonFrame, text='Update Employee', font=('arial', 15, 'bold'), width=160,corner_radius=15,command = update_employee).grid(row=0, column=2, pady=5, padx=5)
deleteButton= CTkButton(buttonFrame, text='Delete Employee', font=('arial', 15, 'bold'), width=160,corner_radius=15, command=delete_employee).grid(row=0, column=3, pady=5, padx=5)
deleteallButton= CTkButton(buttonFrame, text='Delete All Employees', font=('arial', 15, 'bold'), width=180,corner_radius=15, command=delete_all).grid(row=0, column=4, pady=5, padx=5)


treeview_data()
window.bind('<ButtonRelease>',selection)

window.mainloop()
