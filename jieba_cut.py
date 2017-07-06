#encoding=utf-8
import jieba
file=open("demo.txt")
word_list=[]
for line in file:
    seg_list=jieba.cut(line)
    word_list.extend(seg_list)
print ", ".join(word_list)