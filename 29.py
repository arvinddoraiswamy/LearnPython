import contextlib
import requests

url = 'https://w3c.org'
print("Using requests here within a context, that ensures that the objects that are created when requests.method is called, are also destroyed")
with contextlib.closing(requests.get(url, verify=False, timeout=1)) as resp:
    if resp.status_code == 200:
        print("request succeeded and the objects are destroyed")
    else:
        print("request failed")
