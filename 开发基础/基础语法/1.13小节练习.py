'''
练习1：猜年龄游戏 (10分钟)

要求：
允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
'''
age = 22
count = 0
while count < 3:  # 次数小于三次
    user_guess = int(input("请输入年龄："))  # 用户输入
    if user_guess < age:
        print("猜错了，再大一点")
    elif user_guess > age:
        print("猜错了，再小一点")
    else:
        print("恭喜你，猜对了")
        break
    count += 1
else:# 当while 循环正常执行完，中间没有被break 中止的话，就会执行else后面的语句
    print("次数满3次，你输了")

'''
练习2：猜年龄游戏升级版 (20分钟)

要求：
允许用户最多尝试3次
每尝试3次后，如果还没猜对，就问用户是否还想继续玩，
如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
如何猜对了，就直接退出
'''
age = 22
count = 0
while count < 3:  # 次数小于三次
    user_guess = int(input("请输入年龄："))  # 用户输入
    if user_guess < age:
        print("猜错了，再大一点")
    elif user_guess > age:
        print("猜错了，再小一点")
    else:
        print("恭喜你，猜对了")
        break
    count += 1
    if count  == 3:  # 判断，count清零即可
        u = input("是否还想继续玩……[输入y或n]：")
        if u != 'n':
            count = 0