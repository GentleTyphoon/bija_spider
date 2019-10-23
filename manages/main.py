import requests
import setting as set
from tools.Sliding_verification import CrackSlider
from queue import Queue
from threading import Thread
import asyncio

#主函数
class MySpider:
    def __init__(self):
        self.spider_name = ''
        self.allow_code = []
        self.async_number = set.async_number
        self.myheaders = set.my_headers
        self.mycookies = False
        self.myproxy = False

        #mysql配置
        self.mysql_add = set.mysql_host
        self.mysql_user = set.mysql_user
        self.mysql_pwd = set.mysql_pwd
        self.mysql_port = set.mysql_port
        self.BDname = ""
        self.table_name = ""

        # RabbitMq配置
        self.rabbitmq_host = "127.0.0.1"
        self.rabbitmq_user = "root"
        self.rabbitmq_pwd = ""

        self.my_queue = Queue()

    def produce(self, message=None):
        if self.function == 'p':
            pass
        elif self.funciton == 'C':
            pass

    def consume(self):
        '''
        消费函数
        :return:
        '''

    def start_loop(self, loop):
        """
        再后台一直接受loop事件
        :param loop:
        :return:
        """
        asyncio.set_event_loop(loop)
        loop.run_forever()

    def start_consume(self, ):
        """
        消费启动器， 负责把函数运行起来
        :return:
        """
        self.new_loop = asyncio.new_event_loop()

        loop_thread = Thread(target=self.start_loop, args=(self.new_loop,))
        loop_thread.setDaemon(True)
        loop_thread.start()

        save_data = Thread(target=self.save)
        save_data.setDaemon(True)
        save_data.start()

        self.consume()


    def yanzheng(self, message):
        c = CrackSlider()
        cook = c.crack_slider()
        return cook

    async def myrequest(self, message, ):
        '''
        请求函数
        :param message: 响应信息字典
        :return:
        '''
        try:
            print('开始请求页面,url为%s' % message['url'])
            #预先加载格式
            message = self.pretreatment(message)
            #请求前参数调整
            message = self.my_change(message)
            res = await requests(message, auto_proxy=self.auto_proxy, allow_code=self.allow_code)
            # #判断res是否为字典
            # if isinstance(res, dict):
            #     callback = res['callback']
            #     if callback and hasattr(res, callback):
            #         pass
        except:
            pass

    def pretreatment(self):
        '''
        请求配置
        :return:
        '''
        pass

    def my_change(self):
        '''
        请求中间件
        :return:
        '''
        pass

    def callback(self):
        '''
        回调函数
        :return:
        '''

    def myusave(self):
        '''
        存储选择
        :return:
        '''













