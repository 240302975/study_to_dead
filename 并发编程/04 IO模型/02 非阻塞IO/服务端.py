from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8083))
server.listen(5)
server.setblocking(False)
print('starting...')

rlist = []
wlist = []
while True:

    try:
        conn, addr = server.accept()
        rlist.append(conn)
        print(rlist)
    except BlockingIOError:
        # print('干其他的活')

        # 收消息
        del_rlist = []
        for conn in rlist:
            try:
                data = conn.recv(1024)  # 起到检测“操作是否完成”
                if not data:
                    del_rlist.append(conn)
                    continue
                wlist.append((conn, data.upper()))  # 存放套接字以及套接字要发的数据
            except BlockingIOError:
                continue
            except Exception:  # 客户端断开
                conn.close()
                del_rlist.append(conn)

        # 发消息
        del_wlist = []
        for item in wlist:
            try:
                conn = item[0]
                data = item[1]
                conn.send(data)
                del_wlist.append(item)
            except BlockingIOError:  # 捕捉异常
                pass

        for item in del_wlist:
            wlist.remove(item)

        for conn in del_rlist:
            rlist.remove(conn)  # 删除链接

server.close()

'''
1.循环调用recv()将大幅度推高CPU占用率；这也是我们在代码中留一句time.sleep(2)的原因,否则在低配主机下极容易出现卡机情况
2. 任务完成的响应延迟增大了，因为每过一段时间才去轮询一次read操作，而任务可能在两次轮询之间的任意时间完成。
这会导致整体数据吞吐量的降低。
'''