A=list()
for i in range(15):
    v=int(input())
    A.append(v)
print("Lista: ", A)
print("Valor Máximo dentro da lista: %d"%(max(A)))
print("Posição do maior valor da lista: ", A.index(max(A)))
