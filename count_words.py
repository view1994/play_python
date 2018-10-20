#coding utf-8
import jieba
def get_txt_from(src):
    txt=open(src,'r').read()
    txt=txt.lower()
    for i in '`~!@#$%^&*()_+-=[]\\|;":,./<>?\'':
        if i in txt:
            txt=txt.replace(i,' ')
    return txt
def count_words_in(src):
    words=src.split()
    count={}
    for word in words:
        count[word]=count.get(word,0)+1
    items=list(count.items())
    items.sort(key=lambda x:x[1],reverse=True)
    return items
def count_chinese_words_in(src):
    txt=open(src,'r',encoding='utf-8').read()
    for i in '`~!@#$%^&*()_+-={}[]|\\:";\'<>?,./，。、《》？：！；\n':
        txt=txt.replace(i,' ')
    words=jieba.lcut(txt)
    count={}
    for word in words:
        if len(word)==1:
            continue
        elif word in ['丞相','孟德']:
            reword='曹操'
        elif word in ['孔明','孔明曰']:
            reword='诸葛亮'
        elif word in ['刘备','玄德','玄德曰']:
            reword='刘备'
        elif word in ['关公','云长','关羽']:
            reword='关羽'
        else:
            reword=word
        count[reword]=count.get(reword,0)+1
    exclude_words=['将军','却说','二人','不可','不能','如此','荆州','商议']
    for i in exclude_words:
        del count[i]
    items=list(count.items())
    items.sort(key=lambda x:x[1],reverse=True)
    return items
def main():
    src='hamlet.txt'
    words_count=count_words_in(get_txt_from(src))
    #for i in range(100):
    #    print(words_count[i])
    for i in count_chinese_words_in('threekingdoms.txt'):
        print(i)
if __name__ == '__main__':
    main()