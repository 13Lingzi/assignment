from project.ner import *
from project.time import *
from project.entity.work import Work
#提取实体的工作经历，list形式，[work1,work2,...]每个work都是一个对象，里面包含了属性：时间，单位，职位

def work_obj(time_input,company_input,position_input):#输入：work对象的属性值 输出：work对象
    #创建work对象，并给属性赋值
    time=''
    company=''
    position=''
    work = Work(time,company,position)# new一个work对象
    work.time=time_input
    work.company=company_input
    work.position=position_input
    return work

def work_relation(segmentor,postagger,recognizer,sentence):#big function
    work_obj_list=[]
    word = cut_word(segmentor, sentence)#list
    pos = pos_tag(postagger, word)#词性
    netags = ner_tag(recognizer, word, pos)
    company_list=f_company_list(word,netags)
    for index_comp in company_list:#list里面每个元素都是str
        company=(index_comp.split('_'))[1]
        position=f_position_str(index_comp,pos,word)
        time=f_time_str(index_comp,word,pos)
        #每个公司实体都对应一个world对象
        work=work_obj(time,company,position)
        # print(time, '--', company, '--', position)
        work_obj_list.append(work)#把上面函数返回的work对象加到list中
    # print(work_obj_list)
    return work_obj_list





def f_company_list(word,netags,):
    #得到company_list，里面每个元素都是字符串：下标_实体
    company_1=(get_entity1(netags,word))[2]#公司实体
    company_list=[]
    temp=""
    for i in range(0,len(netags)):
        if(netags[i]=='B-Ni'):
            start=i  #start--B-Ni
            while(netags[i]!='E-Ni'):
                i+=1
            end=i     #end--E-Ni
        elif(netags[i]=='Ni'):
            start=end=i
        else:
            start=end=-1
        #有了start end，找对应坐标word里面的实体是否为company
        if(start>=0):
            str1=''
            for j in range(start,end+1):
                str1+=word[j]   #实体名称
            if(str1 in company_1):
                # temp[end]=str
                temp=str(end)+'_'+str1
                company_list.append(temp)
    # company_list.append(temp)
    return company_list


def f_time_str(index_comp,word,pos):
    #从公司实体往前推，第一个时间段，只要中间没有句号或者分号，就收为其时间
    index = int((index_comp.split('_'))[0])#公司实体下标
    time_list=find_time(word,pos)#时间段结束下标_时间段
    index_list=[]#存放这句话中时间段结束下标
    # timeseg_list=[]#存放这句话中时间段，与index_list对应   可能会重复导致删除相同元素
    for time in time_list:
        index_list.append(int((time.split('_'))[0]))
        # timeseg_list.append((time.split('_'))[1])
    i=index#计数
    while(pos[i]!='。'):#从后往前推,只要是没有遇到句号，就继续往前推
        i-=1
        if(i==0 and pos[i]!='nt'):#从后往前推到第一个词还不是时间，那就说明没有时间了
            time_str='null'
            break
        elif(i==0 and pos[i]=='nt'):#从后往前推，第一个是时间,
            time_str=word[i]
            break
        elif(i in index_list):#推到了这个下标等于时间段的下标
            xiabiao=index_list.index(i)#i在index_list中的下标，也就对应在Time_list中的下标
            time_str=(time_list[xiabiao].split('_'))[1]
            break
        else:#往前还没有推到时间
            continue
    return time_str


def f_position_str(index_comp,pos,word):
    #从公司实体到标点符号(除去顿号，前后括号以及前后引号）
    index=int((index_comp.split('_'))[0])
    start=index+1
    position_str=''
    for i in range(start,len(word)):
        if(word[i]=='，' or word[i]=='；' or word[i]=='。'):
            end=i
            break
    for j in range(start,end):
        position_str+=word[j]
    return position_str



















