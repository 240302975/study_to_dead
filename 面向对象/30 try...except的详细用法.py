#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/5 0:14

# try..except...详细用法
# 1、异常类只能用来处理指定的异常情况，如果非指定异常则无法处理
s1 = 'hello'
try:
    int(s1)
except IndexError as e:  # 未捕获到异常，程序直接报错
    print(e)

# 2、多分支：被监测的代码块抛出的异常有多种可能性，
# 并且我们需要针对每一种异常类型都定制专门的处理逻辑
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)

# 3、万能异常Exception：被监测的代码块抛出的异常有多种可能性，
# 并且我们针对所有的异常类型都只用一种处理逻辑就可以了，那就使用Exception
s1 = 'hello'
try:
    int(s1)
except Exception as e:
    print(e)

# 4、也可以在多分支后来一个Exception
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)

# 5、异常的其他机构
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
# except Exception as e:
#     print('统一的处理方法')
else:
    print('try内代码块没有异常则执行我')
finally:
    print('无论异常与否,都会执行该模块,通常是进行清理工作')


# 6、主动触发异常:raise 异常类型（值）
class People:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError('名字必须传入str类型')
        if not isinstance(age, int):
            raise TypeError('年龄必须传入int类型')
        self.name = name
        self.age = age


p = People(333, 18)


try:
    raise TypeError('类型错误')
except Exception as e:
    print(e)


# 7、自定义异常
class EgonException(BaseException):  # 继承BaseException
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise EgonException('类型错误')  # print(obj)
except EgonException as e:
    print(e)


# 8、断言:assert 条件
info = {'name': 'egon', 'age': 18}

# if 'name' not in info:
# #     raise KeyError('必须有name这个key')
# # if 'age' not in info:
# #     raise KeyError('必须有age这个key')

assert ('name' in info) and ('age' in info)

if info['name'] == 'egon' and info['age'] > 10:
    print('welcome')


# 9、总结try..except
#   1：把错误处理和真正的工作分开来
#   2：代码更易组织，更清晰，复杂的工作任务更容易实现；
#   3：毫无疑问，更安全了，不至于由于一些小的疏忽而使程序意外崩溃了
