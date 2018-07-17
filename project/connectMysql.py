import pymysql.cursors
import pymysql
from project.util import get_config

import pandas as pd

class ConnectMysql(object):
    # 连接配置信息
    config = {
        'host': get_config('db','host'),
        'port': int(get_config('db','port') ),  # MySQL默认端口
        'user': get_config('db','user'),  # mysql默认用户名
        'password':get_config('db','password'),
        'db': get_config('db','db'),  # 数据库
        'charset': get_config('db','charset'),
        'cursorclass': pymysql.cursors.DictCursor,
    }



    def connect(self,id):
        # 创建连接
        con = pymysql.connect(**self.config)
        # 执行sql语句
        try:
            with con.cursor() as cursor:
                sql = "select * from cg_director_test where id="+str(id)
                cursor.execute(sql)
                result = cursor.fetchone()

        finally:
            con.close();
        # df = pd.DataFrame(result)  # 转换成DataFrame格式
        # df.head()
        return result
        # print(df.head)

    def count(self):
        # 创建连接
        con = pymysql.connect(**self.config)
        # 执行sql语句
        try:
            with con.cursor() as cursor:
                sql = "select count(*) from cg_director_test"
                cursor.execute(sql)
                result = cursor.fetchone()
        finally:
            con.close();
        # df = pd.DataFrame(result)  # 转换成DataFrame格式
        # df.head()
        return result
        # print(df.head)

