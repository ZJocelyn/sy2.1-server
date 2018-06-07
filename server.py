# coding:utf8  
  
''''创建服务器端程序，用来接收客户端传进的字符数据'''  
  
from socket import *          #引入socket模块内的函数，创建一个套接口
from time import ctime        #引入time模块内的ctime()函数，ctime()函数会显示当前日期与时间
  
def server():              #定义server端函数
    HOST = '127.0.0.1'       #指定服务器ip为本机ip地址
    PORT = 65533             #指定监听端口为65533
    ADDR = (HOST,PORT)       #指定地址，以元组（host,port）的形式表示地址
    server_socket = socket(AF_INET,SOCK_STREAM)   #建立服务器之间的网络通信，建立基于TCP的流式套接口（SOCK_STREAM 类型是基于TCP的，有保障的面向连接的socket）
    server_socket.bind(ADDR)   #调用服务端的bind(address)函数，将套接字绑定到指定地址
    server_socket.listen(5)    #调用服务器端listen(backlog)监听函数开始监听TCP传入连接，backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量，该值至少为1，大部分应用程序设为5即可。
    while True:                
        print 'Waiting for connecting ......'            #显示'Waiting for connecting ......'等待client端发送数据
        tcpclientsocket,addr = server_socket.accept()    #调用服务器端accept()函数，接受client端TCP连接
        print 'Connected by ',addr                       #显示连接端地址
        while True:  
            data = serversocket.recv(1024)             #服务器接收来自客户端的数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。
            if not data:                                  #如果服务器没有接受到数据则跳出循环
                break                                     
            print data                                    #显示从客户端接收到的数据
            data = raw_input('Server>>')                  #调用raw_input()函数，读取在服务器端输入的内容，将数据以字符型式输出
            serversocket.send('[%s]%s'%(ctime(),data))       #发送TCP数据，将字符型数据发送到连接的客户端，客户端在收到数据同时也会收到接收数据的时间。
        servertsocket.close()               #一次会话结束，调用close()函数关闭套接字连接
    server_socket.close()      #会话结束，调用close()函数关闭服务器套接字
  
server()
