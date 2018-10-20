import re
import urllib, urllib2
def Gtranslate(text):

    Gtext = text

    values = {'hl': 'zh-CN', 'ie': 'UTF-8', 'text': Gtext, 'langpair': "'en'|'zh-CN'"}

    url = 'http://translate.google.cn/'

    data = urllib.urlencode(values)

    req = urllib2.Request(url, data)

    browser = 'Mozilla/4.0 (Windows; U;MSIE 6.0; Windows NT 6.1; SV1; .NET CLR 2.0.50727)'
    req.add_header('User-Agent', browser)


    response = urllib2.urlopen(req)


    html = response.read()


    p = re.compile(r"(?<=TRANSLATED_TEXT=).*?;")
    m = p.search(html)
    chineseText = m.group(0).strip(';')
    return chineseText


if __name__ == "__main__":

    Gtext = 'you should believe yourself,you are the best one! and we sure that you will do something making us being proud of you'
    print('The input text: %s' % Gtext)
    chineseText = Gtranslate(Gtext).strip("'")
    print('Translated End,The output text: %s' % chineseText)