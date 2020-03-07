level = 'L0'


# n = 22
# dir = 333333

def func():
    level = 'L1'
    n = 33
    print(locals())

    def outer():
        n = 44
        level = 'L2'
        print("outer:", locals(), n)

        def inner():
            n = 55
            level = 'L3'
            print("inner:", locals(), n)  # 此处打印的n是多少？

        inner()

    outer()


func()
# 查找优先级locals > enclosing function > globals > builtins

# 全局范围：全局存活，全局有效
# 局部范围：临时存活，局部有效
