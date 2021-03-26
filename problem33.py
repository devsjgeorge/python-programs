#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 09:11:14 2021

@author: sajinijoby
"""
num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero', 100:'hundred', 200:'two hundred', \
            300:'three hundred', 400:'four hundred', 500:'five hundred', \
            600:'six hundred', 700:'seven hundred', 800:'eight hundred', \
            900:'nine hundred', 1000:'thousand'}
    
def n2w(n):
        try:
            print(num2words[n])
        except KeyError:
            try:
                print( num2words[n-n%10] + ' ' + num2words[n%10].lower())
            except KeyError:
                print('Number out of range') 
                print(-1)
                
         
                
numb =input("Please enter a number between 1 and 1000:")
print(n2w(int(numb)))
