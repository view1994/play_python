#coding utf-8
import  copy,time
'''
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。

匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
'''

def SwitchPattern(p):
    pattern = list(p)
    temp = []
    while pattern:
        pp = pattern.pop()
        if pp == '*':
            z = pattern.pop()
            if z == '.':
                temp.insert(0, '^')
            else:
                temp.insert(0, z.upper())
        else:
            temp.insert(0, pp)
    return temp

def isUpWord(w):
    if not w :
        return False
    elif (ord(w) >= ord('A')) & ( ord(w ) <= ord( 'Z' )):
        return True
    elif w=='^':
        return True
    else:
        return False

##solution1
def ForwardMatch1( s , p ):
    P=p.split('*')
    s=list(s)
    d=[]
    print(P,s,d)
    for j in P[:-1]:
        print('sub_p={},s={}'.format(j, s,d))
        for i in j[:-1]:
            if i=='.':
                d.append(s.pop(0))
            elif i!=s[0]:
                return False
            else:
                d.append(s.pop(0))
        saved=j[-1]
        print('saved={},s={}'.format(saved, s ,d ))
        if s:
            while (s[0]==saved)|(saved=='.'):
                d.append(s.pop(0))
                if len(s)==0:
                    break
        print('saved={},s={}\n'.format(saved, s , s))
    print('\nsub_p={},s={}'.format(P[-1], s ,s))
    for i in P[-1]:
        if s=='':
            return False
        if i == '.':
            d.append(s.pop(0))
        elif s:
            if i != s[0] :
                return False
            else:
                d.append(s.pop(0))
        else:
            return False
    print('s={}'.format(s, s))
    if len(s)!=0:
        return False
    else:
        return True

##solution2
def BackwardMatch(s, p):
    pattern = list( p )
    txst = list( s )
    d = []
    if (pattern==[]) :
        return True if  txst == [] else False
    else:
        pp = pattern.pop()
    if (txst==[]) :
        if (pp != '*' ):
            return False
        else:
            while pp == '*':
                d.append(pattern.pop())
                if pattern == []:
                    return True
                pp = pattern.pop()
            else:
                return False
    while (txst):
        i=txst.pop()
        if pattern == [] :
            if i in d:
                d = d[d.index(i):]
            elif '.' in d:
                d = d[d.index('.'):]
        while pp == '*':
            d.append( pattern.pop() )
            if pattern==[]:
                pp=[]
                break
            pp =pattern.pop()
        #print('i={},\td={},\tpp={},\ttxst={},\tpattern={}'.format(i, d, pp, txst, pattern))
        if i == pp:
            if i in d:
                d = d[ d.index( i ) : ]
            else:
                d = []
            pp= [] if pattern == [] else pattern.pop()
        elif i in d:
            ind = d.index( i )
            d = d[ ind : ]
        elif pp == '.':
            d = []
            pp = [] if pattern == [] else pattern.pop()
        elif '.' in d:
            ind = d.index('.')
            d = d[ind:]
        else:
            return False
    else:
        while pp == '*':
            d.append( pattern.pop() )
            if pattern==[]:
                pp=[]
                break
            pp =pattern.pop()
        if (pp ==[] ) & (pattern == []):
            return True
        return  False

##solution3
def ForwardMatch(s, p):
    txst = list(s)
    pattern = SwitchPattern(p)
    print('pattern = {},\ttxst = {}'.format(pattern,txst))
    d = []
    if ( pattern==[] ) & ( txst==[]):
        return True
    elif( pattern==[] ) & ( txst!=[]):
        return False
    else:
        pp = pattern.pop(0)
    while txst:
        w = txst.pop(0)

        while isUpWord(pp ):
            d.append(pp.lower())
            pp = [] if pattern == [] else pattern.pop(0)
        print('w={}\tpp={}\td={}\ttxst={}\tpattern={}'.format(w, pp, d, txst, pattern))
        if  w == pp:
            if w in d :
                d = d[d.index(w):]
            else:
                d=[]
                pp = [] if pattern==[] else pattern.pop(0)
        elif '^' in d:
            d = d[d.index('^'):]
        elif w in d:
            d = d[d.index(w):]
        elif pp == '.':
            pp = [] if pattern == [] else pattern.pop(0)

        else:
            return False
    else:               #txst==[]       pp有值    pp = pattern.pop(0)
        #print('w={}\tpp={}\td={}\ttxst={}\tpattern={}'.format(w, pp, d, txst, pattern))
        if ( pp !=[] ) & ( not isUpWord(pp)) :
            return False
        while pattern:
            if not isUpWord(pattern.pop(0)):
                return False
        else :
            return True

