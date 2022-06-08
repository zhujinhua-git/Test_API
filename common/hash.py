from hashlib import sha1
from hashlib import md5

"""
封装各种加密方法，优化中

"""

def my_md5(msg):
    """
    md5 算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    """
    hl = md5()
    hl.update(msg.encode('utf-8'))
    return hl.hexdigest()


def my_sha1(msg):
    """
    sha1 算法加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    """
    sh = sha1()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()


print(my_md5('abcd123456'))