# -#- coding:utf-8 -*-
# @Time:2019/12/2下午9:30
# @Author:liguangchun
# @File:t1.py

# age = int(input("请输入您的年龄：\n"))
# if age<18:
#     print("未成年人。")
# elif age<0:
#     print("请输入大于0的数字")
# else:
#     print("已成年。。。")

i = int(input("请输入一个数字："))
sum = 0
while i>0:
    sum += i
    i=i-2
print(sum)