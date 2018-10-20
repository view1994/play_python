#coding utf-8
import wordcloud
import jieba
def get_txt(src):
    f=open(src,'r',encoding='utf-8')
    txt=f.read()
    f.close()
    words=' '.join(jieba.lcut(txt))
    print(words)
    return words
def make_wordcloud_from(src):
    w=wordcloud.WordCloud(width=600,height=500,background_color='white')
    w.generate(src)
    w.to_file('新时代中国特色社会主义.jpg')
def main():
    src='新时代中国特色社会主义.txt'
    make_wordcloud_from(get_txt(src))
if __name__ == '__main__':
    main()