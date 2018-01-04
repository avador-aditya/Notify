'''
Created on Jan 3, 2018

@author: Aditya Sharma
'''
import smtplib
import cryptocurrency
from cryptocurrency import pwd
from cryptocurrency import pricechange
from cryptocurrency import tip

server_connect=smtplib.SMTP('smtp.gmail.com',587)
server_connect.ehlo()
server_connect.starttls()
server_connect.login('sendersmail', cryptocurrency.pwd.get_password())
status=server_connect.sendmail('sendersmail', ['recievers'],'Subject: \n'+cryptocurrency.pricechange.notify(0.01))
if status=={}:
    print("Success")
else:
    print("Fail")
server_connect.quit()