from  project.connectMysql import ConnectMysql
from project.ner import ner
from project.education import find_education
from project.initial import *

#数据库初始化信息
cm = ConnectMysql()
con = cm.connect()
#调用接口初始化
segmentor = segmentor_initial()
postagger = postagger_initial()
recognizer = recognizer_initial()


cg_directors = []
len = cm.count(con)['count(*)']
for i in range(len):
    education = []
    work = []
    #获取用户信息
    cg_director = cm.read_excel(con, id=i+1)
    resume = cg_director['resume']
    name = cg_director['name']
    id = cg_director['id']


    #获取所有机构名
    ner(segmentor,postagger,recognizer,resume)
    # print(ner_result)
    # 获取用户学历
    education.append(find_education(resume))
    print(education)
    print("---------------------------------------------------------------")



#关闭数据库,关闭调用的接口
cm.sql_close(con)
release_model(segmentor,postagger,recognizer)









