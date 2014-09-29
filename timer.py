import os
import time
from threading import Thread

def timer_loop(time_interval, stop_ticks):
    time_ticks = 0
    while time_ticks < stop_ticks:
        time.sleep(time_interval)
        print time_ticks, "seconds."
        time_ticks += 1

def print_timer(time_interval, stop_ticks):
    t = Thread(target=timer_loop, args=(time_interval, stop_ticks))
    t.start()
    pass

def main():
    print "start"
    print_timer(2, 5)
    print "end"

if __name__ == '__main__':
    main()
