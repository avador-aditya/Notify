'''
Created on Jan 3, 2018

@author: Aditya Sharma
'''
import cryptocurrency
'''
Created on Oct 2, 2017

@author: Aditya Sharma
'''
from time import strftime, localtime
import requests

from time import sleep
price_list=[]
def prereq():

        
    res = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BCH,XRP,ETH,BTC,LTC&tsyms=INR')   
    if res !=None:
        now=strftime("%d-%m-%Y %H:%M:%S", localtime())
        print(now)
    else:
        print("Error")
    
    k=res.json()
    
    for coins in k:
        
        price_list.append([coins,k[coins]['INR']])
def now(): 
    now=strftime("%d-%m-%Y %H:%M:%S", localtime())
    #dt=date()
    dt=(now.split('-'))
    yr=dt[2].split(' ')
    months={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'July','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
    
    
    if len(dt[0])==2 and dt[0][1] in ['1','2','3']:
        if dt[0][1]=='1':
            wrd=dt[0]+'st '+months[dt[1]]+' '+yr[0]+' at '+yr[1]
            
        elif dt[0][1]=='2':
            wrd=dt[0]+'nd '+months[dt[1]]+' '+yr[0]+' at '+yr[1]
        elif dt[0][1]=='3':
            wrd=dt[0]+'rd '+months[dt[1]]+' '+yr[0]+' at '+yr[1]
    elif len(dt[0])==1 and dt[0] in ['1','2','3']:
        if dt[0]=='1':
            wrd=dt[0]+'st '+months[dt[1]]+' '+yr[0]+' at '+yr[1]
        elif dt[0]=='2':
            wrd=dt[0]+'nd '+months[dt[1]]+' '+yr[0]+' at '+yr[1]
        elif dt[0]=='3':
            wrd=dt[0]+'rd '+months[dt[1]]+' '+yr[0]+' at '+yr[1]

    else:
        wrd=dt[0]+'th '+months[dt[1]]+' '+yr[0]+' at '+yr[1]
    return wrd
def change_pr():
    price_change=[]
    res = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BCH,XRP,ETH,BTC,LTC&tsyms=INR')
    k=res.json()
    for coins in k:
        price_change.append([coins,k[coins]['INR']])
    
    if res!=None:
        now()
    else:
        print("Error")
    return price_change    
def notify(perc):
    prereq()        
    sleep(20)
    price_change=change_pr()
    
    noti=" "
    for i in range(0,len(price_list)-1):
        diff=((price_change[i][1]-price_list[i][1])/price_list[i][1])*100
        if abs(float(format(diff,'.2f')))<=perc:
            pass
        else:
            
            
            if diff<0:
                noti=("The current price of "+price_change[i][0]+" is "+str(price_change[i][1])+"\nThe rate of "+price_change[i][0]+" has decreased by "+str(format(diff,'.2f' ))+"%")+"\n"+noti
                #Aarambh.taskbardemo.balloon_tip("Latest Price", noti)
            else:
                noti=("The current price of "+price_change[i][0]+" is "+str(price_change[i][1])+"\nThe rate of "+price_change[i][0]+" has increased by "+str(format(diff,'.2f' ))+"%")+"\n"+noti 
    cryptocurrency.tip.balloon_tip("Price Update", noti)            
    return(noti)            
          

