# Created by szw at 2019/4/27
import random
#随机生成中文名
#支持


class getChineseName:
    #初始化
    def __init__(self):
        self.load()

    def __del__(self):
        pass
    #加载数据文件
    def load(self):
        self.familyNameSet = []
        self.givenNameSet = []
        try:
            #load family name data
            with open("data/familyName.txt",'r',encoding="utf8") as f:
                line = f.readline().replace("\n","")
                while(line):
                    self.familyNameSet.append(line)
                    line = f.readline().replace("\n","")
            #load given name data
            with open("data/givenName.txt",'r',encoding="utf8") as f:
                line = f.readline().replace("\n","")
                while(line):
                    self.givenNameSet.append(line)
                    line = f.readline().replace("\n","")
        except FileNotFoundError:
            print("请在getChineseName文件夹下运行")
    #随机获得一个中文名字
    def get_a_name(self):
        familyName = random.choice(self.familyNameSet)
        givenName = random.choice(self.givenNameSet)
        return familyName+givenName

    #获得一个姓名集 参数为姓名数量,指定是否可重复
    def get_name_set(self,num = 1,repeatable = False):
        nameSet = []
        if(num<=0):
            print("请输入大于0的姓名数量!\n")
        while(len(nameSet) < num):
            familyName = random.choice(self.familyNameSet)
            givenName = random.choice(self.givenNameSet)
            if(((familyName+givenName) in nameSet) and repeatable == False):
                continue
            nameSet.append(familyName+givenName)
        return nameSet

    #获得一个包含指定数量中文名字的文件
    def get_name_file(self,num = 1,repeatable = False,fileName = "out.txt",encoding = "utf8"):
        i = 0
        nameSet = []
        try:
            f = open(fileName,'w',encoding=encoding)

        except FileNotFoundError :
                print("请输入正确的文件路径!\n")
        except UnicodeEncodeError:
                print("请指定正确的文件编码!\n")
        except:
            print("文件打开出错!")
        else:

            if (num <= 0):
                print("请输入大于0的姓名数量!\n")
            while (len(nameSet) < num):
                familyName = random.choice(self.familyNameSet)
                givenName = random.choice(self.givenNameSet)
                if (((familyName + givenName) in nameSet) and repeatable == False):
                    continue
                nameSet.append(familyName + givenName)
            while(i < len(nameSet)):
                f.write(nameSet[i]+"\n")
                i += 1
            print("finished!\n")
            f.close()
if __name__ == "__main__":
    name = getChineseName()
