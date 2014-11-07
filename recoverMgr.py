import time
import string
import sys
import commands
import time
import os
from threading import Thread

exitapp = False

def get_proc_id(process_name):
    process_format = "ps aux | grep '%s'" % (process_name)
    d = [i for i in commands.getoutput(process_format).split("\n") if 'grep' not in i.split()] 
    return (str(d[0].split()[0]), str(d[0].split()[1])) if d else None

def check_recover_process(process_name):
    ps_proc = get_proc_id(process_name)
    print type(ps_proc)
    if ps_proc == None:
         print 'process not exist, launch new one....'
         recover_process(process_name)
    else:
         print process_name, ' exist, query status.. '
         print str(ps_proc)

def recover_process(process_name):
    if 'sm' in process_name or 's2s' in process_name  or 'c2s' in process_name :
        print 'Recovery jabberd2 services'
        os.system('sudo service jabberd2 restart')



if __name__ == '__main__':
    # Start Thread every 2 second to check xmpp if exist.
 
    print 'Checking jabberd2....'
    check_recover_process('sm')
    check_recover_process('s2s')
    check_recover_process('c2s')
