import pika,sys

def fa(mes):
    # 开启socket
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='test')  # 声明队列以向其发送消息消息
    channel.basic_publish(exchange='', routing_key='test',body=mes)  # 注意当未定义exchange时，routing_key需和queue的值保持一致
    print('send success msg to rabbitmq')
    connection.close()  # 关闭连接

def shou():
    # 建立socket
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='test')
    def callback(ch, method, properties, body):
        '''回调函数,处理从rabbitmq中取出的消息'''
        if body:
            body = 'quit'
        print("吴伟夫: %s" % body.decode())
        connection.close()

    channel.basic_consume('test', callback, auto_ack=True)
    channel.start_consuming()  # 开始监听 接受消息



if __name__ == "__main__":
    mess = input('请输入消息')
    fa(mess)
    # shou()