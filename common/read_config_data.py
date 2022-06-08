from conf.config import Config

class ReadConfData:
    '''
    读取conf目录下的config.ini文件内信息
    有新增配置时需要新增获取方法
    '''
    def __init__(self):
        self.conf = Config()

    def get_host(self):
        '''读取host地址,默认返回测试环境地址'''
        return self.conf.get_config("host","test_host")

    def get_db_info(self):
        '''读取mysql数据库登陆信息'''
        db_info = {
            "host": self.conf.get_config("mysql","MYSQL_HOST"),
            "user": self.conf.get_config("mysql","MYSQL_USER"),
            "password": self.conf.get_config("mysql","MYSQL_PASSWD"),
            "port": int(self.conf.get_config("mysql","MYSQL_PORT")),
            "database":self.conf.get_config("mysql","MYSQL_DB")
        }

        return db_info

if __name__ == '__main__':
    r = ReadConfData()
    print(r.get_db_info())