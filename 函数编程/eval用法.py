
#
# names = ["alex","rain","jack"]
#
# f = open("eval_test","w")
# f.write(str(names) )


f = open("eval_test")
d = eval(f.read())  # 把字符串形式的list,dict,set,tuple,再转换成其原有的数据类型
print(type(d))
print(d[2])
