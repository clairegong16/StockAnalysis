# Import the yfinance. If you get module not found error the run !pip install yfinance from your Jupyter notebook
import yfinance as yf
# Import the plotting library
import matplotlib.pyplot as plt
import pandas as pd #for understanding https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html
import sys #for file 

import mathstock
'''
plot single chart
'''
'''
# Get the data for the stock AAPL
data = yf.download('AAPL','2020-01-01','2020-08-01')
print(data.head())
print(data.at['2020-01-02','Close'])
# Plot the close price of the AAPL
data['Adj Close'].plot()
plt.show() #shows the graph to the user

'''

# Define the ticker list

stockslist = ['AAPL', 'AMZN', 'GOOGL', 'WMT', 'IBM', 'MSFT']

# Fetch the data
date1 = '2000-01-01'
date2 = '2020-12-01'
data = yf.download(stockslist, date1, date2)
'''data['Adj Close'].plot()
plt.show()'''
# Print first 5 rows of the data
#print(data.head(5))


#print("data mean:\n", data.mean(axis=0))


#for finding difference between beginning and end. 

for company in stockslist:
    print(company)  
    datas = yf.download(company, date1, date2)  #gets the data of the company between the given dates.
    print("datas:\n", datas)  
    pd.set_option('display.max_rows', len(datas))  #this is here to get all of the data shown in the text file. 

    #the following section is to put the data into a text file:
    with open(company + '.stock.txt', 'w') as stocks: 
        print(datas, file=stocks)
    pd.reset_option('display.max_rows') #reset the length 

# returns the y list given the year and month 
def dates_to_value_list(company, year, month):
  
    if month == '12':
        month2 = '-01'
        year2 = int(year) + 1 
    else:
        month2 = '-02'
        year2 = year 
    with open(company + '.stock.txt') as f: #this opens the text file as a file  
        '''for line in f:
            print(line)'''  #another way to know when to stop reading the file 
        stopper = False #for the while loop below 
        foundbeginning = False 
        ylist = []
        while stopper != True:
            line = f.readline()
            if len(line) == 0:
                break
            #locating the beginning date 
            if line.find(str(year) + '-' + month) != -1:  #.find finds the index that the substring is in.
                foundbeginning = True 
            #locating the end date
            if foundbeginning == True: 
                x = line.split()
                ylist.append(float(x[5]))
                if line.find(str(year2) + month2) != -1: #should stop at 2018-01-xx
                    stopper = True
        if len(line) == 0:
            print("year,month,month2,foundbeginning:", year, month, month2, foundbeginning, "fail to locate the date in the file.")
        return ylist
    

def plotm_and_b(m,b,ylist, company, year, month, plot):
    y_list = []
    for i in range(0,len(ylist)):
        y = m*(i+1)+b
        y_list.append(y)
    if plot == True:
        plt.plot(y_list, color ='blue', label= "line of best fit")
        plt.plot(ylist, color ='red', label = "actual")
        plt.legend()
        plt.title(company + ' ' + str(year) + ' ' + month, loc='right')
        plt.savefig('plots/' + company + str(year)+ month +'.png')
        plt.show()
#my all in one function to loop over through multiple companies:

''' dec = dates_to_value_list('2018-12-03', '2018-12-31', 'MSFT')
jan = dates_to_value_list('2019-01-02', '2019-01-31', 'MSFT')'''

def main(stocklist, d_begdate): #, d_enddate, j_begdate, j_enddate):
    yearlist = findingyears(d_begdate, 10)
    markerlist = ['o', '.', 'x', '+', 'v', '^', '<', '>', 's', 'd']
    colorlist = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    a = 0
    for i in stocklist:
        mdeclist = [] # slopes list 
        mjanlist = []
        marker = markerlist[a]
        color = colorlist[a]
        for j in yearlist: 
            dec = dates_to_value_list(i, j, '12')
            jan = dates_to_value_list(i, j, '01')
            #normalized mdec
            mdec,bdec = mathstock.calcm_and_b(dec, i)
            n_mdec = mdec*(len(dec))/bdec
            mdeclist.append(n_mdec)
            plotm_and_b(mdec,bdec,dec, i, j, 'DEC', True)

            mjan,bjan = mathstock.calcm_and_b(jan, i)
            n_mjan = mjan*(len(jan))/bjan
            mjanlist.append(n_mjan)
            plotm_and_b(mjan,bjan,jan, i, int(j) + 1, 'JAN', True)
        a = a + 1

        plt.plot(mdeclist, mjanlist, marker, color =color, label = i)
        plt.xlabel('slope dec')
        plt.ylabel('slope jan')
        '''plt.xlim(-12,12)
        plt.ylim(-12,12)'''
        plt.legend()
        plt.savefig('plots/' + i + '_scatter' +'.png')
        plt.show()
        plt.close()
       


#input is for example ('2018-12-03', 1) output is 2018. ex. ('2018-12-03', 5) output is 2014,2015,2016,2017,2018
def findingyears(d_begdate, yearnumber): 
    enddec = int(d_begdate[:4])
    startdec = enddec- (yearnumber-1)
    yearlist = []
    while startdec <= enddec:
        yearlist.append(startdec)
        startdec = startdec + 1
    return yearlist

main(stockslist,'2019-12')  









    




