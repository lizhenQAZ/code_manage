# coding: utf-8
from hashlib import sha1, sha224, sha256, sha384, sha512, md5

# md5加密
encrypt_md5 = md5()
encrypt_md5.update('haha'.encode())
print(encrypt_md5.hexdigest(), ': ', len(encrypt_md5.hexdigest()))
print('*'*50, 'md5', '*'*50)

# sha1加密
encrypt_sha1 = sha1()
encrypt_sha1.update('haha'.encode())
print(encrypt_sha1.hexdigest(), ': ', len(encrypt_sha1.hexdigest()))
print('*'*50, 'sha1', '*'*50)

# sha224加密
encrypt_sha224 = sha224()
encrypt_sha224.update('haha'.encode())
print(encrypt_sha224.hexdigest(), ': ', len(encrypt_sha224.hexdigest()))
print('*'*50, 'sha224', '*'*50)

# sha256加密
encrypt_sha256 = sha256()
encrypt_sha256.update('haha'.encode())
print(encrypt_sha256.hexdigest(), ': ', len(encrypt_sha256.hexdigest()))
print('*'*50, 'sha256', '*'*50)

# sha384加密
encrypt_sha384 = sha384()
encrypt_sha384.update('haha'.encode())
print(encrypt_sha384.hexdigest(), ': ', len(encrypt_sha384.hexdigest()))
print('*'*50, 'sha384', '*'*50)

# sha512加密
encrypt_sha512 = sha512()
encrypt_sha512.update('haha'.encode())
print(encrypt_sha512.hexdigest(), ': ', len(encrypt_sha512.hexdigest()))
print('*'*50, 'sha512', '*'*50)
