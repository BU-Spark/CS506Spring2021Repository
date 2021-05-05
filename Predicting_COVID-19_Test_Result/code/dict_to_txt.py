# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 00:09:42 2021

@author: KevinLu
"""
from datetime import datetime

d = {'x': 1, 'y': "test", 'z': 3} 


wdir = "./output/dict_log.txt"

def dict_to_txt(payload, title, wodir = wdir):
    def add_txt_to_file(filename, content):
        res = open(filename, "a")
        for i in content:
            res.write(str(i))
            res.write("\n")
        res.close()
    #generate payload list
    res = []
    res.append("##########" + title + "##########")
    t1 = str(datetime.now())
    res.append("Report Created: " + t1)
    res.append("\n")
    
    #loop through the dict
    for key in payload:
        stro = str(key) + " : " + str(payload[key])
        res.append(stro)
    res.append("#"*(len(title)+20))
    #write file
    add_txt_to_file(wodir, res)
    
dict_to_txt(d, "this is a test")