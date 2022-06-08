import pymysql
from common.read_yaml_data import ReadData
from common.log import Log

class DBConnect():
    '''Mysql数据的增删改查'''

    def __init__(self):
        db_conf = ReadData().get_db_info()
        # 调试时候用查看登陆信息
        # self.log =  Log().logger
        # self.log.info("数据库的登陆信息是%s" % db_conf)

        # 打开数据库,并以字典的形式返回操作结果
        self.db = pymysql.connect(cursorclass=pymysql.cursors.DictCursor,**db_conf)

        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def selector(self,sql):
        '''查询语句'''
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def excute(self,sql):
        '''删除，提交，修改语句'''
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 发生错误时候回滚
            self.db.rollback()

    def close(self):
        self.db.close()

if __name__ == '__main__':
    db=DBConnect()
    print(db.selector("select 1"))