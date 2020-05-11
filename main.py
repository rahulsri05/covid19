from tkinter import *
from functools import partial
from covid import covidConfig 

ccg = covidConfig (  )

tkWindow = Tk()  
tkWindow.geometry('400x300')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(ccg.validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=1, column=2)  

adminnamelabel= Label(tkWindow, text="admin Name").grid(row=5, column=0)
adminname = StringVar()
adminnameEntry = Entry(tkWindow, textvariable=adminname).grid(row=5, column=1)

adminpasswordlabel= Label(tkWindow, text="password").grid(row=6,column=0)

adminpassword=StringVar()

adminpasswordEntry = Entry(tkWindow, textvariable=adminpassword, show="*").grid(row=6, column=1)

adminvalidate=partial(ccg.adminvalidate, adminname,adminpassword)

login=Button(tkWindow, text="Login", command=adminvalidate).grid(row=6,column=2)

userFunc = partial ( ccg.register ,  ccg.addUser )
userRegistration = Button ( tkWindow , text = "User Signup" , command = userFunc ).grid( row = 7, column = 2 )
adminFunc = partial ( ccg.register , ccg.addAdmin )
adminRegistration = Button ( tkWindow , text = "For Admin..." , command = adminFunc ).grid( row = 8, column = 2 )


tkWindow.mainloop()