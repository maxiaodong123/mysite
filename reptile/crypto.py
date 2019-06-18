from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import sys
from binascii import b2a_hex, a2b_hex

# 加密解密：公钥加密，私钥解密
#
# 签名验签：私钥签名，公钥验签
#
print("1、生成私钥和公钥")

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)
# A的秘钥对的生成
private_pem = rsa.exportKey()

with open('d:\\python\\aaaprivate.pem', 'wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('d:\\python\\aaapublic.pem', 'wb') as f:
    f.write(public_pem)

# B的秘钥对的生成
private_pem = rsa.exportKey()
with open('d:\\python\\bbbprivate.pem', 'wb') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('d:\\python\\bbbpublic.pem', 'wb') as f:
    f.write(public_pem)

# 加密和解密
print("2、加密和解密")
# A使用B的公钥对内容进行rsa 加密

message = '大家好，这就是我要加密的数据'
print("message: " + message)
with open('d:\\python\\bbbpublic.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(str(key))
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(bytes(message.encode("utf8"))))
    print("加密（encrypt）")
    print(cipher_text)

# B使用自己的私钥对内容进行rsa 解密

with open('d:\\python\\bbbprivate.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(cipher_text), random_generator)
    print("解密（decrypt）")
    print("text:" + str(text, "utf8"))
    print("message:" + message)

    assert str(text, "utf8") == message

# 签名与验签
print("3、 签名与验签")

# A使用自己的私钥对内容进行签名
print("签名")
with open('d:\\python\\aaaprivate.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    signer = Signature_pkcs1_v1_5.new(rsakey)
    digest = SHA.new()
    digest.update(message.encode("utf8"))
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)

print(signature)
# B使用A的公钥进行验签
print("验签")
with open('d:\\python\\aaapublic.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    verifier = Signature_pkcs1_v1_5.new(rsakey)
    digest = SHA.new()
    digest.update(message.encode("utf8"))
    is_verify = verifier.verify(digest, base64.b64decode(signature))
print(is_verify)

# obj = AES.new()
# print(base64.encodebytes(18243892507))
# print(base64.encodestring(18243892507))
print(len('08f5b8bd6d8f26fa8218d2170d9e6c05'))
print(len('qutouwang'))


class PrpCrypt(object):

    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        # return plain_text.rstrip('\0')
        return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
    pc = PrpCrypt('hengyuanxinda123')  # 初始化密钥
    e = pc.encrypt("18243892507")  # 加密
    d = pc.decrypt(e)  # 解密
    print("加密:", e)
    print("结果:",'08f5b8bd6d8f26fa8218d2170d9e6c05')
    print("解密:", d)