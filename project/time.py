from project.ner import *
#获取这段话中的时间段及其时间段截止下标


#test
def find_time(word,pos):#entity_dict没用上,分词和词性
    i = 0
    time=''
    time_list=[]
    # print(time_list)
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
            temp=str(start)+'-'+str(i-1)#str(start)是时间开始下标
            # print(temp)
            # time_dict[temp]=time_str #time_dic中存放分词中（时间实体开始下标-结束下标：时间实体）
            # temp=str(i-1)
            time=str(i-1)+'_'+time_str#时间段str：结束下标_时间段
            #start是时间开始下标，i-1是时间结束下标
            # num_start=int(str(start))
            # num_end=int(str(i-1))
            if(start>1):
                # print("word[start-1]:",word[start-1])
                # print("word[start-2]:",word[start-2])
                # print("word[i]:",word[i])
                if(word[start-1]=='生于' or word[start-2]=='出生' ):
                    continue
                elif(i!=len(pos) and (word[i]=='生' or word[i]=='出生')):
                    time_list
                else:
                    time_list.append(time)
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