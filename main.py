    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as pt
import numpy as np

print("menu:"
      "\n1) data visualisation"
      "\n2) csv file"   
      "\n3) data manipulation"
      "\n4) read a brief summary")

i=int(input("choose any one option from the above: "))   
if i==1:
    print("1)display the literacy rate in india since 1901"
          "\n2)diplay the sex ratio in india since 1901"
          "\n3)diplay the infant mortality rate in india since 1900"
          "\n4)diplay the GDP of india since 1901"
          "\n5)diplay the import and export revenue of india since 1960"
          "\n6)diplay the inflation rate in india since 1960"
          "\n7)diplay the birth rate in india since 1950"
          "\n8)diplay the death rate in india since 1950"
          "\n9)diplay the fertility rate in india since 1950"
          "\n10)diplay the life expectancy in india since 1950")
    
    x=int(input("choose the option to be displayed: "))

    if(x==1):
        a=[1901,1911,1921,1931,1941,1951,1961,1971,1981,1991,2001,2011]
        b=[9.8,10.6,12.2,15.6,24.9,27.16,40.4,45.96,56.38,64.13,75.26,82.14]
        c=[0.6,1.0,1.8,2.9,7.3,8.86,15.35,21.97,29.76,39.29,53.67,65.46]
        d=[5.4,5.9,7.2,9.5,16.1,18.33,28.3,34.45,43.57,52.21,64.83,74.04]
        pt.plot(a,b,label="male")
        pt.plot(a,c,label="female")
        pt.plot(a,d,label="combined")
    
        pt.legend()
        pt.show()

    elif(x==2):
        a=[1901,1911,1921,1931,1941,1951,1961,1971,1981,1991,2001,2011]
        b=[972,964,955,950,945,946,941,930,934,927,933,943]
        pt.plot(a,b,label="sex ratio")

        pt.legend()
        pt.show()

    elif(x==3):
        a=[1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2020]
        b=[534.77,385.58,355.51,289.11,263.01,258.47,250,218,178,134,99,65,39]
        pt.plot(a,b,label="infant mortality rate")

        pt.legend()     
        pt.show()       

    elif(x==4):
        a=[1901,1911,1921,1931,1941,1951,1961,1971,1981,1991,2001,2011,2021     ]
        b=[7.666,11.822,25.337,26.389,44.085,108.633,186.821,501.199,1727.755,6622.605,23925.301,87363.287,236438.748]
        pt.plot(a,b,label="GDP of india (in billions rupees")

        pt.legend()
        pt.show()   

    elif(x==5):
        a=[1960,1970,1980,1990,2000,2010,2020]
        b=[1.68,2.36,11.44,22.64,60.88,375.35,499.10]
        c=[2.53,2.42,17.23,27.13,65.12,449.97,509.43]
        pt.plot(a,b,label="revenue earned by exports (in billion $)")
        pt.plot(a,c,label="money spent on imports (in billion $)")
        pt.legend()
        pt.show()

    elif(x==6):
        a=[1960,1970,1980,1990,2000,2010,2020]
        b=[1.78,5.09,11.35,8.97,4.01,11.99,6.62]
        pt.plot(a,b,label="inflation rate in india (in %)")
        pt.legend()
        pt.show()    

    elif(x==7):
        a=[1950,1960,1970,1980,1990,2000,2010,2020]
        b=[44.175,42.066,39.231,36.438,31.817,26.635,21.508,17.592]
        pt.plot(a,b,label="birth rate in india (in %)")
        pt.legend()
        pt.show()  

    elif(x==8):
        a=[1950,1960,1970,1980,1990,2000,2010,2020]
        b=[28.161,22.481,17.454,13.498,11.007,8.804,7.589,7.309]
        pt.plot(a,b,label="death rate in india (in %)")
        pt.legend()
        pt.show()      

    elif(x==9):
        a=[1950,1960,1970,1980,1990,2000,2010,2020]
        b=[5.907,5.894,5.598,4.857,4.093,3.346,2.636,2.2]
        pt.plot(a,b,label="fertility rate in india")
        pt.legend()
        pt.show() 

    elif(x==10):
        a=[1950,1960,1970,1980,1990,2000,2010,2020]
        b=[35.21,41.13,47.41,53.47,57.66,62.28,66.43,69.73]
        pt.plot(a,b,label="life expectancy in india")
        pt.legend()
        pt.show()

    else:
        print("please enter the correct number.")

if i==2:
    print("1)display the literacy rate in india since 1901"
          "\n2)diplay the sex ratio in india since 1901"
          "\n3)diplay the infant mortality rate in india since 1900"
          "\n4)diplay the GDP of india since 1901"
          "\n5)diplay the import and export revenue of india since 1960"
          "\n6)diplay the inflation rate in india since 1960"
          "\n7)diplay the birth rate in india since 1950"
          "\n8)diplay the death rate in india since 1950"
          "\n9)diplay the fertility rate in india since 1950"
          "\n10)diplay the life expectancy in india since 1950")
    
    p=int(input("choose the option to be displayed: "))

    if p==1:
        df=pd.read_csv("1.literacyrate.csv")
        print(df)
        
    elif p==2:
        df=pd.read_csv("2.Sex Rato.csv")
        print(df)
        
    elif p==3:
        df=pd.read_csv("3.IMR.csv")
        print(df)
        
    elif p==4:
        df=pd.read_csv("4.GDP.csv")
        print(df)
        
    elif p==5:
        df=pd.read_csv("5.Import Exprt.csv")
        print(df)
    
    elif p==6:
        df=pd.read_csv("6.inflation rate.csv")
        print(df)
        
    elif p==7:
        df=pd.read_csv("7.Birth Rate.csv")
        print(df)
        
    elif p==8:
        df=pd.read_csv("8.Death Rate.csv")
        print(df)    
        
    elif p==9:
        df=pd.read_csv("9.fertility rate.csv")
        print(df)   
        
    elif p==10:
        df=pd.read_csv("10.Life Expectancy.csv")
        print(df)  
        
    else:
        print("please enter the correct number.")
    