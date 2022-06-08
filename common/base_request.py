import requests
import urllib3
from common import log

class BaseRequest:

    def __init__(self):
        self.session =requests.session()
        self.myLog = log.Log().logger

    def request(self,url,method,headers=None,params=None,data=None,json=None,file=None):
        # 打印请求信息日志，后续优化更新
        self.myLog.info("接口的请求地址是【{}】".format(url))
        self.myLog.info("接口的请求方法是【{}】".format(method))

        # 忽略警告
        urllib3.disable_warnings()

        response = self.session.request(url=url,method=method,\
                                        headers=headers,params=params,data=data,json=json,file=file)

