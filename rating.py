import urllib
import json
import time, os

USER_INFO_URL = 'http://codeforces.com/api/user.rating?handle={handle}'
handle = raw_input('Please enter your codeforce username: ')

user_info = urllib.urlopen(USER_INFO_URL.format(handle=handle)).read()
dic = json.loads(user_info)
if dic['status'] != u'OK':
    print 'Oops.. Something went wrong...'
    exit(0)

ratings = dic['result']
start_time = time.time()

for rate in ratings:
    a=rate['newRating']
    b=rate['oldRating']
   # print ('contest id=',rate['contestId'],'rank=',rate['rank'],' oldrating= ',b,' newrating=',a,' improvement=',a-b) 
    print 'improvement = %d' % int(a-b)

end_time = time.time()
print 'Execution time %d seconds' % int(end_time - start_time)

