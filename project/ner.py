
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
def cut_word(segmentor,sentence):
    word = []
    word_split = segmentor.segment(sentence)
    for s in '/'.join(word_split).split('/'): word.append(s)
    return word


# 词性标注
def pos_tag(postagger,word):
    pos = []
    for s in '\t'.join(postagger.postag(word)).split('\t'): pos.append(s)  # 词性标注
    return pos


# 实体标识
def ner_tag(recognizer,word, pos):
    netags = []
    for s in '\t'.join(recognizer.recognize(word, pos)).split('\t'): netags.append(s)  # 实体识别
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
def ner(segmentor,postagger,recognizer,sentence):
    word = cut_word(segmentor,sentence)
    pos = pos_tag(postagger,word)
    netags=ner_tag(recognizer,word,pos)
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



    
        




























