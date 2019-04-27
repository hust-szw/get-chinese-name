# get-chinese-name
自动生成中文名字

这是一个自动生成中文名字的python类，它提供三种获取名字的方法

## 方法：
**get_a_name():** 
返回一个随机的中文名字

**get_name_set(num = 1,repeatable = False)** 
返回一个中文名字列表
有两个可选参数 :
num:列表包含的名字数
repeatable:生成的名字是否允许重复

**get_name_file(num = 1,repeatable = False,fileName = "out.txt",encoding = "utf8"):**
生成一个包含指定个数的中文名的文件
包含四个可选参数：
num:列表包含的名字数
repeatable:生成的名字是否允许重复
filename:输出姓名文件的文件路径
encoding:指定编码格式

## 使用：
### 作为开发：
引入getChineseName 类即可
### 仅用以生成随机姓名集
- 打开cmd 
- 进入 文件夹 cd /../getChineseName
- 输入 python (默认已经安装好python 并且配置好环境变量) 进入交互界面
- import getChineseName 
- name_set = getChineseName
- 接着就可以使用以上三种方法了，例：
- print(name_set.get_a_name())  //打印一个名字
- name.get_name_file(10)  //生成一个包含十个随机名字的文件
