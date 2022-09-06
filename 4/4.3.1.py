import requests

requests.packages.urllib3.disable_warnings()
r=requests.get("https://github.com/", verify=False)
print(r.text)
print(r.status_code)
