# -*- coding: utf-8 -*-
#通过查找命名实体到距离最近的标点符号之间的部分认定为职务
import os
import jieba
LTP_DATA_DIR = 'Z:\\Users\\81269\\Anaconda3\\Lib\\site-packages\\pyltp-0.2.1.dist-info\\ltp_data_v3.4.0'  # ltp模型目录的路径
# LTP_DATA_DIR = 'C:\\Users\\81454\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\pyltp-0.2.1.dist-info\\ltp_data_v3.4.0\\ltp_data_v3.4.0'
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`

#分词
from pyltp import Segmentor
segmentor=Segmentor()#初始化实例
segmentor.load(cws_model_path)#加载模型
segmentor.load_with_lexicon(cws_model_path,'./data/lexicon.txt')
# words=segmentor.segment("理查德·杰克逊（RichardJackson）先生，执行董事、行长。1956年出生，英国特许注册保险师协会会员。2010年6月至今，任深圳发展银行执行董事；2010年6月至10月，任深圳发展银行代理行长；2010年10月至今，任深圳发展银行行长。1974年到1985年，理查德·杰克逊先生就职于英国商联保险公司，在伦敦，香港，新加坡都任过职。1985年到2005年，就职于花旗银行，历任花旗集团国际保险公司国际业务主管、亚太区金融机构主管、花旗银行匈牙利分行主席兼首席执行官、波兰Handlowy银行董事、花旗银行零售部韩国总经理、韩美银行（KoramBank）董事。理查德·杰克逊先生于2005年10月加入中国平安，并自2006年12月至2010年5月任平安银行行长。")
# words=segmentor.segment('邱萍女士，女，1970年9月出生，大专学历，中国国籍，高级会计师。2003年1月至2003年11月任湖北国创高新材料股份有限公司会计；2003年11月至2013年6月任湖北国创楚源投资管理有限公司财务总监、副总经理；2013年6月至今湖北国创房地产开发有限公司总会计师。')
# words=segmentor.segment('王利平女士，董事。1956年出生，获得南开大学货币银行学硕士学位，高级经济师。自2009年6月及2004年1月起分别出任中国平安保险（集团）股份有限公司执行董事、副总经理至今。2010年6月至今，任深圳发展银行第七届董事会非执行董事。王利平女士于1989年6月加入中国平安，2006年7月到2007年1月兼任中国平安副首席保险业务执行官。2005年8月到2006年7月任平安养老保险股份有限公司董事长兼总经理。2002年到2004年任中国平安人寿保险股份有限公司董事长兼首席执行官。1998年到2002年，先后任中国平安总经理助理和副总经理。1995年到1997年，先后任中国平安寿险管理本部总经理和寿险协理。1994年到1995年，任中国平安证券部总经理。')
# words=segmentor.segment('姚波先生，非执行董事。1971年出生，北美精算师协会会员（FSA）和美国精算师协会会员（MAAA），并获得美国纽约大学工商管理硕士学位。自2009年6月起出任中国平安保险（集团）股份有限公司执行董事，自2010年4月和2009年6月起分别出任中国平安首席财务官和副总经理，并自2004年2月兼任中国平安企划部总经理至今。2010年6月至今，任深圳发展银行第七届董事会非执行董事。姚波先生于2001年5月加入中国平安，2008年3月至2010年4月任中国平安财务负责人，2004年2月至2007年1月任中国平安财务副总监，2007年1月至2010年6月任中国平安总精算师，2002年12月至2007年1月任中国平安副总精算师，2001年至2002年曾任中国平安保险股份有限公司产品中心副总经理。此前，姚波先生任职德勤会计师事务所精算咨询高级经理。')
# words=segmentor.segment('欧几里得是西元前三世纪伟大的科学家')
words=segmentor.segment('自1995年起，任国务院发展研究中心研究员、国际合作局副局长等职。1998年，因研究工作贡献获政府特殊津贴。同年起至今，担任中国发展研究基金会副秘书长、秘书长。1999年，赴美国麻省理工大学担任访问学者。2010年，赴哥伦比亚大学Chazen国际商学院担任“LuluChowWang”高级访问学者。2002年至2003年，任国际劳工局全球化社会影响问题世界委员会成员，是该组织唯一的中国委员。此外，他还是中国财政学会第八届常务理事。2005年，卢迈先生领导完成的《中国人类发展报告2005》获联合国计划开发署“政策分析与影响奖”。2011年，国务院扶贫开发领导小组授予卢迈“全国扶贫开发先进个人”称号。')
print('\t'.join(words))
segmentor.release()

#词性标注
from pyltp import Postagger
postagger=Postagger()
postagger.load(pos_model_path)
postags=postagger.postag(words)
print('\t'.join(postags))
postagger.release()

#命名实体识别
from pyltp import NamedEntityRecognizer
recognizer=NamedEntityRecognizer()#初始化实例
recognizer.load(ner_model_path)
netags=recognizer.recognize(words,postags)
print('\t'.join(netags))

#提取机构名及其位置,机构名后面到标点符号之前判定为职称
def findPosition():
    i=0
    while(i<len(words)):
        if(netags[i]=='Ni'):
            print('机构名：',end='')
            print(words[i])#输出这个机构名称
            j=i    #j是机构名的最后下标
            i+=1
            org_end=i#机构名的最后一个坐标
            for m in range(j,i+1):#这种情况j i指向同一个地方
                print(words[m],end='')
            print('       职务：',end='')
            # print(words[j:i+1])
            # print(words[j])
            #输出职务名
            while(postags[i]!='wp'):
                i+=1
            for m in range(org_end+1,i):
                print(words[m],end='')
            print()
        elif(netags[i]=='B-Ni'):
            j=i
            print('机构名：',end='')
            while(netags[i]!='E-Ni'):
                i+=1
            for m in range(j, i + 1):
                print(words[m],end='')
            print('      职务名：',end='')
            org_end=i
                # print(words[j:i+1])
                # print(words[j])
            #输出职务
            while (postags[i] != 'wp'):
                i += 1
            for m in range(org_end + 1, i ):
                print(words[m], end='')
            print()

        else:
            i+=1


findPosition()

