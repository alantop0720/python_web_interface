#有时候github会因为网络问题而连不上，需要多试几次。



import requests
requests.packages.urllib3.disable_warnings()
r = requests.get('https://api.github.com/events',  verify=False)
print(r.content) #请把断点打在这一行



import requests,json
r = requests.get('https://api.github.com/events', verify=False)
print(r.content)

dict_json = json.loads(r.content)
print(dict_json)



import requests
r = requests.get('https://api.github.com/events', verify=False)
print(r.json())


