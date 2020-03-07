# 实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败!
import time

_user = "seven"
_password = "123"

username = input('请输入用户名：')
password = input('请输入密码：')

if username == _user and password == _password:
    print("欢迎 %s 登陆..." % _user)
    time.sleep(1)
    print("登录成功！")
else:
    print("用户名或密码错误！")

# 实现用户输入用户名和密码,当用户名为 seven 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
_user = "seven"
_password = "123"

count = 0
while count < 3:  # 当while后面的条件成立（True），才会执行它下面的代码
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == _user and password == _password:
        print("欢迎 %s 登陆..." % _user)
        break  # 跳出，中断
    else:
        print("用户名或密码错误!")
    count += 1
else:  # 只要上面的while循环正常执行，中间没被打断，就会执行else语句
    print("次数满3次，账户已锁定")

# 实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
count = 0
while count < 3:  # 当while后面的条件成立（True），才会执行它下面的代码
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == "seven" and password == "123":
        print("用户%s已登录成功！" % username)
        break  # 跳出，中断
    elif username == "alex" and password == "123":
        print("用户%s已登录成功！" % username)
        break
    else:
        print("用户名或密码错误!")
    count += 1
else:  # 只要上面的while循环正常执行，中间没被打断，就会执行else语句
    print("次数已满3次，账户已锁定")

# 使用 while 循环实现输出 1,2,3,4,5,7,8,9,11,12
count = 0
while count <= 12:
    count += 1
    if count == 6 or count == 10:
        continue
    print(count)

# 使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
count = 100
while count > 49:# 50也要打印
    print(count)
    count -= 1
    if count == 49:# 自减之后count清零
        count =0
        while count <= 50:# 再顺序输出
            print(count)
            count += 1
        break

# 使用 while 循环实现输出 1-100 内的所有奇数
count = 1
while count <= 100:
    if count % 2 !=0:
        print(count)
    count += 1

# 使用 while 循环实现输出 1-100 内的所有偶数
count = 1
while count <= 100:
    if count % 2 ==0:
        print(count)
    count += 1

# 使用while循环实现输出2-3+4-5+6…+100 的和
count = 2
total = 0
while count <= 100:
    if count % 2 == 0:
        total += count  # 偶数自加
    elif count % 2 == 1:
        total -= count  # 奇数自减
    count += 1
print("the sum is %s." % total)

"""
制作趣味模板程序（编程题）
    需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意显示
    如：敬爱可爱的xxx，最喜欢在xxx地方干xxx
"""
name = input("输入名字：")
address = input("输入地点：")
hobby = input("输入爱好：")
print("敬爱可爱的%s，最喜欢在%s干%s"%(name,address,hobby))

'''
输入一年份，判断该年份是否是闰年并输出结果。（编程题）
    注：凡符合下面两个条件之一的年份是闰年。 （1） 能被4整除但不能被100整除。 （2） 能被400整除。
'''
year = int(input("输入年份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("该年是闰年")
else:
    print("该年不是闰年")

# 假设一年期定期利率为3.25%，计算一下需要过多少年，一万元的一年定期存款连本带息能翻番？
count = 0.0325
deposits = 10000
year = 0
while deposits <= 20000:
    deposits = deposits * (1 + count)  # 本息=本金+利息
    year += 1
print(year)

'''
使用while,完成以下图形的输出。
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
i = 1
j = 4
while i <= 9:
    if i <= 5:
        print("* " * i)
    elif i > 5:
        print("* " * j)
        j -= 1  # 倒三角自减
    i += 1  # i代表高度

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
tour = 100  # 最开始落下为100
hei = 100.0
tim = 1
while tim < 10:# 次数
    hei /= 2
    print(tim)
    print(hei)
    tour += hei * 2 # 反弹+落下
    tim += 1
print('总高度:',tour)
print('第10次反弹高度:', hei / 2)  # 第10次反弹=第11次落下，所以需要/2