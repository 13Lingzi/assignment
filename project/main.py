from  project.connect_mysql import ConnectMysql
from project.model import *
from project.education_experience import find_education
from project.initial import *
from project.entity.education import Education
from project.entity.ner_entity import Entity
from project.entity.Result import Result
from project.entity.work import Work
from project.util import *
from project.time import *


#数据库初始化信息
cm = ConnectMysql()
con = cm.connect()
#调用接口初始化
segmentor = segmentor_initial()
postagger = postagger_initial()
recognizer = recognizer_initial()
parser = parser_initial()

#获取遍历处理信息长度
len = cm.count(con)['count(*)']

#创建一个实体识别对象用于整个流程的处理
init_value=[]
entity = Entity(init_value,init_value,init_value,init_value)

#创建一个result对象用于整个流程的处理
education_list = []
work_list = []
result = Result(None,None,None,None,None,None,None,None,None,education_list,work_list)

for i in range(len):
# i=13755
# if i==13755:
#     获取用户信息
    cg_director = cm.read_excel(con, id=i+1)
    result.did = i+1
    result.code = cg_director['code']
    result.name = cg_director['name']
    result.position = cg_director['position']
    result.sex = cg_director['sex']
    result.age = cg_director['age']
    result.education = get_up_position(cg_director['education'])#写个util来对应实际的最高学历
    result.position_title = cg_director['position_title']
    result.resume = replace_blank(cg_director['resume'])

    resume = result.resume

    # 获取所有机构名
    ner(entity, segmentor, postagger, recognizer, resume)

    #获取教育经历
    result.education_list = education_experience(entity,parser,segmentor,resume,postagger)

    #获取工作经历
    result.work_list = work_experience(entity, segmentor, postagger, recognizer, resume)#调用的是model中的方法


    #导入数据库
    # insert_table(result,cm,con)


    #清空
    education_list.clear()
    work_list.clear()
    result = Result(None,None, None, None, None, None, None, None, None, education_list, work_list)
    print("---------------------------------------------------------------")
    i+= 1
# output(cm,con)
#关闭数据库,关闭调用的接口
cm.sql_close(con)
release_model(segmentor,postagger,recognizer)









