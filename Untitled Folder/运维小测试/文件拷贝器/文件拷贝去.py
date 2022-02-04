import multiprocessing
import os

def copy_word(f_name,s_dir,d_dir):
    s_path = s_dir + '/' + f_name
    d_path = d_dir + '/' + f_name
    print(s_path)
    print(s_path,'>>>',d_path)
    with open(s_path,'rb') as s_file:
        with open(d_path,'wb') as d_file:
            while True:
                file_data = s_file.read(10485760)
                if file_data:
                    d_file.write(file_data)
                else:break


if __name__ == '__main__':
    s_dir = '/Users/mazixuan/Desktop/mzx_memory-pool/Untitled Folder'
    d_dir = '/Users/mazixuan/Desktop/github_image/test'

    try:
        os.mkdir(d_dir)
    except:
        print('目标文件夹已经存在')

    f_name = os.listdir(s_dir)
    for i in f_name:
        # copy_word(i,s_dir,d_dir)
        copy_conn = multiprocessing.Process(target = copy_word,
                                args = (i,s_dir,d_dir))
        copy_conn.start()