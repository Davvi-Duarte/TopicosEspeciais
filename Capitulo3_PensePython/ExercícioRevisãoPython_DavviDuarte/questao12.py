T=list()
ValP=float(input())

while(ValP!=0):
    D=int(input())
    if(D==0):
        print("Valor total da Prestação: R$ %.2f" %(ValP))
        T.append(ValP)
    else:
        j=ValP+(10*0.3)+((10*0.01)*D)
        print("Valor total da Prestação: R$ %.2f" %(j))
        T.append(j)
    ValP=float(input())


cf=sum(T)

print("Valor total de prestações pagas hoje: R$ %.2f" %(cf))

