import requests
import time

def do_encrypt_rc4(src, passwd):
    src = src.strip()
    passwd = str(passwd)

    key = [ord(passwd[i % len(passwd)]) for i in range(256)]
    sbox = [i for i in range(256)]

    j = 0
    for i in range(256):
        j = (j + sbox[i] + key[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]

    output = []
    a = b = 0
    for char in src:
        a = (a + 1) % 256
        b = (b + sbox[a]) % 256
        sbox[a], sbox[b] = sbox[b], sbox[a]
        c = (sbox[a] + sbox[b]) % 256
        encrypted_char = ord(char) ^ sbox[c]
        output.append("{:02x}".format(encrypted_char))

    return ''.join(output)

def onPwdLogin(username, password):
    rckey = str(int(time.time() * 1000))
    pwd = do_encrypt_rc4(password, rckey)

    # post body
    params = {
        'opr': 'pwdLogin',
        'userName': username,
        'pwd': pwd,
        'auth_tag': rckey,
        'rememberPwd': '0'
    }

    url = "http://2.2.2.3/ac_portal/login.php"
    print(time.ctime())
    try:
        response = requests.post(url, data=params, proxies={"http": "", "https": ""}) # noproxy
        print("Status Code: ", response.status_code)
        print("Response: ", response.text)
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    # 输入用户名和密码
    username = ""
    password = ""

    if (username == "" or password == ""):
        print("用户名或密码为空！")
        exit(0)

    onPwdLogin(username, password)
