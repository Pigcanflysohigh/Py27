class Course:
    def __init__(self,cou_name,cou_price,cou_time,cou_teacher):
        self.cou_name = cou_name
        self.cou_price = cou_price
        self.cou_time = cou_time
        self.cou_teacher = cou_teacher

    def func(self):
        '''
        方法样例
        :return:
        '''
        pass

# english = Course('English',10000,6,'Tony')
# print(english.__dict__)