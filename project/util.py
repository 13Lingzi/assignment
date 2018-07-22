import configparser

#获取配置
def get_config(section,key):
    config = configparser.ConfigParser()    # 注意大小写
    config.read("./config/config.conf")   # 配置文件的路径
    return config.get(section, key)



def get_up_postion(positon_number):

    return position