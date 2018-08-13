from datetime import datetime
from threading import Timer

x=datetime.today()
print x
y=x.replace(day=x.day, hour=x.hour, minute=x.minute+2, second=x.second, microsecond=x.microsecond)
print y
delta_t=y-x
print delta_t
secs=delta_t.seconds+1

def hello_world():
    print "hello world"

t = Timer(secs, hello_world)
t.start()