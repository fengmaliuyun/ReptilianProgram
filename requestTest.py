import requests
# GET 请求
response = requests.get("https://foofish.net")

response.status_code
#200

# 原因短语
response.reason
#'OK'

# 响应首部
for name,value in response.headers.items():
    print("%s:%s" % (name, value))

#Content-Encoding:gzip
#Server:nginx/1.10.2
#Date:Thu, 06 Apr 2017 16:28:01 GMT

# 响应内容
response.content

#'<html><body>此处省略一万字...</body></html>
response.headers.