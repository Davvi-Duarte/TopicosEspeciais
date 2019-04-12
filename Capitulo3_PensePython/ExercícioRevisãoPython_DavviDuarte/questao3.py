N=int(input("Numero de casos de teste:"))
for i in range(N):
    v1 = float(input("Valor 1:"))
    v2 = float(input("Valor 2:"))
    v3 = float(input("Valor 3:"))
    print("Média Ponderada:%.1f" %(((v1*2)+(v2*3)+(v3*5)/10)))
