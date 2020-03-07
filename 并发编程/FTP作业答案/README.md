#需求：
1. 用户加密认证
2. 允许多用户登录
3. 每个用户都有自己的家目录，且只能访问自己的家目录
4. 对用户进行磁盘分配，每一个用户的可用空间可以自己设置
5. 允许用户在ftp server上随意切换目录
6. 允许用户查看自己家目录下的文件
7. 允许用户上传和下载，保证文件的一致性（md5）
8. 文件上传、下载过程中显示进度条
9. 支持多并发的功能
10. 使用队列queue模块，实现线程池
11. 允许用户配置最大的并发数，比如允许只有10并发用户
升级需求：10%
1. 文件支持断点续传

#目录结构：
    客户端：
        |-conf
        |   |-setting.py        # 配置文件，存放服务端ip和port, 客户端下载文件的目录等
        |-core
        |   |-main.py            # FTP客户端功能
        |-files                    # 用户下载, 上传文件的存放目录
        |   |-.download             # 目录存放用户未下载完的文件的配置文件
        |-ftp_client.py             # 客户端启动程序
        
    服务端：
        |-conf
        |   |-settings.py            # 配置文件，存放服务端ip和port, 用户目录及用户账户, 日志目录, 与用户确认交互的状态码, 日志配置文件等等
        |   |-accounts.ini            # 用户账户相关的信息
        |-core
        |   |-handler_request.py    # 专门处理服务端就与客户端的请求, 以及命令
        |   |-main.py                # FTP服务端专门与客户端建立连接
        |   |-management.py            # 管理FTP的的启动, 停止, 重启等
        |   |-mythreadpool.py        # 使用queue实现的简单版的线程池, 缺点: 线程不能重复利用
        |-home    
        |   |-egon                    # 用户家目录，每一个用户以用户名作为家目录
        |   |   |-.upload             # 目录存放用户未上传完的文件的配置文件信息
        |   |-....                    # 每个用户下都有: 用户家目录，每一个用户以用户名作为家目录
        |       |-.upload             # 每个用户下都有: 用户未上传完的文件的配置文件信息
        |-ftp_client.py                 # 服务端启动程序

# 启动
    1.运行server文件下的ftp_server.py
    2.运行client文件下的ftp_client.py
    3.使用egon 123登陆
    4.下载的文件在files内，上传的文件在home下个人的空间内

# 用户配置信息
    用户名:                用户密码:
    alex                    123
    egon                    123
    ly                    123
    jzd                    123
    shx                    123

# 所有功能测试
(1) 登陆

    username>>:egon
    password>>:123
    用户名密码正确, 认证成功!
(2) 查看所有命令所对应的帮助信息

    命令 + –-help
    [egon@localhost ~]# ls --help
    [egon@localhost ~]# cd --help
    (3) ls: 查看
(3) ls: 查看

    查看当前目录下的文件
    [egon@localhost ~]# ls
    
    指定目录下的文件(只能查看到自己家目录的范围)
    [egon@localhost ~]# ls /目录1/目录2
    
    查看帮助信息
    [egon@localhost ~]# ls /?
(4) cd: 切换目录

    相对路径切换
    [egon@localhost ~]# cd /目录1
    
    切换到上一层目录
    [egon@localhost ~]# cd ..
    
    绝对路径切换
    [egon@localhost ~]# cd /目录1/目录2
    
    在当前目录下切当前目录
    [egon@localhost ~]# cd .
(5) mkdir: 创建目录(支持递归创建目录)

    相对路径创建:
    [egon@localhost ~]# mkdir /a
    2创建目录成功!
    
    生成多层递归目录:
    [egon@localhost ~]# mkdir /a/b
    创建目录成功!
(6) rmdir: 删除空目录
    
    删除空目录:
    [egon@localhost ~]# rmdir /a/b
    删除目录成功!
(7) remove: 删除文件
    
    删除文件
    [egon@localhost ~]# remove /1/a.txt
    删除文件成功!
(8) upload: 上传文件到服务端
    
    上传到服务端当前路径:
    [egon@localhost ~]# upload a.txt
    你可以上传文件, 在您上传之前, 您的目前空间:68.97MB!
    
    upload running...
    [##################################################] 100.00%
    upload succeed!
    上传文件成功, 您上传完后的剩余空间:66.07MB!
(9) resume_upload: 续传未上传完成的文件到服务端
    
    继续上传文件到服务端当前路径:
    [egon@localhost ~]# resume_upload 文件名
(10) download: 下载文件

    从服务端当前目录下下载文件
    [egon@localhost ~]# download a.txt

    download run...
    [##################################################] 100.00%
    download succeed!
(11) 在download基础之上: 继续从服务端续传下载文件

    用户登陆时会显示为下载完的文件
    根据序号选择要续传的文件即可
(12) 为用户磁盘配额

    上传文件成功, 您上传完后的剩余空间:4.02MB!
(13) 使用队列queue模块，实现线程, 允许用户配置最大的并发数5个
(14) 记录了日志功能
