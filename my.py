import urllib
import json
import time, os

MAX_SUBS = 100000
MAX_CF_CONTEST_ID = 600
MAGIC_START_POINT = 17000

SUBMISSION_URL = 'http://codeforces.com/contest/{ContestId}/submission/{SubmissionId}'
USER_INFO_URL = 'http://codeforces.com/api/user.status?handle={handle}&from=1&count={count}'

URL = 'http://codeforces.com/api/contest.hacks?contestId={contestId}'

EXT = {'C++': 'cpp', 'C': 'c', 'Java': 'java', 'Python': 'py', 'Delphi': 'dpr', 'FPC': 'pas', 'C#': 'cs'}
EXT_keys = EXT.keys()

replacer = {'&quot;': '\"', '&gt;': '>', '&lt;': '<', '&amp;': '&', "&apos;": "'"}
keys = replacer.keys()

handle='stockfish'


user_info = urllib.urlopen(URL.format(contestId=374)).read()
dic = json.loads(user_info)

if dic['status'] != u'OK':
    print 'Oops.. Something went wrong...'
    exit(0)

hacks = dic['result']
start_time=time.time()

for hack in hacks:
    print hack['id']
    print hack['verdict']


end_time = time.time()

print 'Execution time %d seconds' % int(end_time - start_time)
