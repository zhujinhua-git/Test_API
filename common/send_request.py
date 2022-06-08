from common import base_request
from common.read_config_data import ReadConfData
from common.read_yaml_data import ReadData

class SendReuest:
    def __init__(self,test_data):
        self.test_data = test_data
        self.send = base_request.BaseRequest()
        self.readData = ReadConfData().get_host()


    def send_request(self):

        #获取接口信息
        path = self.test_data.path
        method = (self.test_data.methon).upper()
        headers = self.test_data.headers if self.test_data.headers else {}
        params = self.test_data.params if self.test_data.params else {}
        data = self.test_data.data if self.test_data.data else {}
        json = self.test_data.json if self.test_data.json else {}
        extract = self.test_data.extract if self.test_data.extract else {}
        parametrize = self.test_data.parametrize if self.test_data.parametrize else []
        validate = self.test_data.validate if self.test_data.validate else []
        url = self.readData.get_host() + path if self.read.get_host() else path

        result = self.send.request(url=url, method=method, \
                                   headers=headers, params=params, data=data, json=json)

        return result

if __name__ == '__main__':
    test_data1 = ReadData("上下文依赖的非参数化接口.yml").read_yaml()

    s =SendReuest(test_data1)
    s.send_request()