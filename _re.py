import re


s = '192.168.1.1 - - [10/Feb/2024:09:15:22 +0300] "GET /home.html HTTP/1.1" 200 1234'
res = re.findall(r'[^"-]', s)
res = ''.join(res).replace(' +', '+')
res = res.strip().split()
print(res)