import requests

url= 'http://httpbin.org'
r= requests.get(url)
print 'Response object properties and methods available'
print dir(r)
print 'URL, response code, response text, headers and redirection history'
print r.url
print r.status_code
print r.text
print r.headers
print r.history

print 'Making requests with parameters - GET and POST'
payload= {'key':'value'}
headers = {'user-agent': 'my-app/0.0.1'}
cookies = dict(cookies_are='working')

r = requests.get('http://httpbin.org/get', params = payload, cookies=cookies)
print r.status_code
r = requests.post('http://httpbin.org/post', data = payload, headers=headers)
print r.status_code
print r.json()
print r.headers.get('content-type')

jar = requests.cookies.RequestsCookieJar()
print dir(jar)
print jar.values()
