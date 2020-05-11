import tkinter
from tkinter import *
from tkinter import messagebox
from functools import partial
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Analysis import Analysis 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from databaseConfig import *
import time
from tkinter import ttk

class covidConfig(Analysis) :

    def __init__( self  ) :
        Analysis.__init__(self)
        self.data = pd.read_sql( session.query(covidData).__str__(), con = engine )
        self.data.columns = ['SNo', 'ObservationDate', 'Province/State', 'Country/Region',
       'Last Update', 'Confirmed', 'Deaths', 'Recovered']
        self.plotOptions = ["line" , "bar" , "barh" ,
        "hist" , "box" , "density" , "area" , "scatter"
        ]

    def Message( self , title , message) :
        messagebox.showinfo( title=title , message=message )

    def open_window( self ):
        top = Toplevel()
        top.title("top window")
        top.geometry("300x300+120+120")        
        button1 = Button(top, text="confirmed", command=self.graph_plot_1)
        button1.grid(row=0,column=1)
        button2=Button(top,text="death",command=self.graph_plot_2)
        button2.grid(row=0,column=2)
        button3=Button(top,text="recovered",command=self.graph_plot_3)
        button3.grid(row=0,column=3)
        top.mainloop()

    def prediction( self ):
        top= Toplevel()
        top.title("top window")
        top.geometry("300x300+120+120")
        button1=Button(top, text=" Prediction score of death", command=self.display).grid(row=0,column=1)
        button2=Button(top, text=" Prediction score of recovered", command=self.display1).grid(row=0,column=2)
        top.mainloop()

    def display1( self ):
        df = self.data
        x=df[['Confirmed']]
        y=df[['Recovered']]       
        x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.3)
        clf=LinearRegression()
        clf.fit(x_train,y_train)
        clf.predict(x_test)
        score=clf.score(x_test,y_test)
        per=100*score
        print("percentage of correctectness of the prediction=",per)

    def display(self ):
        df = self.data  
        x=df[['Confirmed']]
        y=df[['Deaths']]
        x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.3)
        clf=LinearRegression()
        clf.fit(x_train,y_train)
        clf.predict(x_test)
        score=clf.score(x_test,y_test)
        per=100*score
        print("percentage of correctness of the prediction= ",per)
        
    def adminvalidate(self , adminname,adminpassword):
        if adminname.get()=='' or adminpassword.get()=='':
            self.Message( title = "Warning", message = 'All fields required')
        elif session.query( Admin ).filter( 
            Admin.adminName == adminname.get() , 
            Admin.password == adminpassword.get() ).first() :
            # self.open_window()
            self.prediction()
        # if username.get()=='s' and password.get()=='p':
        else:
            self.Message( title = "Error" , message = 'Enter the correct id and password' )
    def register( self , regFunc ) :
        top= Toplevel()
        print("OK")
        top.title("Registration Window")
        usernameLabel = Label(top, text="User Name").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(top, textvariable=username).grid(row=0, column=1)  

        #password label and password entry box
        passwordLabel = Label(top,text="Password").grid(row=1, column=0)  
        password = StringVar()
        passwordEntry = Entry(top, textvariable=password, show='*').grid(row=1, column=1)  
        adduser = partial( regFunc , username , password ,top )
        loginButton = Button(top, text="Signup", command=adduser).grid(row=1, column=2)  
        top.mainloop()

    def addUser ( self , username , password , top ) :
        user = Users( username=username.get() , password = password.get())
        session.add ( user )
        self.COMMIT(top)

    def addAdmin ( self , username , password , top ) :
        admin = Admin ( adminName=username.get() , password= password.get())
        session.add( admin )
        self.COMMIT(top)

    def COMMIT( self , top  ) :
        try:
            session.commit()
            self.Message ( "Success", message = "You have added successfully")
        except Exception as e :
            # print ( e )
            session.rollback()
            self.Message( "Warn" , message= "username already Registered,Try New" )
        top.destroy()

    def validateLogin( self , username, password):
        if username.get()=='' or password.get()=='':
            self.Message( title = "Warning", message = 'All fields required')
        elif session.query( Users ).filter( 
            Users.username == username.get() , 
            Users.password == password.get() ).first() :
            # self.open_window()
            self.statsWindow()
        # if username.get()=='s' and password.get()=='p':
        else:
            self.Message( title = "Error" , message = 'Enter the correct id and password' )

    def customLables( self , top , text , column , row ) :
        Label( top , text = text ).grid( column = column , row = row )

    def statsWindow( self   ) :
        top = Toplevel(  )
        [self.customLables (top, text, column, row) for 
        top , text, column , row in  
            [[top , "choose plot type:" , 0, 0 ] , 
             [top , "choose x axis" , 1 , 0] ,
             [top , "choose y axis" , 2 , 0] , 
             [top , "Enter size of data" , 3 , 0] 
                ] 
             ]
        top.title("Statistics")
        top.geometry("750x250")
        plot = StringVar()
        plotOptions = ttk.Combobox(top , 
            textvariable = plot)
        x = StringVar()
        xline = ttk.Combobox(top ,
            textvariable = x )
        y = StringVar()
        yline = ttk.Combobox(top ,
            textvariable = y )
        size = IntVar()
        sizeOfData = ttk.Combobox(top , 
            textvariable = size )

        plotOptions["values"] = self.plotOptions
        xline["values"] = list( self.data.columns )
        yline["values"] = list( self.data.columns )

        plotOptions.grid(column = 0 ,row = 1 )
        xline.grid(column=1 , row =1 )
        yline.grid( column= 2 , row = 1  )
        sizeOfData.grid(column =3 , row =1  )
        genPlot = partial (self.genericPlot , x , y , plot , size )
        Button(top, text="Apply", command=genPlot ).grid(
            row=2,column=3)

        top.mainloop()



    #window

if __name__ == "__main__" :
    pass
