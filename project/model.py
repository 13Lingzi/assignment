from project.ner import *
from project.education_experience import education_detail
from project.work_experience import *
from project.connect_mysql import ConnectMysql
from project.util import get_config
from project.check import get_list_id

#命名实体识别整个流程
def ner(entity,segmentor,postagger,recognizer,sentence):
    entity.word = cut_word(segmentor,sentence)
    entity.pos = pos_tag(postagger,entity.word)
    entity.netags=ner_tag(recognizer,entity.word,entity.pos)
    #获取了所有的公司名和学校名
    entity.result = get_entity1(entity.netags, entity.word)
    #把学校拎出来了
    get_university(entity, segmentor,sentence)
    # get_university1(entity,sentence)

    print(entity.result)
    return entity.result

#提取学习经历整体流程
def education_experience(entity,parser,segmentor,sentence,postagger):
    education_list = education_detail(entity,parser,segmentor,sentence,postagger)
    for s in education_list:
        s.print_education()
    return education_list





#提取工作经历整体流程
def work_experience(entity,segmentor,postagger,recognizer,sentence):
    entity.word = cut_word(segmentor, sentence)
    entity.pos = pos_tag(postagger, entity.word)
    entity.netags = ner_tag(recognizer, entity.word, entity.pos)
    # entity_dict = get_entity(netags, word)
    # time_dict = find_time(word, pos)
    #########
    # entity.work=work_relation(segmentor,postagger,recognizer,sentence)
    work_list = work_relation(entity,segmentor,postagger,recognizer,sentence)
    for s in work_list:
        s.print_work()

    # print(entity.work)

    #########
    # time_org(entity.word, entity.pos, entity.netags)#调用work_experience中的方法
    return work_list


#入库操作
def insert_table(result,cm,con):

    #insert_director
    judge = "director"
    sql = cm.insert_sql(judge,result,None,None,get_config('developer', 'person'))
    flag = cm.insert_data(con,result,sql,judge)

    #insert_education
    judge = "education"
    for s in result.education_list:
        if flag:
            sql = cm.insert_sql(judge, result, s, None, get_config('developer', 'person'))
            flag = cm.insert_data(con,result,sql,judge)

    #insert_work
    judge = "work"
    for s in result.work_list:
        if flag:
            sql = cm.insert_sql(judge, result, None, s, get_config('developer', 'person'))
            flag = cm.insert_data(con,result,sql,judge)

def output(cm,con):
    sql = cm.output_sql()
    cm.output_excel(con,sql)









