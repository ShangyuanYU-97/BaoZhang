# 1. float
num1 = 1
str1 = '10'
print(1)
print(type(float(num1)))
print(float(num1))
print(float(str1))
print(type(float(str1)))

# 2. str将数据转换成字符串
print(2)
print(type(str(num1)))

# 3.tuple 将一个序列转换成元组
print(3)
list1 = [10, 20, 30]
print(tuple(list1))
print(type(tuple(list1)))

# 4.list 将一个序列转换成列表
print(4)
list2 = (10, 20, 40)
print(list(list2))
print(type(list(list2)))

# 5.eval() 计算字符串中有效的表达式，并返回一个对象
print(5)
a = '1'
b = '1.1'
c = '(10, 20, 30)'
d = '[1000, 300, 5000]'
print(f'a转换的值为{eval(a)} \t 转换后的类型为{type(eval(a))}')
print(f'b转换的值为{eval(b)} \t 转换后的类型为{type(eval(b))}')
print(f'c转换的值为{eval(c)} \t 转换后的类型为{type(eval(c))}')
print(f'd转换的值为{eval(d)} \t 转换后的类型为{type(eval(d))}')

