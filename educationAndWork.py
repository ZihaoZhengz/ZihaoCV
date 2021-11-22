"""
Name: Zihao Zheng
ID: zihaozhe 
Course number and section: 12780 A2
Homework number: 3
"""
class education():
    university=[];
    universityPeriod=[]

    def __init__(self,university,universityPeriod):
       self.university=university;
       self.universityPeriod=universityPeriod
    def showInfo(self):
        res=[]
        ans=[]
        for i in range(len(self.university)):
            res.append(self.university[i]);
            ans.append(self.universityPeriod[i])
        return res,ans;
class work():
    company=""
    timePeriod=""
    job=""
    def __init__(self,company,job,timePeriod):
        self.company=company;
        self.job=job;
        self.timePeriod=timePeriod;
    def showInfo(self):
        return [self.company,self.job,self.timePeriod]