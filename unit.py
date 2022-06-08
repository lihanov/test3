import syslog
import time
a=1
while True:
    text='This is a test message ' + str(a)
    syslog.syslog(text)
#    print(text)
    a+=1
    time.sleep(3)
