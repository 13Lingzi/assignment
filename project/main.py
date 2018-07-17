from  project.connectMysql import ConnectMysql
from project.ner import ner
from project.cgDirector import CgDirector
from project.education import find_education

cg_directors=[]

len=ConnectMysql.count(ConnectMysql)['count(*)']
for i in range(len):
    education=[]
    work=[]
    #获取用户信息
    cg_director = ConnectMysql.connect(ConnectMysql, id=i+1)
    resume=cg_director['resume']
    name=cg_director['name']
    id=cg_director['id']


    #获取所有机构名
    ner(resume)
    # print(ner_result)
    # 获取用户学历
    education.append(find_education(resume))
    print(education)
    print("---------------------------------------------------------------")



