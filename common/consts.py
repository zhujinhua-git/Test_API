import os
'''
全局变量
'''

# 接口全局配置
API_ENVIRONMENT_DEBUG = 'debug'
API_ENVIRONMENT_RELEASE = 'release'

# 项目根目录
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

# 接口响应时间list，单位毫秒
STRESS_LIST = []

# 接口执行结果list
RESULT_LIST = []