lass={'江政浩':1,'张浩文':2,'肖焱隆':3,'黄安':4,'左剑元':5,'肖翔':6} #311宿舍名单
class2={'吴亚林':1,'邱晓慧':2} #520宿舍名单

n=input('宿舍号')
n=int(n)

if n==311:
    n=lass
    name=input('人名')
    print(n[name])
elif n==520:
    n=class2
    name=input('人名')
    print(n[name])
else:
    for j,s in class2:
        print(j,s)

