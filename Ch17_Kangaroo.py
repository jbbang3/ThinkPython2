import math

class Kangaroo:
    """Represent the time of day
    Attributes: hour, minute, second"""

    def __init__(self, name, content=None):
        self.name = name
        if content==None:
            content=[]
        self.pouch_content = content

    def __str__(self):
        s=[]
        for x in self.pouch_content:
            if isinstance(x, Kangaroo):
                s.append(x.name)
            else:
                s.append(str(x))
        return ', '.join(ss for ss in s)

    def put_in_pouch(self,sth):
        self.pouch_content.append(sth)

def main():
    k=Kangaroo('koo')
    k.put_in_pouch('xxx')
    k.put_in_pouch('xxdx')
    

    roo=Kangaroo('roo')
    k.put_in_pouch(roo)
    
    #print(k)
    print(roo)
    print(vars(roo))

if __name__=="__main__":
    main()