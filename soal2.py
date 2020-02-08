# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:42:52 2020

@author: Players
"""

import re 
password = input("please input the password : \n")
flag = 0
while True:   
    if (len(password)<8): 
        flag = -1
        break
    elif not re.search("[a-z]", password): 
        flag = -1
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        break
    elif not re.search("[_@$]", password): 
        flag = -1
        break
    elif re.search("\s", password): 
        flag = -1
        break
    else: 
        flag = 0
        print("Password Valid") 
        break
  
if flag ==-1: 
    print("Password Invalid")

username = input("please input the username : \n")
flag = 0
while True :
    if (len(username) >9):
        flag = -1
        break
    elif (len(username) <5):
        flag = -1
        break
    elif re.search("[A-Z]", username): 
        flag = -1
        break
    elif re.search("[0-9]", username): 
        flag = -1
        break
    elif re.search("[_@$]", username): 
        flag = -1
        break
    else :
        flag = 0
        print ("username valid")
        break
if flag == -1:
    print("username invalid")