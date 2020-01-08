# -#- coding:utf-8 -*-
# @Time:2020/1/4上午11:50
# @Author:liguangchun
# @File:ReportApi.py
from os.path import join

import mysql.connector
import pymysql
from flask import Flask

host = 'localhost'
username = 'root'
password = '123456'
db_name = 'UserCenter'
_user_info = []
user = []

query_table_sql = """\
select *
from UserCenter.user 
"""

connection = pymysql.connect(host=host,
                             user=username,
                             password=password,
                             charset='utf8mb4',
                             db=db_name)

try:
    with connection.cursor() as cursor:
        print('--------------查询数据--------------')
        cursor.execute(query_table_sql)
        results = cursor.fetchall()
        # print(f'id\tname\tnickname\tbirthday')
        for row in results:
            _user_info.append(row[0])
            _user_info.append(row[1])
            _user_info.append(row[2])
            _user_info.append(row[3])
            # user.append(_user_info)
            # print(user)

        print(_user_info.__len__())

        sum = _user_info.__len__()
        n = 0
        while n < sum:
            # print(_user_info[sum-4:sum])
            user.append(_user_info[n:n+4])
            # sum = sum + n
            # sum = sum - 4;
            n = n + 4
        print(user)
        print("".join(user))

finally:
    connection.close()

app = Flask(__name__)

# select * from UserCenter.`user`;

@app.route('/')
def hello_world():
    return user

if __name__ == '__main__':
    app.run()