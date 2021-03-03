dow_per = '-1.20'

def check_index(self):
    self = list(self)
    print(self)
    if '-' in self:
        print('no')

check_index(dow_per)