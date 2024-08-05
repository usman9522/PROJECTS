from tkinter import *
from tkinter import messagebox
from PIL import ImageTk  # require pillow for jpeg images
from cinemadatabase import *

window2 = Tk()
window2.title("Signup Page.")
window2.geometry("996x560+90+50")
window2.resizable(False, False)

# checking all entries are filled or not
def on_signup_click():
    username = username_entry.get()
    password = pass_entry.get()
    confirm_password = confirm_pass_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()
    placeholder_texts = ["Enter Username", "Enter Password", "Confirm Password", "Enter Email", "Enter Mobile No", '']
    if username in placeholder_texts or password in placeholder_texts or confirm_password in placeholder_texts \
            or email in placeholder_texts or mobile in placeholder_texts:
        messagebox.showerror("Error", "All fields must be filled")
    elif password != confirm_password:
        messagebox.showerror("Error", "Password and Confirm Password do not match")
    else:
        add_user(connection, username, password, mobile, email)
        messagebox.showinfo("Signup Completed", "Signup completed successfully")
        window2.destroy()
        import signin

def back_to_signin():
    window2.destroy()
    import signin

# setting background image
bgimage = ImageTk.PhotoImage(file='bg2.jpg')
bglabel = Label(window2, image=bgimage)
bglabel.place(x=0, y=0)

# HEADER PORTION
header = Label(window2, text='SIGNUP INFO')
header.config(font=("Helvetica", 30, 'bold'), bg="#C72928", fg='white')
header.place(x=140, y=60)
# white line below header
frame1 = Frame(window2, width=450, height=2, bg="white")
frame1.place(x=50, y=135)

# USERNAME
username_label = Label(window2, text='Username:')
username_label.config(font=("Helvetica", 12, 'bold'), bg="#C72928", fg='white')
username_label.place(x=100, y=180)
username_entry = Entry(window2, width=20, font=("Helvetica", 11), fg='black')
username_entry.place(x=210, y=180)
# placeholder
username_entry.insert(0, "Enter Username")
# delete placeholder on click
username_entry.bind("<Button-1>", lambda event: username_entry.delete(0, END))

# PASSWORD
pass_label = Label(window2, text='Create\nPassword:', justify=LEFT)
pass_label.config(font=("Helvetica", 12, 'bold'), bg="#C72928", fg='white')
pass_label.place(x=100, y=220)
pass_entry = Entry(window2, width=20, font=("Helvetica", 11), fg='black')
pass_entry.place(x=210, y=225)
# placeholder
pass_entry.insert(0, "Enter Password")
# delete placeholder on click
pass_entry.bind("<Button-1>", lambda event: pass_entry.delete(0, END))

# CONFIRM PASSWORD
confirm_pass_label = Label(window2, text='Confirm\nPassword:', justify=LEFT )
confirm_pass_label.config(font=("Helvetica", 12, 'bold'), bg="#C72928", fg='white')
confirm_pass_label.place(x=100, y=270)
confirm_pass_entry = Entry(window2, width=20, font=("Helvetica", 11), fg='black')
confirm_pass_entry.place(x=210, y=273)
# placeholder
confirm_pass_entry.insert(0, "Confirm Password")
# delete placeholder on click
confirm_pass_entry.bind("<Button-1>", lambda event: confirm_pass_entry.delete(0, END))

# EMAIL
email_label = Label(window2, text='Email:')
email_label.config(font=("Helvetica", 12, 'bold'), bg="#C72928", fg='white')
email_label.place(x=100, y=320)
email_entry = Entry(window2, width=20, font=("Helvetica", 11), fg='black')
email_entry.place(x=210, y=320)
# placeholder
email_entry.insert(0, "Enter Email")
# delete placeholder on click
email_entry.bind("<Button-1>", lambda event: email_entry.delete(0, END))

# MOBILE NUMBER
mobile_label = Label(window2, text='Mobile No:')
mobile_label.config(font=("Helvetica", 12, 'bold'), bg="#C72928", fg='white')
mobile_label.place(x=100, y=360)
mobile_entry = Entry(window2, width=20, font=("Helvetica", 11), fg='black')
mobile_entry.place(x=210, y=360)
# placeholder
mobile_entry.insert(0, "Enter Mobile No")
# delete placeholder on click
mobile_entry.bind("<Button-1>", lambda event: mobile_entry.delete(0, END))

# SIGNUP BUTTON
signup_button = Button(window2, text='SIGNUP', width=9,
                       font=("Helvetica", 9, 'bold'), bg="white", fg='#C72928',
                       command=on_signup_click)
signup_button.place(x=240, y=400)


# BACK TO SIGNIN BUTTON
back_button = Button(window2, text=' GO BACK ', width=15,
                     font=("Helvetica", 9, 'bold'), bg="white", fg='#C72928',
                     command=back_to_signin)
back_button.place(x=170, y=450)

# CLOSE
window2.mainloop()
