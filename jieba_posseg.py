#encoding=utf-8
import jieba.posseg as pseg
file=open("demo.txt")
word_pseg_dict={}
for line in file:
    words=pseg.cut(line)
    for word,flag in words:
        if word not in word_pseg_dict:
            word_pseg_dict[word]=flag
for key in word_pseg_dict:
    print(key,word_pseg_dict[key])