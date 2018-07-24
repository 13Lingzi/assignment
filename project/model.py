from project.ner import *
from project.education_experience import education_detail
from project.work_experience import *
#命名实体识别整个流程
def ner(entity,segmentor,postagger,recognizer,sentence):
    entity.word = cut_word(segmentor,sentence)
    entity.pos = pos_tag(postagger,entity.word)
    entity.netags=ner_tag(recognizer,entity.word,entity.pos)
    entity.result = get_entity1(entity.netags, entity.word)
    get_university(entity, segmentor,sentence)
    print(entity.result)
    return entity.result

#提取学习经历整体流程
def education_experience(entity,parser,segmentor):
    education_list = education_detail(entity,parser,segmentor)
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
    work_list = work_relation(segmentor,postagger,recognizer,sentence)
    for s in work_list:
        s.print_work()

    # print(entity.work)
    #########
    # time_org(entity.word, entity.pos, entity.netags)#调用work_experience中的方法
    return work_list

