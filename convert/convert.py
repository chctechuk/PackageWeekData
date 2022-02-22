# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 2020
@author: chcuk
"""

from datetime import datetime, timedelta

class convert():
    def __init__(self, cycleDays):
        """
        Parameters
        ----------
        cycleDays : int
            the number of daily files left in folder.
        """
        self.cycleDays = cycleDays
    
    def now(self):
        return datetime.now()
    
    def outDaybyDate(self):
        year   = self.now().year
        month  = self.now().month
        day    = self.now().day
        months = [0,31,59,90,120,151,181,212,243,273,304,334]
        if 0 < month <= 12:
            sumn = months[month-1]
        else:
            print("month error")
        sumn += day
        leap = 0
        if (year%400==0) or ((year%4)==0) and (year%100!=0):
            leap=1
        if (leap==1) and (month>2):
            sumn += 1
        return year, sumn
    
    def outPreDaybyDate(self):
        year   = (self.now() - timedelta(days=self.cycleDays + 1)).year
        month  = (self.now() - timedelta(days=self.cycleDays + 1)).month
        day    = (self.now() - timedelta(days=self.cycleDays + 1)).day
        months = [0,31,59,90,120,151,181,212,243,273,304,334]
        if 0 < month <= 12:
            sumn = months[month-1]
        else:
            print("month error")
        sumn += day
        leap = 0
        if (year%400==0) or ((year%4)==0) and (year%100!=0):
            leap=1
        if (leap==1) and (month>2):
            sumn += 1
        return year, sumn
