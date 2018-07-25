import configparser
import datetime
import sys

#获取配置
def get_config(section,key):
    config = configparser.ConfigParser()    # 注意大小写
    config.read("./config/config.conf")   # 配置文件的路径
    return config.get(section, key)


#获取word在sentence中的下标
def index_in_sentence(word,sentence):
    cut_tag = len(sentence)
    for index in range(len(sentence)):
        if sentence[index] == word:
            cut_tag = index
            break
    return cut_tag

#获取依存树的最大索引
def get_max_index(arcs,start_index,word):
    max_index = start_index
    while (start_index <= max_index and start_index < len(arcs)):
        arc_index = int(arcs[start_index])
        if arc_index > max_index:
            if judge_wp(word[arc_index]):
                break
            max_index = arc_index
        start_index += 1
    return max_index

#获取依存树最小索引
# def get_min_index(arcs,start_index,word):
#     min_index = start_index
#     temp_index = start_index
#     while(start_index >= 0):
#         start_index -= 1
#         if arcs[start_index] == temp_index:
#             min_index = start_index
#

    return max_index


def judge_wp(word):
    if word == "," or word == "、" or word == "。" or word =="，":
        return True
    return False

def replace_blank(sentence):
    return sentence.replace(" ","")
#list1:短 list2:长
def get_start_index(list1,list2):
    index = 0
    index1 = 0
    flag = False
    while(index < len(list1) and index1 < len(list2)):
        if list2[index1] != list1[index]:
            if flag:
                index = 0
            flag = False
        else:
            index+=1
            flag = True
        index1+=1
    return index1-len(list1)


def get_start_index1(list_long,list_short):
    # 两个均为单字分词的list进行匹配，在长list里面找短list，
    # 若找到，返回匹配处长list中第一个字符的下标，否则为null
    l = 0#list_long中的index
    s = 0
    num = 0  #匹配字符个数
    while(l<len(list_long) and s<len(list_short)):
        if(list_short[s] == list_long[l]):  #单个字符匹配
            s+=1
            l+=1
            num+=1
        else:
            if(num!=0):   #单个字符不匹配时前面已经有匹配的子串了
                s=0
                num=0
            else:
                l+=1
        if(num == len(list_short)):#如果匹配的数量等于短的list长度了，说明匹配完成了
            start_index=l-s  #匹配开始的地方
            # break
            return start_index
    if(l == len(list_long)):#长的list到头了
        start_index = -1
        return start_index



def get_up_position(position_number):
    if(position_number=="1"):
        position="中专及中专以下"
    elif(position_number=="2"):
        position="大专"
    elif(position_number=="3"):
        position="本科"
    elif(position_number=="4"):
        position="硕士研究生"
    elif(position_number=="5"):
        position="博士研究生"
    else:
        position="其他"
    return position

def get_now():
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    return nowTime

def change_none(word):
    if word is None:
        word = ""
    return word

def read_txt():
    school_name_list=[]
    with open('.\data\lexicon.txt','r',encoding='UTF-8-sig') as f:
        for line in f:
            school_name_list.append(line.strip('\n').strip())
    # print(school_name)
    return school_name_list

def get_single_list(word):
    single_list = []
    for s in word:
        single_list.append(s)
    return single_list



def get_front_wp(index,list):
    while(judge_wp(list[index])==False):
        index-=1
    return index

def get_back_wp(index,list):
    while (judge_wp(list[index]) == False):
        index += 1
    return index