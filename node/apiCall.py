import json
import requests


r = requests.get('http://localhost:3000')
data=r.json()
for item in data:
	print("%s is %s" % (item['name'], item['color']))

