from random import randint
class Die():
    def __init__(self,face_number=6):
        self.face_number = face_number
    def roll(self):
        '''返回一个1-6的随机数'''
        return randint(1,self.face_number)