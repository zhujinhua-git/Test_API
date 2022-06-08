from common import consts
from common.log import Log
import json

class Assertion:
    '''
    封装断言方法，调试时候可以把raise打开，把错误抛出，执行用例后把raise屏蔽掉
    '''

    def __init__(self):
        self.mylog = Log().logger

    def assert_code(self,code,expected_code):
        '''
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        '''
        try:
            assert code == expected_code
            return True
        except:
            self.mylog.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            consts.RESULT_LIST.append("Fail")



    def assert_body(self,body, msg,expected_msg):
        '''
        验证response body中任意属性的值
        :param body:
        :param msg:
        :param expected_msg:
        :return:
        '''

        try:
            msg = body[msg]
            assert msg == expected_msg
            return True
        except:
            self.mylog.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, msg))
            consts.RESULT_LIST.append("Fail")

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            self.mylog.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            consts.RESULT_LIST.append('fail')



    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            self.mylog.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            consts.RESULT_LIST.append('fail')



    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            self.mylog.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            consts.RESULT_LIST.append('fail')

            raise




if __name__ == '__main__':
    a = Assertion()
    a.assert_code(1,2)
    a.assert_in_text("a","abc")
    print(consts.RESULT_LIST)