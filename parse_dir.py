import os                                             #导入操作文件夹需要的os模块  
  
def list_dir_recur(root_dir):
    import os              
    list_files=[]                         
    for object_in_dir in os.listdir(root_dir):
        if os.path.isdir(os.path.join(root_dir,object_in_dir)):
            list_recur=list_dir_recur(os.path.join(root_dir,object_in_dir))
            list_files.extend(list_recur)
        else:
            list_files.append(os.path.join(root_dir,object_in_dir))
    return list_files
  

all_list_files=list_dir_recur("dir_test")
for file in all_list_files:
    f=open(file)
    for line in f:
        print(line)
