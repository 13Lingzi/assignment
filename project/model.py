from project.ner import *
from project.work_experience import *

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
def work_experience(entity,segmentor,postagger,recognizer,sentence):
    # word = cut_word(sentence)
    entity.word = cut_word(segmentor, sentence)
    # pos = pos_tag(word)
    entity.pos = pos_tag(postagger, entity.word)
    # netags = ner_tag(word, pos)
    entity.netags = ner_tag(recognizer, entity.word, entity.pos)
    # entity_dict = get_entity(netags, word)
    # time_dict = find_time(word, pos)
    time_org(entity.word, entity.pos, entity.netags)
    # return