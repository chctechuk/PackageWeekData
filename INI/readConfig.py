# -*- coding: utf-8 -*-
"""
Read Config File
Created on Tue Feb 22 2022
@author: Dr Hui Zhi
"""

import configparser

def readConfig(configFile='config_pwd.ini'):
    """
    Parameters
    ----------
    configFile : file
        configFile is config file name with extension.

    Returns
    -------
    config : dict
    """
    config = {}
    cfg    = configparser.ConfigParser(
        inline_comment_prefixes='#', allow_no_value=True)
    cfg.read(configFile)
    
    config['IFP'] = cfg.get('Input Configuration', 'InputFolderPath')
    config['OFP']  = cfg.get('Input Configuration', 'OutputFolderPath')

    config['DOP'] = cfg.getint('Process Configuration', 'DayOfPackage')
    config['NOW'] = cfg.getint('Process Configuration', 'NumOfWeeks')
    
    return config
