def readfile(filename, fn):
    ''' Takes a text file and return frequency histogram
    for worlds 
    filename: file name of the text file
    fn: starting line #
    '''
    
    hist={}
    with open(filename, 'r') as f:
        lines=f.readlines()[fn:]
    for line in lines:
        processline(line,hist)     
    return hist

def processline(line,hist):
    ''' Takes a line and returns histogram of words
    '''

    line=line.replace('-',' ')
    words=list(line.split(" "))
    for w in words:
        w=w.strip().lower()
        w=w.translate(str.maketrans('','',string.punctuation))
        w=w.translate(str.maketrans('','','“”'))
        w=re.sub("’s",'', w)
        w=re.sub("n’t",'', w)
        if w !='':
            hist[w]=hist.get(w,0)+1
       
def summary(hist):
    ''' prints total number of different wordds
    '''
    print("total number of different words is", len(hist))

def frequent(hist,n):
    ''' takes a histogram and returns it in the 
    decreasing order of freq
    n = top n number of items to enter
    returns a list of tuples

    '''
    
    c=[]
    for k,v in hist.items():
        if k !='':
            c.append((v,k))
            c.sort(reverse=True)
    print(c[0:n-1])


def most_frequent(s):
    ''' takes a string and returns the most frequently
    used character
    n = string
    '''
    s=s.lower()
    ch=list(s)
    d={}
    l=[]
    for c in ch:
        if c in "~!@#$%,. ^&*()-_\\/\"\'":
            z=c
        else:
            d[c]=d.get(c,0)+1
    print(d)
    for key,value in d.items():
        l.append((value,key))
        l.sort(reverse=True)
    return(l)

def alphabet(w):
    """
    returns characters of a word in sorted order
    """
    wl=list(w)
    wl.sort()
    return "".join(wl)

def find_anagram(l):
    """
    check for anagrams in the list and return a dict
    """
    d={}
    for w in l:
        walphabet=alphabet(w)
        if walphabet not in d:
            d[walphabet]=[w]
        else:
            d[walphabet].append(w)
    print(d)          
    return d

def print_ana(d):
    """
    print anagrams. 
    characters with the highest number of anagrams prints first
    """
    t=[]
    for v in d.values():
        if len(v)>1:
            t.append((len(v),v))
    t.sort(reverse='True')
    for x in t:
        print(x)

if __name__ == '__main__':
    fin=open('words.txt')
    word=[]
    for line in fin:
        w=line.strip().lower()
        word.append(w)

    wordlist=['IBM','HAL','banana','jj','train','cheer','jolly','jollt','molley','deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    print(alphabet('wetweagaewg'))
    print_ana(find_anagram(word))