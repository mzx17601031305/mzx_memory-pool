import os
import multiprocessing
import shutil


#建立文件夹并判断是否存在
import time


def mkdir_c(path):
    is_exists = os.path.exists(path)
    #判断结果
    if not is_exists:
        os.mkdir(path)
        print(path + '创建目录成功')
    else:
        print(path + '目录已经存在')

#复制文件
def Copy_File(file_name,s_path,d_path):
    s_file  = os.path.join(s_path,file_name)
    if os.path.isfile(s_file):
        shutil.copy(s_file,d_path)
        print(f'传输{s_file}成功',os.getpid())




if __name__ == '__main__':
    s_path = '/Users/mazixuan/Desktop/mzx_memory-pool/Untitled Folder'
    d_path = '/Users/mazixuan/Desktop/github_image/test'
    mkdir_c(d_path)
    list_file = os.listdir(s_path)
    print(list_file)

    for i in list_file:
        a = os.path.join(s_path,i)
        if not os.path.isfile(i):
             a = multiprocessing.Process(target=Copy_File,args=(i,s_path,d_path))
             a.start()
        else:
            print(f'这个不是文件{a}')