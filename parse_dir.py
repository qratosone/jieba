import os                                             #导入操作文件夹需要的os模块  
  
def list_dir_recur(root_dir):             #定义函数，参数为要操作的根文件夹，和最后要输出的新文件  
    list_all=[]                         #以写方式打开文件  
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
  

print(os.listdir("dir_test"))

all_list=list_dir_recur("dir_test")
for line in all_list:
    print(line)
