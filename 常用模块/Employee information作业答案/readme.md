# 实现功能： #
    程序启动后，给用户提供接口，实现增删改查的需求
    1查⽂件(find)
        find name,age from staff_table where age > 22
        find * from staff_table where dept = "IT"
        find * from staff_table where enroll_data like "2013"
    2.添加员⼯信息（比对⽤户的⼿机号，重复会提示用户已存在）
        add staff_table Mosson,18,13678789527,IT,2018-12-11
    3.删除员⼯信息（根据序号删除相应员⼯的信息）
        del from staff_table where id = 10
    4.修改员⼯信息（可以根据特殊条件修改员⼯信息）
        update staff_table set dept="Market" where dept = "IT"
        update staff_table set age=25 where name = "Alex Li"
# 开发环境： #
	Python 3.5.2
# 启动方式： #
    打开CMD
	进入到Employee information.py文件所在的目录
	执行Employee information.py
	配套文本文件为staff_table
# 登录信息： #
    不需要登陆
# 运行效果： #
    程序启动
        ***************欢迎来到员工查询系统***************
        请根据以下提示输入对应指令序号：
        1.查询员工信息
        2.创建员工信息
        3.删除员工信息
        4.修改员工信息
    >>>:1
    退出请按Q
    ---------------我们支持以下查询语句---------------
    
                find name,age from staff_table where age > 22
                find * from staff_table where dept = "IT"
                find * from staff_table where enroll_date like "2013"
                请输入您的查询语句：
    <<<:find name,age from staff_table where age > 22
    -----本次查询的结果如下：-----
    name   age
    Alex Li , 25
    Jack Wang , 28
    Mack Qiao , 44
    Rachel Chen , 23
    Shanshan Du , 26
    满足本次查询的个数为： 5
    退出请按Q
###
    请根据以下提示输入对应指令序号：
            1.查询员工信息
            2.创建员工信息
            3.删除员工信息
            4.修改员工信息
    >>>:2
    支持以下语句新建员工信息：)
            add staff_table Shanshan Du,26,13698424612,Operation,2017-07-02
            退出请按Q
    请输入新建命令的SQL语句：add staff_table Shanshan Du,26,13698424612,Operation,2017-07-02
    您输入的用户已存在
###
    请根据以下提示输入对应指令序号：
            1.查询员工信息
            2.创建员工信息
            3.删除员工信息
            4.修改员工信息
    >>>:3
    支持以下语句删除员工信息：
            del from staff_table where id = 10
            退出请按Q
    请输入删除命令的SQL语句：del from staff_table where id = 10
    本次删除的数目为： 1
###
    请根据以下提示输入对应指令序号：
            1.查询员工信息
            2.创建员工信息
            3.删除员工信息
            4.修改员工信息
    >>>:4
    支持以下语句修改员工信息，包括部门名称与年龄:
            UPDATE staff_table SET dept="Market" WHERE dept = "IT"
            UPDATE staff_table SET age=25 WHERE name = "Alex Li"
            退出请按Q
    请输入您要操作的语句：
    <<<:UPDATE staff_table SET age=25 WHERE name = "Alex Li"
    信息已更新！
    本次更新信息数目为： 1