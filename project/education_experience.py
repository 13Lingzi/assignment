from project.ner import cut_word
from project.util import *
from project.entity.education import *
from project.time import find_time
#依存句法分析
def parser_tag(parser,word,pos):
    pars = []
    arcs = parser.parse(word, pos)
    for s in '\t'.join("%d" % (arc.head-1) for arc in arcs).split('\t'): pars.append(s)
    return pars

#可以写成枚举类型
def find_education(sentence):
    education=[]
    result=get_education(sentence)
    while result!=0:
        education.append(result)
        sentence=sentence.replace(edu_detail(result),"")
        result=get_education(sentence)
    return education


def get_education(sentence):
    if "中专" in sentence:
        return 1
    elif "大专" in sentence:
        return 2
    elif "本科" in sentence:
        return 13
    elif "学士" in sentence:
        return 23
    elif "硕士" in sentence:
        return 14
    elif "研究生" in sentence:
        return 24
    elif "博士" in sentence:
        return 5
    else:
        return 0

def edu_detail(word):
    if word==1:
        return "中专"
    elif word==2:
        return "大专"
    elif word==13:
        return "本科"
    elif word==23:
        return "学士"
    elif word==14:
        return "硕士"
    elif word==24:
        return "研究生"
    elif word==5:
        return "博士"
    else:
        return ""

def education_detail(entity,parser,segmentor,sentence,postagger):
    arcs = parser_tag(parser, entity.word, entity.pos)
    university = entity.result[3]
    # for index in range(len(entity.word)):
    #     print(str(index) + ":" + entity.word[index] + arcs[index])
    education_list = []
    time_list = find_time(entity.word,entity.pos)
    # print(time_list)
    if len(university) != 0:
        for s in university:
            education = Education(s,None,None)
            education_str = university_parser(segmentor,entity.word,arcs,s)
            education.education = education_str
            education_time = university_time(time_list,s,sentence)
            education.time = education_time
            education_list.append(education)
    else:
        education_detail_list = find_education(sentence)
        # sentence_cut = get_single_list(sentence)
        # for s in education_detail_list:
        #     s_cut = get_single_list(edu_detail(s))
        #     start_index = get_start_index(s_cut,sentence_cut)-1
        #     front_wp_index = get_front_wp(start_index,sentence_cut)
        #     back_wp_index = get_back_wp(start_index,sentence_cut)
        #     new_sentence = sentence[front_wp_index+1:back_wp_index]
        #     new_sentence_cut = cut_word(segmentor,new_sentence)
        #     pos = pos_tag(postagger,new_sentence_cut)
        #     arcs = parser_tag(parser,new_sentence_cut,pos)
        #     for index in range(len(new_sentence_cut)):
        #         print(str(index) + ":" + new_sentence_cut[index] + arcs[index])
        #     for index in range(len(new_sentence_cut)):
        #         if new_sentence_cut[index] == edu_detail(s):
        #             s_index = index
        #
        #     print(new_sentence)
        # print(education_detail_list)
    return education_list


# def education_detail(entity,parser,segmentor):
#     #得到教育对象列表，里面有属性university,deucation,time
#     education_list=[]
#     return education_list




def university_ws():
    return


def university_parser(segmentor,word,arcs,str):
    education_str = ""
    temp_cut_word = cut_word(segmentor, str)
    start_index = get_start_index(temp_cut_word, word)
    end_index = start_index + len(temp_cut_word)-1
    max_index = get_max_index(arcs, start_index, word)
    for index in range(max_index - end_index):
        if judge_wp(word[end_index + index + 1]):
            break;
        add_word = word[end_index + index + 1]
        education_str += add_word
    return education_str

def university_time(time_list,s,sentence):
    time = ""
    s_index = get_start_index(list(s),list(sentence))
    wp_index = s_index
    while (wp_index > 0):
        temp = list(sentence)[wp_index]
        if temp == "。" or temp == ";" or temp =="；":
            break;
        wp_index -=1
    for value in time_list:
        time_value = value.split("_")[1]
        time_index = get_start_index(list(time_value),list(sentence))
        if time_index > wp_index and time_index < s_index:
            time += time_value
    return time