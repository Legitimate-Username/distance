def diff(x,y):
    if x==y: 
        return 0
    else: 
        return 1

def distance(x, y):
    m=len(x)
    n=len(y)
    E=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, m+1):
        E[i][0]=i
    for j in range(1, n+1):
        E[0][j]=j
    string1=""
    string2=""
    for i in range(1, m+1):
        for j in range(1,n+1):
            insertion=E[i-1][j]+1
            deletion=E[i][j-1]+1
            substitute=E[i-1][j-1]+diff(x[i-1],y[j-1])
            E[i][j]=min(insertion, deletion, substitute)
    a=m
    b=n
    while(a>0 and b>0):
        horizontal=E[a][b-1]
        vertical=E[a-1][b]
        diagonal=E[a-1][b-1]
        minimum=min(horizontal, vertical, diagonal)
        if (minimum == diagonal):
            string1+=x[a-1]
            string2+=y[b-1]
            a-=1
            b-=1        
        elif(minimum==vertical):
            string1+=x[a-1]
            string2+="-"
            a-=1
        elif(minimum==horizontal):
            string1+="-"
            string2+=y[b-1]
            b-=1
        if(b==0):
            while(a>0):
                string1+=x[a-1]
                string2+="-"
                a-=1
        if(a==0):
            while(b>0):
                string1+=y[b-1]
                string2+="-"
                b-=1
    print "edit distance = "+str(E[m][n])
    print "alignment:"
    print string1[::-1]
    print string2[::-1]
    return E

x=raw_input('X ==> ')
y=raw_input('Y ==> ')
distance(x, y)