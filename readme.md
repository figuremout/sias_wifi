辣鸡高研院 WiFi 每 24h 要重新登录，搞得老子向日葵老是断联 T-T

自动重连脚本，启动!

# 使用方法
1. 安装依赖
```bash
$ conda/pip install requests
```
2. 打开 connect.py 脚本，填入 `username`, `password`
3. 启动
```bash
% python connect.py
Sun May 12 12:16:37 2024
Status Code:  200
Response: {'success':true, 'msg':'logon success','action':'logout','pop':0,'userName':'xxxxxxxxxxxx','location':'http://2.2.2.3/ac_portal/proxy.html?type=logout'}
```
4. crond 每 12h (6:00, 18:00) 自动执行脚本 （WSL 也适用，Win 用户自行搜索自动执行脚本方法）
 ```bash
$ crontab -e
0 6,18 * * * path_to_python path_to_connect.py >> /tmp/sias_wifi.log 2>&1
 ```
