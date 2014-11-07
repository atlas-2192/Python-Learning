import time
import string
import sys
import commands
import time

def get_cpumem(pid):
    d = [i for i in commands.getoutput("ps aux").split("\n")
        if i.split()[1] == str(pid)]
    return (float(d[0].split()[2]), float(d[0].split()[3])) if d else None

if __name__ == '__main__':
    print("%APP\t%TIME\t            \t%CPU\t%MEM")

    try:
        while True:
            ps_pair = get_cpumem('2047')
            ps_acc  = get_cpumem('2052')
            ps_sm  = get_cpumem('2017')
            ps_s2s  = get_cpumem('2023')
            ps_c2s  = get_cpumem('2028')

            file_name = time.strftime("%Y-%m-%d")
            file_name += '.log'
            f = open(file_name, 'a+')

            time_str = time.strftime("%H:%M:%S")
            print("%s\t%s\t\t%.2f\t%.2f" %('pairing',time_str, ps_pair[0], ps_pair[1]))
            f.write("%s\t%s\t\t%.2f\t%.2f\n" %('pairing',time_str, ps_pair[0], ps_pair[1]))
            print("%s\t%s\t\t%.2f\t%.2f" %('account',time_str, ps_acc[0], ps_acc[1]))
            f.write("%s\t%s\t\t%.2f\t%.2f\n" %('account',time_str, ps_acc[0], ps_acc[1]))
            print("%s\t%s\t\t%.2f\t%.2f" %('sm',time_str, ps_sm[0], ps_sm[1]))
            f.write("%s\t%s\t\t%.2f\t%.2f\n" %('sm',time_str, ps_sm[0], ps_sm[1]))
            print("%s\t%s\t\t%.2f\t%.2f" %('s2s',time_str, ps_s2s[0], ps_s2s[1]))
            f.write("%s\t%s\t\t%.2f\t%.2f\n" %('s2s',time_str, ps_s2s[0], ps_s2s[1]))
            print("%s\t%s\t\t%.2f\t%.2f" %('c2s',time_str, ps_c2s[0], ps_c2s[1]))
            f.write("%s\t%s\t\t%.2f\t%.2f\n" %('c2s',time_str, ps_c2s[0], ps_c2s[1]))

            f.write('-----------------------------------------------------\n')
            print('-----------------------------------------------------')
            f.closed
            time.sleep(60)
    except KeyboardInterrupt:
        print
        exit(0)
