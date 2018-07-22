from project.ner import *
from project.time import *
#提取实体的工作经历，list形式，[{时间：工作单位},{}，{}，{}]
def time_org(word,pos,netags):
    #时间和机构之间的关系
    time_dict=find_time(word,pos)#时间的字典{'11-11': '1956年', '133-135': '于2005年10月', '33-36': '2010年6月至10月',
    entity_dict = get_entity(netags, word)#人名 地名 机构名
    org_dict=entity_dict[2]#机构名的字典[{'72/29': '深圳发展银行'}, {'96/41': '深圳发展银行'}, {'119/53': '深圳发展银行'},
    #最后提取出来一个字典形式吧（时间：机构/关系）
    #"任"
    i1=0
    i2=0
    ren_list=[]#存放所有“任”出现的下标  #存放的是int类型
    while(i1<len(word)):
        if (word[i1]=='任' or word[i1]=='曾任' or word[i1] == '历任' or word[i1] == '就职' or word[i1] =='现任' or word[i1]=='兼任' or word[i1]=='出任' or word[i1]=='先后任' or word[i1]=='就读'or word[i1]=='加入'):
            #定义一个函数，在分词的i到j之间，找时间和实体以及关系
            #所以就需要把这个每次出现的词存在一个list中，每次取start为当前下标往前数几个存放时间的距离，往后到下一个任
            #到下一个任往前呢？还是到下一个任，把时间都存进一个list(time_list)，然后取第一个时间？
            ren_list.append(i1)#存放所有“任”出现的下标  #存放的是int类型
        i1+=1
    print(ren_list)
    while(i2<len(ren_list)):
        if(i2==0 and ren_list[i2]<=7 and i2<len(ren_list)-1):#第一个任，并且任所在下标小于7，并且有下一个任
            date = ren_ren_time(time_dict,0,ren_list[i2+1])#从开头到下一个任出现
            org = ren_ren_org(org_dict,0,ren_list[i2+1])
            if(org==''):print()
            else:
                print("date:",date)
                print("org:",org)
        elif(i2 == len(ren_list)-1):#i是分词中最后一个任了
            date = ren_ren_time(time_dict,ren_list[i2]-7,len(word))#从i往前数时间距离到句末
            org = ren_ren_org(org_dict,ren_list[i2],len(word))####应该是i2所在任的下标-7
            if (org == ''):
                print()
            else:
                print("date:", date)
                print("org:", org)
        else:
            date = ren_ren_time(time_dict,ren_list[i2]-7,ren_list[i2+1])#i2改成i2+1
            org = ren_ren_org(org_dict,ren_list[i2],ren_list[i2+1])
            if (org == ''):
                print()
            else:
                print("date:", date)
                print("org:", org)
        i2+=1
def ren_ren_time(time_dict,start,end):#返回在此范围内（两个任之间）最靠前的那个时间
    #在start到end之间找时间和实体以及关系
    ''' 找时间字典里面位置在start-end之间的时间，
    在时间字典里面提取key里面-后面的数字，只要在start-end之间，就把value提取出来。'''
    time_list=[]#存放start到end之间出现的时间序列
    time_index=[]#存放时间段在分词中最后的下标
    temp=end#如果这段话中出现多个时间下标，temp存放最小的那个
    time=''
    for key in time_dict:
        # time_index.append(int(key))
        index=int(key)
        if(index>=start and index<=end):#如果时间字典中出现了在范围内的，比较下标，选择下标最小的满足条件的时间段作为时间
            if(index<temp):
                temp=index
            time=time_dict[key]#改到上面
    print(time)
    return time

def ren_ren_org(org_dict,start,end):#找两个任之间的机构名，只要是机构名的字典里面所有出现的机构名都列出来
    temp=start
    org=""
    index=-1
    # print('org_dict:=======',org_dict)#org_dict其实是里面元素为dictionary的list
    for dict in org_dict:
        index+=1#org_dict  list的下标
        org_index=int((list(dict)[0].split('/'))[1])#机构名分词中的下标
        # print(index,"   ",start,"   ",end,"   ")
        if(org_index>end):
            break;#因为是list，所以后面的就不需要检验了
        if (org_index >= start and org_index <= end):
            # org+=(list(org_dict[index]))[1]
            # print ((org_dict[index]).values())
            print(dict[(list(org_dict[index]))[0]])#深圳发展银行
            # print((list(org_dict[index])))#['41/20']
            # print(org_dict[index])#{'41/20': '深圳发展银行'}

    # print(org)
    return org