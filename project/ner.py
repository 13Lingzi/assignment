# -*- coding: utf-8 -*-
import os
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from project.util import get_config

# import jieba


# 分句
# def cut_sentence(sentences):
#     sents = SentenceSplitter.split(sentences)
#     # sents=SentenceSplitter.split('亚甲硝酸盐是一种化学物质')
#     sentence = []
#
#     for s in '\n'.join(sents).split('\n'): sentence.append(s)
#     # print("分句：")
#     # print(sentence)
#     return sentence


# 分词
def cut_word(sentence):
    cws_model_path = os.path.join(get_config('ner','LTP_DATA_DIR'), 'cws.model')  # 分词模型路径，模型名称为`cws.model`
    word = []
    segmentor = Segmentor()  # 初始化实例
    segmentor.load(cws_model_path)  # 加载模型
    segmentor.load_with_lexicon(cws_model_path, get_config('ner','lexicon'))  # 加载模型
    word_split = segmentor.segment(sentence)
    for s in '/'.join(word_split).split('/'): word.append(s)
    segmentor.release()  # 释放模型
    return word


# 词性标注
def pos_tag(word):
    pos_model_path = os.path.join(get_config('ner','LTP_DATA_DIR'), 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
    postagger = Postagger()  # 初始化实例
    postagger.load(pos_model_path)  # 加载模型
    pos = []
    for s in '\t'.join(postagger.postag(word)).split('\t'): pos.append(s)  # 词性标注
    postagger.release()  # 释放模型
    return pos


# 实体标识
def ner_tag(word, pos):
    ner_model_path = os.path.join(get_config('ner','LTP_DATA_DIR'), 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
    recognizer = NamedEntityRecognizer()  # 初始化实例
    recognizer.load(ner_model_path)  # 加载模型
    netags = []
    for s in '\t'.join(recognizer.recognize(word, pos)).split('\t'): netags.append(s)  # 实体识别
    recognizer.release()  # 释放模型
    return netags

#实体识别:基础3大类，人名，地名，机构名
def get_entity(netags,word):
    per = []  # 人名
    org = []  # 机构名
    pla = []  # 地名
    result = []

    for index in range(len(netags)):
        s = netags[index]
        if "Nh" in s:
            if "S" in s:
                flag = False
                entity_dict = word_util(word, index, netags, flag)
                per.append(entity_dict)
            elif "B" in s:
                flag=True
                entity_dict = word_util(word, index,netags,flag)
                per.append(entity_dict)
        if "Ni" in s:
            if "S" in s:
                flag = False
                entity_dict = word_util(word, index, netags, flag)
                org.append(entity_dict)
            elif "B" in s:
                flag = True
                entity_dict = word_util(word, index, netags, flag)
                org.append(entity_dict)
        if "Ns" in s:
            if "S" in s:
                flag = False
                entity_dict = word_util(word, index, netags, flag)
                pla.append(entity_dict)
            elif "B" in s:
                flag = True
                entity_dict = word_util(word, index, netags, flag)
                pla.append(entity_dict)
        else:
            continue
    result.append(per)
    result.append(pla)
    result.append(org)
    return result

#命名实体识别整个流程
def ner(sentence):
    word = cut_word(sentence)
    pos = pos_tag(word)
    netags=ner_tag(word,pos)
    entity_dict = get_entity(netags, word)
    print(entity_dict)
    position_dict = get_position(entity_dict[2],word,pos)
    print(position_dict)


#防代码冗余
def word_util(word,index,netags,flag):
    #这个字典存放的是当前识别出来的完整实体其最后一个字的下标和其在分词list中的下标
    entity_dict={}
    words_temp = ""
    index_temp = index
    if flag:
        while "E" not in netags[index]:
            index += 1
    for index1 in range(index - index_temp + 1): words_temp += word[index_temp + index1]

    word_len = 0
    for i in range(index+1):
        word_len+=len(word[i])
    entity_dict[str(word_len-1)+'/'+str(index)]=words_temp
    return entity_dict


#获取岗位
def get_position(entity_dict,word,pos):
    position_dict = {}
    for entity in entity_dict:
        for key in entity.keys():
            index_str = key
        index = []  # index[0]是在句子中的下标，index[1]是在分词中的下标
        for s in index_str.split('/'): index.append(s)
        index_temp=int(index[1])+1
        index_temp1 = index_temp
        while (pos[index_temp1] != 'wp'):
            index_temp1+=1
        position_temp = ""
        for i in range(index_temp1-index_temp+1):
            position_temp += word[i+index_temp]
        position_dict[index[1]] = position_temp
    return position_dict



    
        




























