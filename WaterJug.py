5def gcd(n,m):
    if m==0:
        return n
    return gcd(m,n%m)

def pour(to,from1,d):
    if to>from1:
        print("The water is flowing from big jar to small jar")
    else:
        print("The water is flowing from small jar to big jar")
    print("The water exchange combinations are: ")
    fromjug=0
    tojug=0
    step=0
    print("(",tojug,",",fromjug,")")
    while ((fromjug is not d) and (tojug is not d)):
        if fromjug==0:
            fromjug=from1
            step=step+1
            print("(",tojug,",",fromjug,")")
        if tojug==to:
            tojug=0
            step=step+1
            print("(",tojug,",",fromjug,")")
        temp=min(fromjug,to-tojug)
        fromjug=fromjug-temp
        tojug=tojug+temp
        step=step+1
        print("(",tojug,",",fromjug,")")
    
    return step


def minsteps(n,m,d):
    if m>n:
        temp=m
        m=n
        n=temp
        
    if (d%(gcd(n,m))!=0) or d>n:
        
        return -1
   
    return min(pour(n,m,d),pour(m,n,d))

def main():
    n=int(input("Enter the quantity in first jug: "))
    m=int(input("Enter the quantity in second jug: "))
    d=int(input("Enter the quantity you needed: "))
    c=minsteps(n,m,d)
    if c==-1:
        print("It is not possible to get the required litres in either of the two jugs")
    else:
        print("The minimum number of steps required are to get the quantity ",d," is ",c)
main()
