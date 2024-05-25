"""
Name: Shaik Mohammed Sohail
Student ID: 22028788
Course: 7PAM2004-0901-2023 - Data Handling and Visualisation
University: Msc Data Science
"""

import pandas as pd
import matplotlib.pyplot as plt

def readFile(file):
    '''
    Parameters
    ----------
    file: The filename is an argument parsed from the main function which name/path of the csv file

    Returns
    -------
    This function will read the csv file and return the dataframe
    '''
    
    db = pd.read_csv(file,skiprows = 4)
    
    return db

def transoose(df, indicator):
    '''
    Parameters
    ----------
    df: pandas DataFrame
        The DataFrame parsed from the main function.
    indicator: str
        The indicator code to filter the DataFrame.

    Returns
    -------
    pandas DataFrame
        The subset of the DataFrame, transposed with country names as column headers.
    '''
    # Filter the DataFrame for the specified indicator
    df = df[df["Indicator Code"] == indicator]

    # Filter for the countries of interest
    countries = ["China", "Germany", "United Kingdom", "United States", "India"]
    df = df[df["Country Name"].isin(countries)]

    # Define the period of interest
    period = ["2000", "2002", "2004", "2006", "2008", "2010", "2012", "2014", "2016", "2018", "2020", "2022"]

    available_columns = ["Country Name"] + period
    df = df[available_columns]

    df.set_index('Country Name', inplace=True)
    df_t = df.transpose()

    return df_t

    
def linePlot(df,title):
    '''
    Parameters
    ----------
    df : The data is parsed argument from main fnction which should be the dataframe type..

    Returns
    -------
    The function return nothng but plots the Line graph for the parsed data frame.
    '''
    df.plot(kind="line", figsize=(10, 5))
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel("Percentage of total withdrawl")
    plt.legend()
    plt.savefig(f'22028788_{title}.png', dpi=300)
    
def Bar(data,title):
    '''

    Parameters
    ----------
    data : The data is parsed argument from main fnction which should be the dataframe type..

    Returns
    -------
    The function return nothng but plots the bar graph for the parsed data frame.

    '''
    data = data.loc[:,["2000","2006","2010","2014"]]
    
    data.plot(kind="bar", figsize=(10, 5))
    plt.title(title)
    plt.xlabel("Countries")
    plt.ylabel("Percentage of Consumption")
    plt.legend()
    plt.savefig('22028788_bar.png', dpi=300)
    
def pieChart(plt1,plt2,plt3,plt4,labels):
    '''

    Parameters
    ----------
    data : The data is parsed argument from main fnction which should be the dataframe type..

    Returns
    -------
    The function return nothng but plots the bar graph for the parsed data frame.
    '''
    
    fig, ax = plt.subplots(2,2)
    ax[0,0].pie(plt1, labels=labels, autopct='%1.1f%%')
    ax[0,0].set_title("China")
    ax[0,1].pie(plt2, labels=labels, autopct='%1.1f%%')
    ax[0,1].set_title("India")
    ax[1,0].pie(plt3, labels=labels, autopct='%1.1f%%')
    ax[1,0].set_title("UK")
    ax[1,1].pie(plt4, labels=labels, autopct='%1.1f%%')
    ax[1,1].set_title("USA")
    fig.savefig("22028788_pie.png", dpi=300)

#main function

data = readFile("API_Download_DS2_en_csv_v2_487468.csv")

populationGrowth = transoose(data,"SP.POP.TOTL")

linePlot(populationGrowth,"Population Growth over the years")

co2emission = transoose(data,"EN.CO2.ETOT.ZS")

linePlot(co2emission,"CO2 Emission")

electric = transoose(data, "EG.ELC.FOSL.ZS")

Bar(electric.transpose(),"Electricity production from oil, gas and coal sources (% of total)")

gasesFuelDataframe = transoose(data, "EN.ATM.CO2E.GF.KT")
gasesFuelDataframe = gasesFuelDataframe.transpose()
liquidFuelDataframe = transoose(data, "EN.ATM.CO2E.LF.KT")
liquidFuelDataframe = liquidFuelDataframe.transpose()
solidFuelDataframe = transoose(data, "EN.ATM.CO2E.SF.KT")
solidFuelDataframe = solidFuelDataframe.transpose()

labels = ["Gasesous Fuel","Liquid Fuel","Solid Fuel"]

chinaSizes = [gasesFuelDataframe.loc['China', '2014'],liquidFuelDataframe.loc['China', '2014'],solidFuelDataframe.loc['China', '2014']]
indiaSizes = [gasesFuelDataframe.loc['India', '2014'],liquidFuelDataframe.loc['India', '2014'],solidFuelDataframe.loc['India', '2014']]
ukSizes = [gasesFuelDataframe.loc['United Kingdom', '2014'],liquidFuelDataframe.loc['United Kingdom', '2014'],solidFuelDataframe.loc['United Kingdom', '2014']]
usSizes = [gasesFuelDataframe.loc['United States', '2014'],liquidFuelDataframe.loc['United States', '2014'],solidFuelDataframe.loc['United States', '2014']]

pieChart(chinaSizes,indiaSizes,ukSizes,usSizes,labels)