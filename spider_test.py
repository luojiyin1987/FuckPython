import urllib.error
import urllib.parse
import urllib.request
import http.cookiejar

url = "https://www.baidu.com"
headers = {"User-Agent": "Mozaila/4.0 (compatible; MSIE 5.5; Windows NT)"}

request = urllib.request.Request(url, data=None, headers={})
response = urllib.request.urlopen(request, timeout=10)

