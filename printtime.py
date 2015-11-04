#!/usr/local/bin/python

from datetime import datetime

now = datetime.now()
print now
print now.year
print now.month
print now.day

<<<<<<< HEAD
#print str(now.month) + '/' + str(now.day) + '/' + str(now.year)
print 'Date is '+'%s/%s/%s' % (now.month, now.day, now.year) 
print 'Time is: ' + '%s:%s:%s' % (now.hour, now.minute, now.second)
print 'Time is: ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
print str(now.hour) + ':' + str(now.minute)
print 'Date and Time : '+'%s/%s/%s : %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
=======
print str(now.month) + '/' + str(now.day) + '/' + str(now.year)
print 'Time is: ' + str(now.hour) + ':' + str(now.minute)
print str(now.hour) + ':' + str(now.minute)
>>>>>>> d307d522e13003bda853423e62f27dad08c41278