##solution4
def isMatch4( s , p ):
    print('s={},\tp={}'.format( s , p ) )
    return True if BackwardMatch( s , p ) else ForwardMatch( s , p )

##solution5
def Match1word(sentence,pattern):        #backword match
    print( 'START-->{: <60}\t{}'.format(str(sentence),str(pattern )))
    i=0
    if ( pattern==[] ) & ( sentence==[]):
        print('return True ---pattern , sentence all empty!')
        return True
    elif( pattern==[] ) & ( sentence!=[]):
        print('return False --- pattern empty , but sentence not empty')
        return False
    else:       #pattern not empty
        d = []
        while pattern:
            pp = pattern.pop()
            if isUpWord( pp ):
                d.append( pp )
            else:
                p = pp
                break
        else:       #patter dose not have any low word
            p = []
    if not sentence :  #sentence empty
        if ( p !=[] )  :
            print('False--sentence empty, and p != []')
            return False
            '''
            while pattern:
                if not isUpWord(pattern.pop()):
                    print('False--sentence empty, and pattern has low word')
                    return False
            '''
        else :
            print('return True--sentence empty,and pattern  all up word')
            return True

    else:   #sentence is not empty
        word = sentence.pop()
        #print('sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern, word, p, d))
        d_saved= copy.deepcopy(d)
        pattern_saved = copy.deepcopy(pattern)
        sentence_saved = copy.deepcopy(sentence)
        if ( word == p) :
            #print('SAVED ==[p=word]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern, word,p, d))
            if Match1word( sentence, pattern ):
                print('word == p:return True')
                return True
            else:
                d = d_saved
                pattern = pattern_saved
                sentence = sentence_saved
        if p == '.':
            print('SAVED ==[p="."]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern, word,p, d))
            if Match1word(sentence, pattern):
                print('p == . :return True')
                return True
            else:
                d = d_saved
                pattern = pattern_saved
                sentence = sentence_saved
            #print('SAVED ==[p="."]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern, word, p, d))
        if word.upper() in d :
            print('SAVED ==[word.upper() in d]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence,pattern, word, p, d))
            d = d [ d.index( word.upper()) : ]
            if  p:
                pattern.append(p)
            while d :
                pattern.append( d. pop() )
            if Match1word(sentence, pattern) :
                print('word.upper() in d :return True')
                return True
            else:
                d = d_saved
                pattern = pattern_saved
                sentence = sentence_saved
            #print('SAVED ==[word.upper() in d]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence,pattern,word, p, d))

        if '^' in d:
            print('1SAVED ==["^" in d ]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern,word, p, d))
            d = d[d.index('^'):]
            if  p:
                pattern.append(p)
            while d:
                pattern.append(d.pop())
            #print('2SAVED ==["^" in d ]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern,word, p, d))
            if  Match1word(sentence, pattern):
                print('^ in d :return True')
                return True
            else:
                #print('3SAVED ==["^" in d ]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern,word, p, d))
                return False
        else:
            print('else false')
            return False



def isMatch(s,p):
    '''
    :param s:str        #待匹配字符串
    :param p:str        #匹配模式
    :return:bool        #返回值
    note：
    '.' 匹配任意单个字符。
    '*' 匹配零个或多个前面的元素。
    '''
    sentence = list(s)
    pattern = SwitchPattern(p)
    #print('sentence = {},\tpattern = {},\t'.format( sentence , pattern ) )
    return  Match1word( sentence, pattern )


def main():
    s = "tccaaaaabsqa"
    p = "tc*a*bs.a"

    s,p="aaa","ab*a*c*a"
    #s ,p = "missassppi", "mis*as*p*."

    #s , p = "aab","a.*"
    #s,p="a",".*..a*"        #False
    s , p = "abbabaaaaaaacaaa" , "a*.*b.a.*c*b*a*c*a"
    #s , p = "bcaccbbacbcbcab" , "b*.c*..*.b*b*.*c*"
    #s ,p = 'abcdef' , 'abCEd.f'
    s,p='aa','a*'
    s ,p = "baabbbaccbccacacc","c*..b*a*a.*a..*c"
    s,p="ccabbaacbcbbabaa","bba*ba*.*.a*.*b*a*a"            #440
    s,p='zxbbbaa','bba*ba*.*.a*.*b*a*a'
    #print(ForwardMatch(s, p))
    t= time.time()
    print( isMatch( s , p ) )
    print('time:',time.time()-t)

if __name__ == '__main__':
    main()