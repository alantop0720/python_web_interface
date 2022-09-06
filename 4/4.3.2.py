import requests

requests.packages.urllib3.disable_warnings()

r = requests.get('https://api.github.com/events', verify=False)
print(r.content)
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
print(r.content)
r = requests.put('http://httpbin.org/put', data = {'key':'value'})
print(r.content)
r = requests.delete('http://httpbin.org/delete')
print(r.content)
r = requests.head('http://httpbin.org/get')
print(r.content)
r = requests.options('http://httpbin.org/get')
print(r.content)


import requests
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)


import json
dict_a = {"k1":"v1","k2":"v2"}

#把字典转成json字符串
x = json.dumps(dict_a)
print(x)
print(type(x))

#把json字符串转成字典
y = json.loads(x)
print(y)
print(type(y))

import requests
r = requests.get('http://www.qq.com')
print(r.headers)



url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers, verify=False)
