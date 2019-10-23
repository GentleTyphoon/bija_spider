import pika
import time

def fa(mes):
    # 开启socket
    credentials = pika.PlainCredentials('admin', 'K^u2oFI@8Hv*')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='129.211.17.165', credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='buff_163')  # 声明队列以向其发送消息消息
    if mes == 'quit':
        connection.close()  # 关闭连接
    channel.basic_publish(exchange='', routing_key='test',body=mes)  # 注意当未定义exchange时，routing_key需和queue的值保持一致
    print('send success msg to rabbitmq')

def shou():
    # 建立socket
    print('开始接受')
    credentials = pika.PlainCredentials('admin', 'K^u2oFI@8Hv*')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='129.211.17.165', credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='buff_163')
    print('链接成功')
    def callback(ch, method, properties, body):
        '''回调函数,处理从rabbitmq中取出的消息'''
        body = body
        mess = body.decode()
        print(mess)
        if mess and mess == 'quit':
            connection.close()
    channel.basic_consume('test', callback, auto_ack=True)
    channel.start_consuming()  # 开始监听 接受消息


if __name__ == "__main__":
    # fa()
    shou()
