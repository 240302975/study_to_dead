**概述：**
本次作业文件夹一共包含了以下4个文件：
    流程图：员工信息表思路流程图
    程序文件: run_program.py
    用户信息文件：staff_info.txt
    程序说明文件：README.md
 
 
**一，程序功能**
1.可进行模糊查询，语法至少支持下面3种查询语法:
     
    find name,age from staff_table where age > 22
     
    find * from staff_table where dept = "IT"
     
    find * from staff_table where enroll_date like "2013"
2.可创建新员工纪录，以phone做唯一键(即不允许表里有手机号重复的情况)，staff_id需自增
     
    语法: add staff_table Alex Li,25,134435344,IT,2015-10-29
3.可删除指定员工信息纪录，输入员工id，即可删除
     
    语法: del from staff where  id=3
4.可修改员工信息，语法如下:
     
    UPDATE staff_table SET dept="Market" WHERE  dept = "IT" 把所有dept=IT的纪录的dept改成Market
    UPDATE staff_table SET age=25 WHERE  name = "Alex Li"  把name=Alex Li的纪录的年龄改成25
5.以上每条语名执行完毕后，要显示这条语句影响了多少条纪录。 比如查询语句 就显示 查询出了多少条、修改语句就显示修改了多少条等。
 
 
**二，部分变量说明**
    prompt_func() 欢迎登录的函数名
    initial_employee_information() 初始化员工信息的函数名
    find_func()  查找函数名
    add_func()   添加函数名
    del_func()   删除函数名
    update_func()  更新函数名
    main()    主函数
    staff_infofile  读取文件后，存放文件内容的变量
    user_input   用户输入
    core_message 用户添加的信息内容
    DATA_STAFF 初始化数据，定义成常量
    after_update_name  更新后的名称
    after_update_content  更新后的内容
    before_update_name  更新前的名称
    before_update_content  更新前的内容
     
     
**三，运行代码**
    本程序的开发环境是python3.x
    运行后，根据控制台显示的提示信息执行