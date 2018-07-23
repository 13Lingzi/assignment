from project.ner import *
#获取这段话中的时间段及其时间段截止下标

def find_time(word,pos):#entity_dict没用上,分词和词性
    i = 0
    time=''
    time_list=[]
    while (i < len(pos)):
        tag = 1
        if (pos[i] == 'nt' or pos[i] == 'p'):
            if (pos[i] == 'p' and pos[i + 1] != 'nt'):
                i += 1
                continue
            start = i  # 时间序列的开始
            while ((tag == 1)):
                if (i == len(pos) - 1):
                    i += 1
                    tag = 0
                else:
                    i += 1
                    if ((pos[i] == 'nt') or (pos[i] == 'nd') or (pos[i] == 'c') or (pos[i] == 'p') or (
                        word[i] == '到')):
                        continue
                    else:
                        tag = 0
            time_str=''
            for n in range(start, i):
                time_str+=word[n]
            # print(time_str)
            # temp=str(start)+'-'+str(i-1)
            # time_dict[temp]=time_str #time_dic中存放分词中（时间实体开始下标-结束下标：时间实体）
            temp=str(i-1)
            time=str(i-1)+'_'+time_str#时间段str：结束下标_时间段
            time_list.append(time)
            # time_dict[temp]=time_str#时间字典中存放分词中时间段的结束下标
            # print(time_dict)
        else:
            i += 1
    # print(time_list)
    return time_list

def time(entity,segmentor,postagger,sentence):
    entity.word = cut_word(segmentor, sentence)
    entity.pos = pos_tag(postagger, entity.word)
    # netags = ner_tag(word, pos)
    # entity_dict = get_entity(netags, word)
    find_time(entity.word,entity.pos)