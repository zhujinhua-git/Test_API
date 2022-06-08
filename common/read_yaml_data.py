import yaml
import os
from common.consts import BASE_PATH
from conf.config import Config

class ReadData:

    '''
    读取yaml文件
    '''

    def __init__(self,yamlFileName):
        '''初始化函数'''
        self.yamlPath = os.path.join(BASE_PATH,"params",yamlFileName)
        self.conf = Config()
        if not os.path.isfile(self.yamlPath):
            raise FileNotFoundError("请确保yaml文件是否存在！")

    def read_yaml(self):
        ''' 读取yaml文件'''
        with open(self.yamlPath,encoding='utf-8',mode="r") as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value

    def write_yaml(self,data):
        '''写入yaml文件,写入的格式：[{,,,},{}]'''
        with open(self.yamlPath,encoding="utf-8",mode="a") as f:
            yaml.dump(data,stream=f,encoding="utf-8",allow_unicode=True)

    def clear_yaml(yamlPath):
        '''清空yaml文件'''
        with open(yamlPath,encoding="utf-8",mode="w") as f:
            f.truncate()

if __name__ == '__main__':
    pass