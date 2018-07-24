from project.util import index_in_sentence
# 分词
def cut_word(segmentor, sentence):
    word = []
    word_split = segmentor.segment(sentence)
    for s in '/'.join(word_split).split('/'): word.append(s)
    return word


# 词性标注
def pos_tag(postagger, word):
    pos = []
    for s in '\t'.join(postagger.postag(word)).split('\t'): pos.append(s)  # 词性标注
    return pos


# 实体标识
def ner_tag(recognizer, word, pos):
    netags = []
    for s in '\t'.join(recognizer.recognize(word, pos)).split('\t'): netags.append(s)  # 实体识别
    return netags


# 实体识别:基础3大类，人名，地名，机构名
def get_entity1(netags, word):
    per = []
    org = []
    pla = []
    result = []
    for index in range(len(netags)):
        s = netags[index]
        if "Nh" in s:
            if "S" in s:
                per.append(word[index])
            elif "B" in s:
                words_temp = ""
                index_temp = index
                while "E" not in netags[index]:
                    index += 1
                for index1 in range(index - index_temp + 1): words_temp += word[index_temp + index1]
                per.append(words_temp)
        if "Ni" in s:
            if "S" in s:
                org.append(word[index])
            elif "B" in s:
                words_temp = ""
                index_temp = index
                while "E" not in netags[index]:
                    index += 1
                for index1 in range(index - index_temp + 1): words_temp += word[index_temp + index1]
                org.append(words_temp)
        if "Ns" in s:
            if "S" in s:
                pla.append(word[index])
            elif "B" in s:
                words_temp = ""
                index_temp = index
                while "E" not in netags[index]:
                    index += 1
                for index1 in range(index - index_temp + 1): words_temp += word[index_temp + index1]
                pla.append(words_temp)
        else:
            continue
    result.append(per)
    result.append(pla)
    result.append(org)
    return result


# 实体识别:基础3大类，人名，地名，机构名
def get_entity(netags, word):
    per = {}  # 人名
    org = {}  # 机构名
    pla = {}  # 地名
    result = []

    for index in range(len(netags)):
        s = netags[index]
        if "Nh" in s:
            if "S" in s:
                flag = False
                per = word_util(word, index, netags, flag, per)
                # per.append(entity_dict)
            elif "B" in s:
                flag = True
                per = word_util(word, index, netags, flag, per)
                # per.append(entity_dict)
        if "Ni" in s:
            if "S" in s:
                flag = False
                org = word_util(word, index, netags, flag, org)
                # org.append(entity_dict)
            elif "B" in s:
                flag = True
                org = word_util(word, index, netags, flag, org)
                # org.append(entity_dict)
        if "Ns" in s:
            if "S" in s:
                flag = False
                pla = word_util(word, index, netags, flag, pla)
                # pla.append(entity_dict)
            elif "B" in s:
                flag = True
                pla = word_util(word, index, netags, flag, pla)
                # pla.append(entity_dict)
        else:
            continue
    result.append(per)
    result.append(pla)
    result.append(org)
    return result


# 实体修正
def entity_revise(entity_dict):
    return entity_dict


# 防代码冗余
def word_util(word, index, netags, flag, entity_dict):
    # 这个字典存放的是当前识别出来的完整实体其最后一个字的下标和其在分词list中的下标
    words_temp = ""
    index_temp = index
    if flag:
        while "E" not in netags[index]:
            index += 1
    for index1 in range(index - index_temp + 1): words_temp += word[index_temp + index1]

    word_len = 0
    for i in range(index + 1):
        word_len += len(word[i])
    entity_dict[str(word_len - 1) + '/' + str(index)] = words_temp
    return entity_dict


# 获取岗位
# def get_position(entity_dict,word,pos):
#     position_dict = {}
#     for key in entity_dict.keys():
#         index_str = key
#         index = []  # index[0]是在句子中的下标，index[1]是在分词中的下标
#         for s in index_str.split('/'): index.append(s)
#         index_temp=int(index[1])+1
#         index_temp1 = index_temp
#         while (pos[index_temp1] != 'wp'):
#             index_temp1+=1
#         position_temp = ""
#         for i in range(index_temp1-index_temp+1):
#             position_temp += word[i+index_temp]
#         position_dict[index[1]] = position_temp
#     return position_dict

# 获取学校实体
# 匹配：大学，学院，学校，研究生院
def get_university(Entity, segmentor, sentence):
    cut_tag = index_in_sentence('任', sentence)
    university = []
    temp_university = ""

    for index in range(len(Entity.result[2])):

        cut_word = ('/'.join(segmentor.segment(Entity.result[2][index])).split('/'))
        # print(cut_word)
        for index1 in range(len(cut_word)):
            university_tag = cut_word[index1]
            if university_tag == '大学' or university_tag == '学院' or university_tag == '学校':
                for i in range(index1 + 1): temp_university += cut_word[i]
                if index_in_sentence(temp_university[0], sentence) < cut_tag:
                    university.append(temp_university)
                    Entity.result[2][index] = ""
                    temp_university = ""
                break;
        cut_word.clear()

    Entity.result.append(university)
    Entity.result[2] = [i for i in Entity.result[2] if i != ""]

# 学校实体工具
# def university_util(cut_word,pos_out):
































