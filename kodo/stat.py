from qiniu import Auth
from qiniu import BucketManager
access_key = 'AK'
secret_key = 'SK'

#初始化Auth状态
q = Auth(access_key, secret_key)
#初始化BucketManager
bucket = BucketManager(q)

#你要测试的空间， 并且这个key在你空间中存在
bucket_name = '2018_11_16'
key = 'test11.png'
#获取文件的状态信息
ret, info = bucket.stat(bucket_name, key)
print(info)
assert 'hash' in ret