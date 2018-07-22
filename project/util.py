import configparser

#获取配置
def get_config(section,key):
    config = configparser.ConfigParser()    # 注意大小写
    config.read("./config/config.conf")   # 配置文件的路径
    return config.get(section, key)



def get_up_position(position_number):
    if(position_number==1):
        position="中专及中专以下"
    elif(position_number==2):
        position="大专"
    elif(position_number==3):
        position="本科"
    elif(position_number==4):
        position="硕士研究生"
    elif(position_number==5):
        position="博士研究生"
    else:
        position="其他"
    return position