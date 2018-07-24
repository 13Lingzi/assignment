import pymysql.cursors
import pymysql
# from project.util import get_config,get_now,change_none
from project.util import get_config,get_now



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
            print("执行count异常")
            self.sql_close(con)
        return result

    def insert_data(self,con,result,sql,table):
        flag = True
        # 执行sql语句
        try:
            with con.cursor() as cursor:
                cursor.execute(sql)
                con.commit()
        except:
            print("执行"+table+":insert_data异常:id："+str(result.did)+" name:"+result.name+"该条记录出错")
            con.rollback()
            self.sql_close(con)
            flag = False
        return flag


    #关闭数据库连接
    def sql_close(self,con):
        con.close();


    #获取insert_data_sql语句
    def insert_sql(self,judge,result,Education,Work,person):
        sql = ""
        if judge == "director":
            sql = "insert into "+get_config('db', 'table_director')+"(did,code,name,position,sex,age,education,position_title,create_time,modify_person) values("+str(result.did)+",'"+result.code+"','"+result.name+"','"+result.position+"','"+result.sex+"','"+result.age+"','"+result.education+"','"+result.position_title+"','"+get_now()+"','"+person+"')"

        if judge == "education":
            Education.time = change_none(Education.time)
            Education.university = change_none(Education.university)
            Education.education = change_none(Education.education)
            return "insert into "+get_config('db', 'table_education')+"(did,university,education,time,create_time,modify_person) values("+str(result.did)+",'"+Education.university+"','"+Education.education+"','"+Education.time+"','"+get_now()+"','"+person+"')"

        if judge == "work":
            Work.time = change_none(Work.time)
            Work.company = change_none(Work.company)
            Work.position = change_none(Work.position)
            sql = "insert into " + get_config('db',
                                             'table_work') + "(did,company,position,time,create_time,modify_person) values(" + str(result.did) + ",'" + Work.company + "','" + Work.position + "','" + Work.time + "','" + get_now() + "','" + person + "')"

        return sql