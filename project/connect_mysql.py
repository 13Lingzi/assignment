import pymysql.cursors
import pymysql
from project.util import get_config


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


    #创建连接
    def connect(self):
        con = pymysql.connect(**self.config)
        return con

    def read_excel(self,con,id):
        # 执行sql语句
        try:
            with con.cursor() as cursor:
                sql = "select * from "+get_config('db','table')+" where id="+str(id)
                cursor.execute(sql)
                result = cursor.fetchone()
        except:
            print("执行read_excel异常")
            self.sql_close(con)

        return result
        # print(df.head)

    #读取数据表中数量
    def count(self,con):
        # 执行sql语句
        try:
            with con.cursor() as cursor:
                sql = "select count(*) from "+get_config('db','table')
                cursor.execute(sql)
                result = cursor.fetchone()
        except:
            print("执行read_excel异常")
            self.sql_close(con)
        return result

    #关闭数据库连接
    def sql_close(self,con):
        con.close();
