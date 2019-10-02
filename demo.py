# _*_ encoding:utf-8 _*_
__author__ = 'JQXX'
__date__ = '2018/12/7 1:06'
f_j=open("jieba_dict.txt","r",encoding="utf-8") # jieba的默认词典
f=open("all_new_word.txt","r",encoding="utf-8") # all_new_word.txt为互信息与左右信息熵发现的新词
f_s=open("stopword.txt","r",encoding="utf-8") # 中文停用词文件
#f_w=open("jieba_word.txt","w",encoding="utf-8")
jieba_dict={}

for i in f_j:
    i=i.strip().split()
    # if i[0] in jieba_dict:
    #     print(i[0],"----------",i[1])
    #f_w.write(i[0]+"\n")
    jieba_dict[i[0]]=i[2]
for s in f_s:
    if s.strip():
        jieba_dict[s.strip()]="stop"
# for k in jieba_dict:
#     if jieba_dict[k]=="stop":
#         print(k)

result_dict={}

for line in f:
    i = line.strip().split(",")[0].split("_")
    if len(i)<2:
        continue
    key=""
    if i[0] in jieba_dict:
        key += jieba_dict[i[0]]
    else:
        key += "x"
    key+="_"
    if i[1] in jieba_dict:
        key += jieba_dict[i[1]]
    else:
        key += "x"
    result_dict.setdefault(key,[])
    result_dict[key].append(line)
f.close()
f_j.close()
for k in result_dict:
    f_w=open("result/"+k+".txt","w",encoding='utf-8')
    for i in result_dict[k]:
        f_w.write(i)
    f_w.close()