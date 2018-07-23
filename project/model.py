from project.ner import *
from project.education_experience import education_detail

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
def work_experience():

    return