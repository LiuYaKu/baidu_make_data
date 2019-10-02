# _*_ encoding:utf-8 _*_
__author__ = 'JQXX'
__date__ = '2018/12/21 0:29'
import os
ff=os.listdir("./result/")


f = open("relu_no_pro.txt") # 词性对规则文件
f_w = open("relu_no_proword.txt", "w", encoding='utf-8') # 规则抽出来的非领域词
f_test = open("relu_wait_proword.txt", "w", encoding='utf-8') # 剩余的待分类新词
my_rule = [i for i in ff if "uj" in i or "stop" in i]

f_l=[]
for i in f:
    f_l.append(i.strip()+".txt")
    i="./result/"+i.strip()+".txt"
    try:
        t=open(i,"r",encoding="utf-8")
    except:
        continue
    for j in t:
        if j.strip():
            f_w.write(j.strip().split(",")[0].replace("_","")+"\n")
    t.close()
for i in my_rule:
    i = "./result/" + i
    try:
        t=open(i,"r",encoding="utf-8")
    except:
        continue
    for j in t:
        if j.strip():
            f_w.write(j.strip().split(",")[0].replace("_","")+"\n")
    t.close()

for j in ff:
    if j not in f_l:
        t = open("./result/"+j, "r", encoding="utf-8")
        for jj in t:
            if len(jj.strip().split(",")[0].replace("_",""))<3:
                f_w.write(jj.strip().split(",")[0].replace("_", "") + "\n")
                continue
            if jj.strip().split(",")[0].split("_")[0]==jj.strip().split(",")[0].split("_")[1]:
                f_w.write(jj.strip().split(",")[0].replace("_","")+"\n")
            elif jj.strip():
                f_test.write(jj.strip().split(",")[0].replace("_","")+"\n")
        t.close()

f_test.close()
f_w.close()
f.close()