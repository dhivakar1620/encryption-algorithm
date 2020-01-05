import math as ma
from operator import itemgetter
cut=[]
od=[]
mkey=[]
def bitc(s=''):
    bp=[]
    bb=[bin(ord(x))[2:].zfill(8) for x in s]
    for x in bb:
         bp.append(x)
    bp="".join(bp)
    l=len(bp)
    l=l/64
    l=ma.ceil(l)
    bp=bp.zfill(l*64) 
    return bp,l
def odr(bp):
    out=[]
    g=1
    z=0
    y=8
    for i in range (8):
        now=bp[z:y]
        lc,rc=half(now,4)##ad
        z+=8
        y+=8
        for j in now :
            g+=int(j)
            g=4-g
        ing=(int(rc)*g*int(lc))#to brake asc ord
        rnd=(ing%16)+1
        #print(now,ing,g,"round:", rnd)
        temp=[]
        temp=[now,ing,rnd,i]
        out.append(temp)
    print(out) 
    out.sort(key=lambda x: x[1])
    l=len(out)
    return out,l

def splt(bit):
    out=[]
    le=len(bit)
    z=0
    y=8
    for i in range (int(le/8)):
        now=bit[z:y]
        z+=8
        y+=8
        out.append(now)
    return(out)

def half(bits,s):
    lb, rb= bits[:s],bits[s:]
    return lb,rb

def appc(order,bits):
 obits = ""
 for i in order:
  obits += bits[i-1] 
 return obits



inp="computer"
ke ="october"
pt,pl=bitc(inp)
print(pt,pl)
ky,l=bitc(ke)
xx=ky
print(ky,l)
ky,l=odr(ky)
print(ky,l)
for i in range(l):
    mkey.append(ky[i][0])
    temp=(ky[i][3])
    od.append((temp+1))
mkey=''.join(mkey)
l=len(mkey)
print(mkey,l)

print(ke)
print(xx)
print(od)
z=0
y=64
for i in range (pl):
    now=pt[z:y]
    z+=64
    y+=64
    ptt=splt(now)
    print(ptt)
    ptt=appc(od,ptt)
    
ptt=splt(ptt)
print(ptt)
print(pt)
