import requests
url = 'https://www.baidu.com'
r = requests.get(url)
r.status_code
print(r.status_code)
r.text
print(r.text[:500])