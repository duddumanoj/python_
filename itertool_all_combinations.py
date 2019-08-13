import itertools
# method to compute gcd ( recursion ) 
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
jk=int(input())
gh=0
while(gh<jk):
    n=int(input())
    r=[]
    r.extend(list(map(int,input().rstrip().split())))
    pu=r
    j=1
    count=0
    while(j<=n/2):
        c=itertools.combinations(r,j)#iter  possible combinations
        for i in list(c):
            
            l=[ele for ele in r if ele not in i] 
            #print(l)
            l=tuple(l)
            s=1
            k=0
            while(k<len(i)):
                s=s*i[k]
                k=k+1
            s1=1
            k1=0
            while(k1<len(l)):
                s1=s1*l[k1]
                k1=k1+1
            #print(s1,s)    
            y=gcd(s1,s)
            if(y==1):
                count=count+1
            if(len(l)!=len(i)):
                y=gcd(s,s1)
                if(y==1):
                    count=count+1
            r=pu
        j=j+1
    print(count)   
    gh=gh+1         
           
                
            
            
           
