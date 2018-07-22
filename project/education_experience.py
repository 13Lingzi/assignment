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


def university_ws():
    return