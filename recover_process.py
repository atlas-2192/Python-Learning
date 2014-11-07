import time
import string
import sys
import commands
import time
import os
from threading import Thread

exitapp = False
recover_process_name = 'jabberd2'

def get_proc_id(process_name):
    process_format = "ps aux | grep '%s'" % (process_name)
    d = [i for i in commands.getoutput(process_format).split("\n") if 'grep' not in i.split()]
    #return process id and user name
    return (str(d[0].split()[0]), str(d[0].split()[1])) if d else None

def timer_loop(time_interval, gostop):
    global exitapp
    time_ticks = 0
    while not exitapp:
        time.sleep(time_interval)

        ps_acc = get_proc_id(recover_process_name)
        print type(ps_acc)
        if ps_acc == None:
             print 'process not exist, launch new one....'
             run_account_xmpp_screen_background()
        else:
             print 'account xmpp exist, query status.. '
             print str(ps_acc)

def run_account_xmpp_screen_background():
    print 'Run account xmpp'
    os.system('sudo screen -d -m /home/'.recover_process_name)


if __name__ == '__main__':
    # Start Thread every 2 second to check xmpp if exist.
    try:
        pass
        t = Thread(target=timer_loop, args=(2,0))
        t.start()
        t.join(2000)
        run_account_xmpp_screen_background()
    except KeyboardInterrupt:
        pass
        exitapp = Truea
