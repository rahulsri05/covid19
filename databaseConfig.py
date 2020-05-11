from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column , Integer , Numeric ,String  ,func , Date , DateTime
from datetime import datetime as dt
import pandas as pd

username = "username"
password = "password"
dbname = "testdb"

engine = create_engine (  f"postgresql://{username}:{password}@localhost:5432/{dbname}" )

Session = sessionmaker ( bind = engine )

session = Session ( )
Base =declarative_base ( )

class Users (Base):
	__tablename__ = "users"
	username = Column( String(100) , primary_key = True )
	password = Column ( String(100) , nullable = False )

	def __init__( self , username , password ) :
		self.username = username
		self.password = password

class Admin (Base):
	__tablename__ = "admin"
	adminName = Column ( String(100) , primary_key = True )
	password = Column ( String( 100) , nullable = False )

	def __init__( self , adminName , password ) :
		self.adminName = adminName
		self.password = password

class loginInfo ( Base ) :
	__tablename__ = "loginInfo"
	username = Column ( String(100) , primary_key = True )
	timeString = Column ( String (100) ,  nullable = False)

	def __init__ ( self , username ) :
		self.username = username
		self.timeString = dt.now().strftime("%m/%d/%y %H:%M:%S")

class covidData( Base ) :
	__tablename__ = "covid_data"
	id = Column( Integer , primary_key = True )
	obsrvDate = Column( Date , nullable = False )
	State = Column( String(100) , nullable = False )
	Region = Column( String( 100) , nullable = False )
	lastUpd = Column ( DateTime , nullable = False )
	Confirmed = Column( Integer , nullable = False )
	Deaths = Column ( Integer , nullable = False )
	Recovered = Column ( Integer , nullable = False  )

	def __init__( self , obsrvDate , State , Region , 
	lastUpd , Confirmed , Deaths , Recovered ) :
		self.obsrvDate = obsrvDate
		self.State = State
		self.Region = Region
		self.lastUpd = lastUpd
		self.Confirmed = Confirmed
		self.Deaths = Deaths
		self.Recovered = Recovered

def updateCovidData( fileName ) :
	df = pd.read_csv( fileName , index_col= 0  )
	df.columns = ['obsrvDate' , 'State' , 'Region' ,'lastUpd' ,
	 'Confirmed' , 'Deaths' , 'Recovered'] 
	try :
		session.bulk_insert_mappings( covidData , df.to_dict(orient = "records") ) 
		session.commit()
		print("Updated Successfully")
	except Exception as e :
		print(e)	
		session.rollback()



if __name__ == "__main__" :
	pass
	#Base.metadata.create_all ( bind = engine )
	#updateCovidData( fileName="fileName" )


