#coding:utf-8
#
import os
def split_file():
    i=0
    names = {}
    filepath = input('输入路径: ')
    #filepath = '/Users/tanyashi/Desktop/2830e_print/450M/disk_dbg450M.txt'
    if not os.path.exists(filepath):
        print(filepath,'not exist!')
    else:
        #sep_words = input('分割字符：')
        sep_words = '*************Start NewChannel****************'
        new_file_path = filepath.rsplit('/', 1)[0]
        g = open(new_file_path+'/start_of_'+filepath.rsplit('/', 1)[-1], 'a')
        with open(filepath, 'r',encoding='utf-8') as f:
            line = f.readline()
            i+=1
            while line:
                if (sep_words in line):
                    start_line=f.readline()
                    new_file_name = 'v_pid=' + start_line.split(':')[-1].split()[0]
                    new_file = new_file_path + '/' + new_file_name
                    if os.path.exists(new_file+'.txt'):
                        if new_file in names.keys():
                            names[new_file]+=1
                        else:
                            names[new_file]=1
                        #print(names[new_file],type(names[new_file]))
                        new_file = new_file + '_' + str(names[new_file]) + '.txt'
                    else:
                        new_file = new_file + '.txt'
                    g.close()
                    g = open(new_file, 'a')
                    g.write(line )
                    g.write(start_line)
                else:
                    g.write(line )
                i+=1
                try:
                    line = f.readline()
                except:
                    print(g.name,i)
            else:
                g.close()
        print('end')


def main():
    split_file()


if __name__ == '__main__':
    main()