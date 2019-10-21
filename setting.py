import os

# 爬虫设置
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
async_number = 1

#更新
Auto_update = True
update_time = 60

# rabbitmq
rabbitmq_host = "127.0.0.1"
rabbitmq_user = "zzj"
rabbitmq_pwd = "123456"

# mysql
mysql_host = "127.0.0.1"
mysql_user = "root"
mysql_pwd = "123456"
mysql_port = 3306

# selenium
webdriver_path_win = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

# 环境路径
PATH = os.path.dirname(os.path.realpath(__file__))