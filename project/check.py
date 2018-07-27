#author = yhy
import random

def get_list_id(len):
    id_list = []
    i = 0
    while (i < 100):
        id = random.randint(1,len)
        id_list.append(id)
        i += 1
    return id_list