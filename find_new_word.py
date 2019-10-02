import jieba
from model import TrieNode
from utils import  load_dictionary, generate_ngram, save_model, load_model,cut_sent
import re
from multiprocessing import Manager
from config import FLAGS
import multiprocessing
import numpy as np
import pickle
import os
l_zre=[i.strip() for i in open(FLAGS.data_path+"z_relu_no_pro.txt")]
f_j=open(FLAGS.data_path+"dict.txt","r",encoding="utf-8")
jieba_dict={}
result_set=set()
zhuang_set=set()
fei_set=set()

for i in f_j:
    i=i.strip().split()
    jieba_dict[i[0]]=i[2]

jieba.load_userdict(FLAGS.data_path+"my_dict.txt")
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"

stop_word=[i.strip() for i in open(FLAGS.data_path+"stopword.txt","r",encoding="utf-8")]


for s in stop_word:
    jieba_dict[s.strip()]="stop"

read_file = open(FLAGS.data_path + "char_to_id.txt", "r", encoding='utf-8')
char_to_id = {}
for i in read_file:
    i = i.strip().split()
    if len(i) != 2:
        continue
    char_to_id[i[0]] = int(i[1])
files = os.listdir(FLAGS.data_path + "mulu/")
root_name = FLAGS.data_path + "root.pkl"

def get_fen_result(zz):
    all_sen=[]
    data=[]
    sentences = cut_sent(zz)
    for sent in sentences:
        sent = sent.replace("\n", "")
        sent = sent.replace("\t", "")
        sent = sent.replace(" ", "")
        if sent:
            all_sen.append(sent)

    for line in all_sen:
        word_list = [x for x in jieba.cut(line.strip())]
        data.append(word_list)
    if os.path.exists(root_name):
        root = load_model(root_name)
    else:
        dict_name = FLAGS.data_path + 'dict.txt'
        word_freq = load_dictionary(dict_name)
        root = TrieNode('*', word_freq)
        save_model(root, root_name)
    for word_list in data:
        ngrams = generate_ngram(word_list, FLAGS.ngram)
        for d in ngrams:
            root.add(d)
    te_re, add_word = root.find_word(FLAGS.topN, stop_word, jieba_dict, l_zre)
    del  root
    return te_re



for path in files:
    target = open(FLAGS.result_path+path,"w",encoding="utf-8")
    all_sen = []
    data = []
    f = open(FLAGS.data_path + "mulu/" + path, "r", encoding='utf-8')
    all_txt=f.read()
    zz = re.sub('\$\d\$', '', all_txt)
    temp=""
    res=get_fen_result(zz)
    for dui in res:
        target.write(dui[0]+"\n")
    target.close()
