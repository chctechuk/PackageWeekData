# -*- coding: utf-8 -*-
"""
Package Week Data
Created on Mon Feb 21 2022
@author: chcuk
"""

import sys
sys.dont_write_bytecode = True
import time
import os
import gc
import INI
from datetime import datetime
import convert
import shutil
import Core

def main():
    flag = 1
    while flag:
        today = datetime.now().weekday()
        if today==config['DOP']:
            for i in range(1, config['NOW']*7+1):
                tarYear  = '%04d'%convert.convert(i).outPreDaybyDate()[0]
                tarDay   = '%03d'%convert.convert(i).outPreDaybyDate()[1]
                savePath = '{}{}{}{}{}'.format(
                    config['OFP'], '/', tarYear, '/', tarDay)
                if not os.path.exists(savePath):
                    os.makedirs(savePath)
                    CHCSHPath = '{}{}{}{}{}{}'.format(
                        config['IFP'], '/CHCSH/SSR0', tarDay, '0.', 
                        tarYear[2:], 'C')
                    CHCUKPath = '{}{}{}{}{}{}'.format(
                        config['IFP'], '/Products/SSR0', tarDay, '0.', 
                        tarYear[2:], 'C')
                    CNEPath   = '{}{}{}{}{}{}'.format(
                        config['IFP'], '/Products/SSRA00CNE0', tarDay, '0.',
                        tarYear[2:], 'C')
                    DLRPath   = '{}{}{}{}{}{}'.format(
                        config['IFP'], '/Products/SSRA00DLR0', tarDay, '0.',
                        tarYear[2:], 'C')
                    GFZPath   = '{}{}{}{}{}{}'.format(
                        config['IFP'], '/Products/SSRA00GFZ0', tarDay, '0.',
                        tarYear[2:], 'C')
                    WHUPath   = '{}{}{}{}{}{}'.format(
                        config['IFP'], '/Products/SSRA00WHU0', tarDay, '0.',
                        tarYear[2:], 'C')
                    IGSPath   = '{}{}{}{}{}{}'.format(
                        config['IFP'], '/Products/SSRA01IGS0', tarDay, '0.',
                        tarYear[2:], 'C')
                    MIXPath   = '{}{}{}{}{}{}'.format(
                        config['IFP'], '/Products/SSRA00MIX0', tarDay, '0.',
                        tarYear[2:], 'C')
                    if os.path.exists(CHCSHPath):
                        targetPath = '{}{}{}{}{}{}'.format(
                            savePath, '/SSRA0CHCSH', tarDay, '0.', tarYear[2:], 'C')
                        shutil.copyfile(CHCSHPath, targetPath)
                        Core.cGZIP(config, targetPath)
                    else:
                        INI.logRecord(config, CHCSHPath+' is not found')
                    if os.path.exists(CHCUKPath):
                        targetPath = '{}{}{}{}{}{}'.format(
                            savePath, '/SSRA0CHCUK', tarDay, '0.', tarYear[2:], 'C')
                        shutil.copyfile(CHCUKPath, targetPath)
                        Core.cGZIP(config, targetPath)
                    else:
                        INI.logRecord(config, CHCUKPath+' is not found')
                    if os.path.exists(CNEPath):
                        targetPath = '{}{}{}'.format(
                            savePath, '/', os.path.split(CNEPath)[1])
                        shutil.copyfile(CNEPath, targetPath)
                        Core.cGZIP(config, targetPath)
                    else:
                        INI.logRecord(config, CNEPath+' is not found')
                    if os.path.exists(DLRPath):
                        targetPath = '{}{}{}'.format(
                            savePath, '/', os.path.split(DLRPath)[1])
                        shutil.copyfile(DLRPath, targetPath)
                        Core.cGZIP(config, targetPath)
                    else:
                        INI.logRecord(config, DLRPath+' is not found')
                    if os.path.exists(GFZPath):
                        targetPath = '{}{}{}'.format(
                            savePath, '/', os.path.split(GFZPath)[1])
                        shutil.copyfile(GFZPath, targetPath)
                        Core.cGZIP(config, targetPath)
                    else:
                        INI.logRecord(config, GFZPath+' is not found')
                    if os.path.exists(WHUPath):
                        targetPath = '{}{}{}'.format(
                            savePath, '/', os.path.split(WHUPath)[1])
                        shutil.copyfile(WHUPath, targetPath)
                        Core.cGZIP(config, targetPath)
                    else:
                        INI.logRecord(config, WHUPath+' is not found')
                    if os.path.exists(IGSPath):
                        targetPath = '{}{}{}'.format(
                            savePath, '/', os.path.split(IGSPath)[1])
                        shutil.copyfile(IGSPath, targetPath)
                        Core.cGZIP(config, targetPath)
                    else:
                        INI.logRecord(config, IGSPath+' is not found')
                    if os.path.exists(MIXPath):
                        targetPath = '{}{}{}'.format(
                            savePath, '/', os.path.split(MIXPath)[1])
                        shutil.copyfile(MIXPath, targetPath)
                        Core.cGZIP(config, targetPath)
                    else:
                        INI.logRecord(config, MIXPath+' is not found')
                    del (tarYear, tarDay, CHCSHPath, CHCUKPath, CNEPath,
                         DLRPath, GFZPath, WHUPath, IGSPath)
                    gc.collect()
                else:
                    time.sleep(3600)
        else:
            time.sleep(int(86400/4))
# %%
if __name__ == '__main__':
    INI.logo()
    INI.validity()
    config = INI.readConfig('config_pwd.ini')
    INI.mkFolder(config)
    main()
