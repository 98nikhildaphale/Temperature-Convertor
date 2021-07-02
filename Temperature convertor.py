# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 23:20:33 2021


"""


a=input("Press c to convert from celcius to fahrenheit OR Press f to convert fahrenheit to celcius: ")
 
if a=="c":
   x=int(input("enter the temperature: "))
   y=(x-32)*5/9
   print(y) 

elif a=="f":
    z=int(input("enter the temperature: "))
    b=(z*9/5)+32
    print(b)