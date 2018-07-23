import configparser

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
    while (start_index <= max_index):
        arc_index = int(arcs[start_index])
        if arc_index > max_index:
            if judge_wp(word[arc_index]):
                break
            max_index = arc_index
        start_index += 1
    return max_index

def judge_wp(word):
    if word == "," or word == "、" or word == "。":
        return True
    return False

def replace_blank(sentence):
    return sentence.replace(" ","")

def get_start_index(list1,list2):
    index = 0
    index1 = 0

    while(index < len(list1) and index1 < len(list2)):
        if list2[index1] != list1[index]:
             index1+=1
        else:
             index+=1
             index1+=1
    return index1-len(list1)+1



