class Work(object):

    # def __init__(self,company,position,time):
    #     self.company = company
    #     self.position = position
    #     self.time = time
    def __init__(self,time,company,position):
        self.company = company
        self.position = position
        self.time = time

    def print_work(self):
        print("time:"+self.time+" company:"+self.company+" position:"+self.position)






