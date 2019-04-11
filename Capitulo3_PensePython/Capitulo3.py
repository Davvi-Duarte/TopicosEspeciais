#Atividade do Livro "Pense em Python"- Aluno: Davvi Duarte Rodrigues-Info4

#Cap.3: Funções

#3.1: Chamada de função

'''
type(59)
int('65')
int('Hello')
int(7.88888)
int(-5.6)
float(36)
float('3.14159')
str(99)
str(3.14159)
''''

#3.2: Funções matemáticas

'''
import math
ratio = signal_power/noise_power
decibels = 20 * math.log10(ratio)
radians = 0.8
height = math.sin(radians)
'''

'''
degrees = 75
radians = degrees / 150.0 * math.pi
math.sin(radians)
'''

'''
math.sqrt(2)/4
'''

#3.3:Composição

'''
minutos = horas * 60 #ta certo
horas * 60 = minutos #ta errado
'''

#3.4: Como acrescentar novas funções

'''
def print_refrao():
    print("O Nome dela eh Jennifer, eu encontrei ela no Tinder.")
    print("Não eh minha namorada, mas poderia ser. ")
'''

'''
print(print_refrao)
type(print_refrao)
'''

'''
print_refrao()
'''

'''
def repete_refrao():
    print_refrao()
    print_refrao()
'''

'''
repete_refrao()
'''

#3.5: Uso e definições

'''
def print_refrao():
    print("O Nome dela eh Jennifer, eu encontrei ela no Tinder.")
    print("Não eh minha namorada, mas poderia ser. ")

def repete_refrao():
    print_refrao()
    print_refrao()

repete_refrao()
'''

#3.7: Parâmetros e argumentos

'''
def print_duplo(opa):
    print(opa)
    print(opa)
'''

'''
print_duplo('Rhavy')
print_duplo(30)
print_duplo(math.pi)
'''

'''
print_duplo('Rhavy'*5)
print_duplo(math.cos(math.pi))
'''

'''
Jennifer='Encontrei ela no Tinder'
print_duplo(Jennifer)
'''

#3.8: As variáveis e os parâmetros são locais

'''
def cat_duplo(p1, p2):
    cat=p1+2
    print_duplo(cat)
'''

'''
linha1 = 'Casa suja'
linha2 = 'Chao sujo'

cat_duplo(linha1, linha2)
'''

'''
print(cat)
'''

#3.10: Funções com resultado e funções nulas

'''
x=math.cos(radianos)
a=(math.sqrt(10) + 2) / 4
'''

'''
math.sqrt(10)
'''

'''
resultado=print_duplo('Pey')
print(resultado)
'''

'''
print(type(None))
'''

#Fim dos exemplos


