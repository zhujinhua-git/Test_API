import os
from configparser import ConfigParser
from common.log import Log


class Config:

    '''配置文件的增删改查'''


    def __init__(self):
        self.config = ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')
        #  配置文件路径错误抛出异常
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")
        #  读取配置文件
        self.config.read(self.conf_path, encoding='utf-8')

    # 读取配置
    def get_config(self,section,option):

        return self.config.get(section,option)

    # 新增一个配置块
    def add_config(self,section):
        self.config.add_section(section)
        #写入到文件中，这句代码等同于with open后as出一个文件句柄
        self.config.write(open(self.conf_path,"w+"))

    # 新增配置块的内容
    def set_config(self,section,option,value):
        self.config.set(section,option,value)
        self.config.write(open(self.conf_path,"w+"))

    # 删除配置文件块，整个文件块所有内容被删除
    def remove_section(self,section):
        self.config.remove_section(section)
        self.config.write(open(self.conf_path,"w+"))

    # 删除配置块内容
    def remove_option(self,option,value):
        self.config.remove_option(option,value)
        self.config.write(open(self.conf_path,"w+"))

if __name__ == '__main__':
    con = Config()
    # res = con.get_config("release","host")
    # con.add_config("zhujinhua")
    # con.set_config("zhujinhua","age","18")
    # con.remove_section("zhujinhua")
    # con.remove_option("zhujinhua","age")



