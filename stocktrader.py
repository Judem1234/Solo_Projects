# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:45:14 2021

@author: judem
"""
import os

from tabulate import tabulate

class TransactionError(Exception):
    pass

class DateError(Exception):
    pass

stocks = {}
portfolio = {}
transactions = []

# Question 1

def normaliseDate(s):
 """
    This function takes a date and changes it into a the format YYYY-MM-DD
    Parameters
    ----------
    s : s is the input date that is of the correct input format
    Raises
    ------
    DateError
        If the input date is not of the correct format, 
        a DateError is raised
    Returns
    -------
    s : The function return the inputed date in the format YYYY-MM-DD
 """   
 s= s.replace('.','-')
 s= s.replace('/','-')
 s= "-" + s + "-"
 s= s.replace('-1-','-01-') 
 s= s.replace('-2-','-02-')
 s= s.replace('-3-','-03-')
 s= s.replace('-4-','-04-')
 s= s.replace('-5-','-05-')
 s= s.replace('-6-','-06-')
 s= s.replace('-7-','-07-')
 s= s.replace('-8-','-08-')
 s= s.replace('-9-','-09-')
 s = s[1:len(s)-1]

 if s[7] != "-":  
   p= s[0:2]  
   s = "+" + s # the plus is used for if the months are the same  
   x=s[0:3]
   s=s.replace(x,s[7:11])
   s = s + "to not make same on each side"
   s= s.replace(s[8:],p)  

 if len(s)!= 10 or s[0] == "-" or s[9] == "-" :     
     raise DateError("wrong input")
 return s 
 
# Question 2

def loadStock(symbol):
 """
    This function loads all the stocks of a csv file that you choose
    Parameters
    ----------
    symbol : symbol is the file name of a csv stock file in the Directory
    after running this function it should load all of the data into the stocks dictionary.

  """   
 filename= symbol + '.csv'
 with open(filename, mode="rt", encoding= 'utf8') as f:
        f.readline() #Skip first line
        indivstocks={}
        stocks[symbol]= indivstocks
        for line in f:
            column = line.split(',')
            indivstocks[normaliseDate(column[0])]= [float(column[1]),float(column[2]),float(column[3]),float(column[4])]
            #only works if in correct format
   
# Question 3
            
def loadPortfolio(fname='portfolio.csv'): 
 """
    This function will load the information of a csv file into the portfolio dictionary
    Parameters
    ----------
    fname : Type, optional
    the input fname is the name of the csv file of
    a correctly formatted portfolio. The default is 'portfolio.csv'.
   Raises
    ------
    ValueError
        This occurs when the portofolio csv file is not of the correct format
        i.e if the date input is wrong
   Returns
    -------
    None. But the information is loaded to the portfolio dictionary

 """    
 with open(fname, mode="rt", encoding= 'utf8') as f:    
        h=-1
        for line in f:    
         h+= 1
         line= line.strip()
         value = line.split(',') 
         if h == 0:
             try :
                portfolio["date"] =  normaliseDate(value[0]) 
             except DateError:
                raise ValueError("the portfolio has wrong date input")
         if h == 1:
             portfolio["cash"] = float(value[0])
             if (portfolio["cash"]*100) // 1 != (portfolio["cash"]*100):
               raise ValueError("you can't have 1 tenth of a pence")
         if h > 1:
             portfolio[value[0]] = int(value[1])
             loadStock(value[0])
           
                                        
def Earlydate(date):
   """
    This function will raise and error if the date is earlier than the portfolio date
    Parameters
    ----------
    date : The input date is any date
    Raises
    ------
    DateError
        An error is raised if the date is earlier than the date of the portfolio
        which is the main reason for the function
    Returns
    -------
    None.

    """ 
   date= normaliseDate(date) 
   portdate= portfolio["date"]
   if date[0:4] < portdate[0:4]:
      raise DateError("date is earlier than date of portfolio")
   if date[0:4] == portdate[0:4]:
       if date[5:7] < portdate[5:7]:
           raise DateError("date is earlier than date of portfolio")
       if date[5:7] == portdate[5:7]:
          if date[8:] < portdate[8:]:
             raise DateError("date is earlier than date of portfolio")

#Question 4 
                       
def valuatePortfolio(date = 1,verbose=False):
    """
    This function will evaluate your portfolio dictionary
    Parameters
    ----------
    date : Type, optional
        The date you want to valuate the portfolio. The default is portfolio["date"].
    verbose : Type, optional
        If False, only the Total value is returned
        If True a table is printed breaking down all the values, The default is False.
    Raises
    ------
    ValueError
        ValueError is raised when it is not a trading day
    Returns
    -------
    totalvalue : the function returns the total value of the portfolio

    """
    if date == 1:
        date = portfolio["date"] 
    date= normaliseDate(date) 
    Earlydate(date)
    lst= list(portfolio)
    h = portfolio
    totalvalue=h["cash"]
    elem_of_list= 2
    if verbose == True:
       table = [['Capital type', 'Volume', 'Val/Unit*','Value in £*'],[ 'Cash', '1', portfolio["cash"], portfolio["cash"]]]  
    while elem_of_list < len(lst):
       symbol=lst[elem_of_list]
       try:
           values_of_stocks_on_day= (stocks[symbol])[date]
       except KeyError:
           raise ValueError("not a trading day")
       value= values_of_stocks_on_day[2]*portfolio[symbol]
       elem_of_list += 1
       totalvalue += value
       if verbose == True:
           table.append(["shares of {}".format(symbol),portfolio[symbol],format(values_of_stocks_on_day[2],'.2f'),format(value,'.2f')])      
    totalvalue = format(totalvalue, '.2f')
    if verbose == True:
        print("Your portfolio on {}:".format(date))
        print("[* share values based on the lowest price on {}]".format(date))
        print(tabulate(table, headers='firstrow', tablefmt='grid')) 
        print("TOTAL VALUE                                       {}".format(totalvalue))  
    return totalvalue   


#Question 5
    
def addTransaction(trans,verbose= False):  
   """
    This function will add a transaction to your portfolio and update the transactions list
    
    Parameters
    ----------
    trans : the trans input is a transaction you want to make of the form
    date,symbol,volume.
    verbose : TYPE, optional
        If verbose is False, the transaction is added without documentation
        If verbose is True, the transaction is added and fully documented. The default is False.

    Raises
    ------
    TransactionError
       If there is an error with the transaction a TransactionError is raised
       with a appropriate message

    Returns
    -------
    None.

    """ 
   trans["date"]= normaliseDate(trans["date"])
   transdate= trans["date"]
   Earlydate(transdate)  
   portfolio["cash"]
   t=stocks[trans["symbol"]]
   trans_date= t[trans["date"]]
   try:
       portfolio[trans["symbol"]]
   except KeyError:
       portfolio[trans["symbol"]] = 0 # when you want to add stocks of a stock you don't have
   if (portfolio[trans["symbol"]] + trans["volume"]) < 0:
     raise TransactionError("we have sold more stocks than we have")   
   if trans["volume"] < 0:
    portfolio["cash"] += -trans["volume"]*trans_date[2]
    if verbose == True:
     print('{} : Sold {} Shares of {} for a total of £{}, Available cash: £{}'.format(transdate,-trans["volume"],trans["symbol"],-trans["volume"]*trans_date[2],portfolio["cash"]))
   if trans["volume"] > 0:
    if portfolio["cash"] - trans["volume"]*trans_date[1] < 0:
        raise TransactionError ("We dont have enough cash to buy this many stocks")
    portfolio["cash"] +=  -trans["volume"]*trans_date[1]
    if verbose == True:
     print('{} : Bought {} Shares of {} for a total of £{}, Available cash: £{}'.format(transdate,trans["volume"],trans["symbol"],trans["volume"]*trans_date[1],portfolio["cash"]))
   portfolio[trans["symbol"]] += trans["volume"]
   if portfolio[trans["symbol"]] == 0:
      portfolio.pop(trans["symbol"]) #remove stock from portfolio
   portfolio["date"]= trans["date"]
   transactions.append(trans)

#Question 6 
   
def savePortfolio(fname="portfolio.csv"): 
 """
    This function saves the portfolio dictiory into a new CSV file. 
   
    Parameters
    ----------
    fname : TYPE, optional
        This is the name of a new csv that you want to save 
        the portfolio dictonary information into. The default is "portfolio.csv".

    Returns
    -------
    None.

  """
 with open(fname,mode="wt", encoding="utf8") as f:
     p= list(portfolio)
     f.write("%s \n%s \n" % (portfolio[p[0]], portfolio[p[1]]))
     h= 2
     while h< len(p):
         f.write(p[h])
         f.write(",")
         f.write("%s \n" % (portfolio[p[h]]))
         h += 1
     f.close() 
      
#Question 7 
    
def sellAll(date = 1,verbose=False):
    """
    This function will sell all of the stocks you posses

    Parameters
    ----------
    date : TYPE, optional
        This is the date in which you want to sellAll of 
        the stocks in your portfolio. The default is portfolio["date"].
    verbose : TYPE, optional
        If verbose is True, all the transactions that 
        were made are printed. The default is False.

    Raises
    ------
    DateError
        If you try sell the stocks on a non trading day
        a DateError is raised

    Returns
    -------
    None.

    """
    if date == 1:
       date = portfolio["date"]
    date = normaliseDate(date)
    Earlydate(date)
    p= list(portfolio)
    h=2
    l = len(transactions)
    while h< len(p):
        totvol= portfolio[p[h]]
        try: 
            addTransaction({'date':date, 'symbol':p[h], 'volume':-totvol })
        except KeyError:
            raise DateError("not a trading day")
        h += 1
    if verbose == True: 
       while l< len(transactions): 
          print(transactions[l])
          l += 1
 
#Question 8                
       
def loadAllStocks(): 
 """
    This function will load all of the stocks from a directory into
    the stocks dictionary

    Returns
    -------
    None.

 """  
 # The followoing code is similar to the one on     
 # https://www.geeksforgeeks.org/python-list-files-in-a-directory/ 
 folder = 'C:/Users/judem/OneDrive/Desktop/Python/Final Coursework/Stocks directory'
 dir_list = os.listdir(folder)
 
 h=0
 while h < len(dir_list):
  p=dir_list[h]
  try:
      loadStock(p.split(".")[0])
  except Exception:
      pass
  h += 1
  
# most of next functions are to help with question 9  


def NextTradingDay():
 """
 This function will move the date of the portfolio to the 
 next trading day
 """
 date = portfolio["date"]
 stocklst= list(stocks)     
 p= list(stocks[stocklst[0]])
 h=0
 while h < len(p):
     if p[h] == date:
         break
     h += 1
 if h == len(p)-1:
   raise ValueError # the last trading day
 else:  
   portfolio["date"] = p[h+1]
 return portfolio["date"]


def Quotient(h, symbol): 
 """
    This function calculates the quotient of a stock

    Parameters
    ----------
    h : h is the date you want to evaluate the quotient 
    symbol : the quotient of the symbol you want to evauluate

    Returns
    -------
    Quotient : This function returns the quotient of the the date
    with the previous 9 days

    """   
 h= normaliseDate(h)
 stocklst= list(stocks)     
 p= list(stocks[stocklst[0]])
 t= 0
 Q_divisor=0
 StocksOnFirstDay=(stocks[symbol])[h]
 day = 0 
 while day < len(p):
     if p[day] == h:
         break
     day += 1
 day += 1    
 while t<10 :  
  h= p[day-1]
  StocksOnDay=(stocks[symbol])[h]
  Q_divisor += StocksOnDay[1]  
  t += 1
  day += -1
 Quotient=10*StocksOnFirstDay[1]/Q_divisor
 return Quotient

 
def BestChoice():
 """
    This function will tell you which stock in stocks dictionary has highest quotient
    Returns
    -------
    final :  This function returns the highest Quotient from all the symbols
    in your stocks dictionary

 """   
 date= normaliseDate(portfolio["date"])   
 h= list(stocks) 
 t= 0
 Quo=0
 while t < len(h):
    try: 
        if Quotient(date,h[t]) > Quo:
           Quo= Quotient(date,h[t])
           final = h[t]
    except KeyError: # for when anything in stocks dictionary isnt a stock 
        pass
    t += 1
 return final  

def BuyStocks(verbose=False):
  """
    This function will buy the max amount of a stock which our cash can 
    buy. The stock bought is chose by the BestChoice() function 

    Parameters
    ----------
    verbose : TYPE, optional
    If True, the details of thetransaction is printed. The default is False.

    Returns
    -------
    None.
  """
  NextTradingDay()
  portdate= portfolio["date"]
  bestsym = BestChoice()
  loadStock(bestsym)
  stockon= stocks[bestsym]
  stockonday=(stockon[portdate])[1]
  p=0
  t=0
  while t < 1:
      p += 1
      if p*stockonday > portfolio["cash"]:
        t=1
  if p==0:
    print("we do not have enough cash")      
  if verbose == True:
     addTransaction({ 'date':portfolio["date"], 'symbol':bestsym, 'volume':p-1 },True)
  if verbose == False:
     addTransaction({ 'date':portfolio["date"], 'symbol':bestsym, 'volume':p-1 })
     
    
def SellStocks(l,verbose=False):
    """
    This function will sell all of the stocks of the stock we just 
    bought if they have gone up a lot or dropped a lot.

    Parameters
    ----------
    l: This is to make sure that we are taking the volume of the transaction
    that we have just made when buying the stocks
    verbose : TYPE, optional
    If verbose is true, the details of thetransaction is printed. The default is False.

    Returns
    -------
    None.

    """
    t= 0
    vol=(transactions[l])["volume"]
    p= portfolio["date"]
    bestsym = BestChoice()
    SymbolStocks= stocks[bestsym]
    HighStocksOnDay= (SymbolStocks[p])[1]
    while t<1:
      NextTradingDay() 
      if ((SymbolStocks[portfolio["date"]])[2])/HighStocksOnDay > 1.3 or ((SymbolStocks[portfolio["date"]])[2])/HighStocksOnDay < 0.7:
         t=2
    if verbose == True:     
     addTransaction({ 'date':portfolio["date"], 'symbol':bestsym, 'volume':-vol},True)
    if verbose == False:
     addTransaction({ 'date':portfolio["date"], 'symbol':bestsym, 'volume':-vol})   
    
def tradeStrategy1(verbose=False):
  """
  This function is a trading strategy that essentialy buys a load of one stock when the price
  per unit has gone up a bit over 10 days and then sells all those stocks if the have drastically 
  dropped or gone up.
  """
  stocklst= list(stocks)     
  p= list(stocks[stocklst[0]])
  earlier= 0
  t=0
  l=0
  try:
   Earlydate(p[8])
  except DateError:
     earlier = 1
  if earlier == 0:
    portfolio["date"]= p[8]
  if earlier == 1:  
   h=0
   while h < len(p):
     if p[h] == portfolio["date"]:
         break
     h += 1 
   portfolio["date"]= p[h-1]  
  while t<3650: 
   t += 1
   if verbose == True:
    try:
     BuyStocks(True)
     SellStocks(l,True)
     l += 2 
    except ValueError:  # when there is no more trading days, in this case the day is 2018-03-13 
     break
   if verbose == False:
    try:
      BuyStocks() 
      SellStocks(l)
      l += 2
    except ValueError:   
     break      

def main():  
 return
    
# the following allows your module to be run as a program
if __name__ == '__main__' or __name__ == 'builtins':
    main() 
    
  