#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from sets import Set
import sys

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

f = open('file.txt', 'r')            
result = Set()

for line in f.readlines():                          
    if "string in line" in line:       
        pass #do something
        result.add('some text')
print len(result), len(user_id), len(camera_id)