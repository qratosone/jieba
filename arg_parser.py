def open_file(filename):
    file=open(filename)
    return file

def get_frequency(file):
    import jieba
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
    return word_dict_list




import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="read the input file")
parser.add_argument("-r",help="read a directory",action="store_true")
parser.add_argument("-o","--output",help="write the output file")
args = parser.parse_args()
flag_recur=args.r
filename_input=args.filename
filename_output=args.output
if filename_input:
    if not flag_recur:
        print("file input:",filename_input)
        file_open=open_file(filename_input)
        for line in file_open:
            print(line) # do something to the file
    else:
        print("directory input:",filename_input)
if filename_output:
    print("file output:",filename_output)