import pandas as pd
import matplotlib.pyplot as plt

class Analysis :
    def __init__( self ) :
        pass

    def genericPlot( self , x , y , kind , ndata = 100 ) :
        x = x.get() ; y = y.get() ; kind = kind.get() ; ndata = ndata.get()
        df=pd.read_csv("covid_19_data.csv")
        df [[ "SNo" , y ]].iloc[:ndata].plot( x = "SNo" , y = y , kind = kind  )
        plt.xlabel(x)
        plt.ylabel(y)
        ticks = plt.xticks( df.SNo.iloc[:ndata:2] , df[x].iloc[:ndata:2] , rotation = "vertical" ) 
        self.showPlot()

 
    def graph_plot_1(self  ):
        df=pd.read_csv("covid_19_data.csv")
        # x=df['Country/Region'].iloc[:100]
        # y=df['Confirmed'][:100]
        df[['SNo' , "Confirmed"]].iloc[:100].plot.bar( x = 'SNo' , y = "Confirmed"  ) 
        plt.title('Graph shows the number of confirmed cases in country/region')
        plt.xlabel('country')
        plt.ylabel('Confirmed cases')

        # plt.bar(x,y)
        ticks = plt.xticks( df.SNo.iloc[:100:2] , df["Country/Region"].iloc[:100:2] ) 
        # print(x)
        self.showPlot()

    def showPlot(self) :
        plt.tight_layout()
        plt.show()

    def graph_plot_2(self ):
        df=pd.read_csv("covid_19_data.csv")
        # x=df['Country/Region'][:100]
        # y=df['Deaths'][:100]
        df[['SNo' , "Deaths"]].iloc[:100].plot.bar( x = 'SNo' , y = "Deaths"  ) 
        plt.title('Graph shows the number of death cases in country/region')
        plt.xlabel('country')
        plt.ylabel('death cases')
        ticks = plt.xticks( df.SNo.iloc[:100:2] , df["Country/Region"].iloc[:100:2] ) 
        # plt.bar(x,y)
        self.showPlot()

    def graph_plot_3( self ):
        df=pd.read_csv("covid_19_data.csv")
        # x=df['Country/Region'][:100]
        # y=df['Recovered'][:100]
        df[['SNo' , "Recovered"]].iloc[:100].plot.bar( x = 'SNo' , y = "Recovered"  ) 
        plt.title('Graph shows the number of recovered cases in country/region')
        plt.xlabel('country')
        plt.ylabel('death cases')
        # plt.bar(x,y)
        ticks = plt.xticks( df.SNo.iloc[:100:2] , df["Country/Region"].iloc[:100:2] ) 
        plt.show()