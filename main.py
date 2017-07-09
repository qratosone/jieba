def get_frequency(filename):
    import jieba
    file=open(filename)
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
    file.close()
    return word_dict_list

def get_word_list(filename):
    import jieba
    file=open(filename)
    word_list=[]
    for line in file:
        seg_list=jieba.cut(line)
        word_list.extend(seg_list)
    file.close()
    return word_list

def get_posseg_list(filename):
    import jieba.posseg as pseg
    file=open(filename)
    word_pseg_dict={}
    for line in file:
        words=pseg.cut(line)
        for word,flag in words:
            if word not in word_pseg_dict:
                word_pseg_dict[word]=flag
    file.close()
    return list(word_pseg_dict)

def list_dir_recur(root_dir):
    import os              
    list_all=[]                         
    for object_in_dir in os.listdir(root_dir):
        if os.path.isdir(os.path.join(root_dir,object_in_dir)):
            list_recur=list_dir_recur(os.path.join(root_dir,object_in_dir))
            list_all.extend(list_recur)
        else:
            print(os.path.join(root_dir,object_in_dir))                 
            fr=open(os.path.join(root_dir,object_in_dir),'r')
            for line in fr:
                line_add = line.strip().replace('\n', '').replace('\r', '').strip()
                list_all.append(line_add)
    return list_all

def write_list(file_output,list_to_write):
    f=open(file_output,"w+")
    for i in list_to_write:
        f.write(str(i))
        f.write('\n')
    f.close()


def operate(frequency,list_f,posseg,file):
    list_out=[]
    if frequency:
        print("flag frequency")
        list_f=get_frequency(file)
        list_out.extend(list_f)
    if list_f:
        print("flag list")
        list_l=get_word_list(file)
        list_out.extend(list_l)
    if posseg:
        print("flag posseg")
        list_p=get_posseg_list(file)
        list_out.extend(list_p)
    return list_out


import argparse
parser = argparse.ArgumentParser()
# arguments for I/O
parser.add_argument("filename", help="read the input file")
parser.add_argument("-r",help="read a directory",action="store_true")
parser.add_argument("-o","--output",help="write the output file")

# agruments for functions
parser.add_argument("-f","--frequency",help="count word frequency",action="store_true")
parser.add_argument("-l","--list",help="get the list of words",action="store_true")
parser.add_argument("-p","--posseg",help="get the posseg of words",action="store_true")
args = parser.parse_args()
flag_recur=args.r
filename_input=args.filename
filename_output=args.output

flag_f=args.frequency
flag_l=args.list
flag_p=args.posseg


list_total=[]
if filename_input:
    if not flag_recur:
        print("file input:",filename_input)
        list_total=operate(flag_f,flag_l,flag_p,filename_input)
    else:
        print("directory input:",filename_input)
        file_list=list_dir_recur(filename_input)
if filename_output:
    print("file output:",filename_output)
    write_list(filename_output,list_total)
