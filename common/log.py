import logging
import os
import time
from common.consts import BASE_PATH

class Log:
    '''
    说明:封装log方法
    分别输出日志到文件、控制台
    log文件命名规则：日期命名
    '''

    def __init__(self):
        self.logName = os.path.join(BASE_PATH,'log/{}.log'.format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        # 创建一个fileHandler，用于输出日志到文件
        fh = logging.FileHandler(self.logName,encoding="utf-8")
        self.logger.addHandler(fh)
        fh.setFormatter(self.formatter)
        fh.setLevel(logging.INFO)

        # 创建一个StreamHandler，用于输出日志到文件
        sh = logging.StreamHandler()
        self.logger.addHandler(sh)
        sh.setLevel(logging.INFO)
        sh.setFormatter(self.formatter)


if __name__ == '__main__':
    logger = Log().logger
    logger.info("---测试开始---")
    logger.debug("---测试结束---")

