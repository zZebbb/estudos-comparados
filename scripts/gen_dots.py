import json,math,sys
g=json.load(open('data/globo.json'))
def rings_of(lst): return [[(r[i],r[i+1]) for i in range(0,len(r),2)] for r in lst]
def bb(r): xs=[p[0] for p in r]; ys=[p[1] for p in r]; return min(xs),max(xs),min(ys),max(ys)
W=[(r,bb(r)) for r in rings_of(g['world'])]
ST={k:[(r,bb(r)) for r in rings_of(v)] for k,v in g['study'].items()}
def pip(r,lon,lat):
    c=False;n=len(r);j=n-1
    for i in range(n):
        xi,yi=r[i];xj,yj=r[j]
        if (yi>lat)!=(yj>lat) and lon<(xj-xi)*(lat-yi)/(yj-yi+1e-12)+xi: c=not c
        j=i
    return c
def inset(rs,lon,lat):
    c=False
    for r,(a,b,cc,d) in rs:
        if a<=lon<=b and cc<=lat<=d and pip(r,lon,lat): c=not c
    return c
slugs=list(ST)
def gen(S,flags):
    pts=[];lat=-58.0
    while lat<=82:
        n=max(1,round(360*math.cos(math.radians(lat))/S));d=360/n
        for i in range(n):
            lon=-180+i*d+d/2;f=0
            for k,rs in ST.items():
                if inset(rs,lon,lat): f=slugs.index(k)+1;break
            if f or inset(W,lon,lat): pts+=[round(lat,2),round(lon,2)]+([f] if flags else [])
        lat=round(lat+S,2)
    return pts
p=gen(1.2,True);json.dump({"slugs":slugs,"step":1.2,"p":p},open('data/dots.json','w'),separators=(',',':'))
import collections;print(len(p)//3,collections.Counter(p[2::3]))
q=gen(3,False);json.dump(q,open('land-dots-3graus.json','w'),separators=(',',':'));print(len(q)//2)
