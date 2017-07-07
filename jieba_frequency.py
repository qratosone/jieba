import jieba
file=open("demo.txt")
word_list=[]
for line in file:
    seg_list=jieba.cut(line)
    word_list.extend(seg_list)

word_dict={}
for item in word_list:
    if item not in word_dict:
        word_dict[item]=1
    else:
        word_dict[item]+=1
word_dict_list=sorted(word_dict.items(),key=lambda item: item[1],reverse=True)
for key in word_dict_list:
    print (key[0],key[1])