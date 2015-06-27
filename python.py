import urllib
import json
import time, os

import matplotlib.pyplot as plt
plt.figure()


 
plt.figure()

x=[]
y=[]

x.append(1)
y.append(1500)

USER_INFO_URL = 'http://codeforces.com/api/user.rating?handle={handle}'
handle = raw_input('Please enter your codeforce username: ')

user_info = urllib.urlopen(USER_INFO_URL.format(handle=handle)).read()
dic = json.loads(user_info)
if dic['status'] != u'OK':
    print 'Oops.. Something went wrong...'
    exit(0)

ratings = dic['result']
start_time = time.time()

val=1

for rate in ratings:
    a=rate['newRating']
    b=rate['oldRating']
    x.append(val+1)
    y.append(a)
    val=val+1
    print a
   
label='a'     
plt.plot(x,y,label='your rating')
plt.xlabel("contest no")
plt.ylabel("rating")
plt.title("your rating graph")

plt.xlim(0,30)
plt.ylim(1000,2000)

plt.legend(loc="upper left")

plt.savefig("rating.png")



end_time = time.time()
print 'Execution time %d seconds' % int(end_time - start_time)

