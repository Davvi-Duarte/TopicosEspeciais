A=list()

for i in range(6):
    v=float(input())
    if (v >=1):
        A.append(v)

soma=sum(A)

print("Média dos valores Positivos: %.1f" %(soma/len(A) ))
