from project.ner import cut_word
from project.util import *
from project.entity.education import *
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
'''
def education_detail(entity,parser,segmentor):
    arcs = parser_tag(parser, entity.word, entity.pos)
    university = entity.result[3]
    # for index in range(len(entity.word)):
    #     print(str(index) + ":" + entity.word[index] + arcs[index])
    education_list = []
    if university != None:
        for s in university:
            education = Education(s,None,None)
            education_str=""
            temp_cut_word = cut_word(segmentor,s)
            start_index = get_start_index(temp_cut_word,entity.word)
            end_index = start_index+len(temp_cut_word)-1
            max_index= get_max_index(arcs,start_index,entity.word)
            for index in range(max_index-end_index):
                if judge_wp(entity.word[end_index+index+1]):
                    break;
                add_word = entity.word[end_index+index+1]
                education_str+=add_word
            education.education = education_str
            education_list.append(education)
    return education_list
'''

def education_detail(entity,parser,segmentor):
    #得到教育对象列表，里面有属性university,deucation,time
    education_list=[]


    return education_list

def get_school(entity,sentence):
    #看句子中是否出现txt文件中的词，如果出现，就加到school_list中去
    school_name_list=read_txt()#txt中的学校名
    school_list=[] #存放sentence中出现的学校名
    sen=list(sentence)#简历中句子，单字分词
    # sentence=entity.word#分好的词
    for school in school_name_list:
        s=list(school)#学校名单字分词list[’北‘，’京‘，’大‘，’学‘]
        start_index=get_start_index1(sen,s)
        if(start_index!=-1):#说明学校在句子中
            school_list.append(school)
    print(school_list)










    return schlool_list

def university_ws():
    return