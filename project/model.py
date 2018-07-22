from project.ner import *

#命名实体识别整个流程
def ner(entity,segmentor,postagger,recognizer,sentence):
    entity.word = cut_word(segmentor,sentence)
    entity.pos = pos_tag(postagger,entity.word)
    entity.netags=ner_tag(recognizer,entity.word,entity.pos)
    entity.result = get_entity1(entity.netags, entity.word)
    get_university(entity, segmentor)
    print(entity.result)
    # entity_dict = get_entity(netags, word)
    # print(entity_dict)
    # position_dict = get_position(entity_dict[2],word,pos)
    # print(position_dict)

#提取学习经历整体流程
def education_experience():
    return

#提取工作经历整体流程
def work_experience():

    return