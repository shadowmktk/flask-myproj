# flask-myproj
Flask Web项目，通过URL方式获取指定域名的证书时间和证书内容


Install requirements.
```
pip3 install -r requirements.txt
```

Running demo.
```
python3 app.py

curl http://127.0.0.1:5000
```


Example.
```
http://127.0.0.1:5000/?domain=域名
http://127.0.0.1:5000/?domain=域名&port=443
http://127.0.0.1:5000/?domain=域名&port=8443
```

```
root@ubuntu:~# curl -s http://127.0.0.1:5000/?domain=www.taobao.com | jq .
{
  "域名": "www.taobao.com",
  "证书创建时间": "2024-06-19 17:06:02",
  "证书到期时间": "2025-07-21 17:06:01",
  "证书是否过期": false,
  "证书内容": "-----BEGIN CERTIFICATE-----XXX-----END CERTIFICATE----"
}
root@ubuntu:~#
root@ubuntu:~# curl -s http://127.0.0.1:5000/?domain=www.aliyun.com | jq .
{
  "域名": "www.aliyun.com",
  "证书创建时间": "2024-05-08 15:46:06",
  "证书到期时间": "2025-06-09 15:46:05",
  "证书是否过期": false,
  "证书内容": "-----BEGIN CERTIFICATE-----XXX-----END CERTIFICATE-----"
}
root@ubuntu:~#
root@ubuntu:~# curl -s "http://127.0.0.1:5000/?domain=192.168.3.106&port=8443" | jq .
{
  "域名": "192.168.3.106",
  "证书创建时间": "2024-09-06 10:10:10",
  "证书到期时间": "2034-09-04 10:10:10",
  "证书是否过期": false,
  "证书内容": "-----BEGIN CERTIFICATE-----XXX-----END CERTIFICATE-----"
}
root@ubuntu:~#
```

Docker.
```
docker build -t flask-myproj:v1.0.0 .

docker run -d --name flask-myproj -p 8080:8000 flask-myproj:v1.0.0
```
```
curl -s "http://127.0.0.1:8080/?domain=192.168.3.106"
curl -s "http://127.0.0.1:8080/?domain=192.168.3.106&port=8443"
```

