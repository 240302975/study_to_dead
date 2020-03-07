# 笨逼方法
score = int(input("输入你的分数:"))
if 90 <= score <=100:
    print("A")
elif 80 <= score <=89:
    print("B")
elif 60 <= score <=79:
    print("C")
elif 40 <= score <=59:
    print("D")
elif 0 <= score <= 39:
    print("E")
else:
    print("NO")

# 判断成绩
score = int(input("输入分数:"))
if score > 100:
    print("我擦，最高分才100...")
elif score >= 90:  # 代码是从上到下依次判断，只要满足一个，就不会再往下走
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
elif score >= 40:
    print("D")
else:
    print("太笨了...E")

# 猜随机数字
import random
n = random.randint(0,3)
user_guess = int(input("input your guess:"))
if user_guess > n:
    print("try smaller...")
elif user_guess < n:
    print("try bigger...")
else:
    print("bingo,you get it!")
# print(n)

# while循环
count = 0
while count <= 100:  # 只要count<=100就不断执行下面的代码
    print("loop ", count)
    count += 1  # 每执行一次，就把count+1，要不然就变成死循环啦，因为count一直是0

# 输出100以内所有偶数
count = 0
while count <= 100:  # 只要count<=100就不断执行下面的代码
    if count % 2 == 0:  # 判断是否为偶数
        print("loop ", count)
    count += 1  # 每执行一次，就把count+1，要不然就变成死循环啦，因为count一直是0

# 猜3次
import random
n = random.randint(0, 3)
count = 0
while count < 3:
    user_guess = int(input("input your guess:"))
    if user_guess > n:
        print("try smaller...")
    elif user_guess < n:
        print("try bigger...")
    else:
        print("bingo,you get it!")
        break
    count += 1

# while…else…
count = 0
while count <= 5 :
    count += 1
    if count == 3:break
    print("Loop",count)
else:
    print("循环正常执行完啦")
print("-----out of while loop ------")