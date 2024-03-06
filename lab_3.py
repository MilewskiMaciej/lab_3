import random
#Zadanie 1
"""
def zad1():
    a = [i for i in range(1,11)]
    b = [4**j for j in range(0,8)]
    c = [k for k in b if k%2==0]
    print(a)
    print(b)
    print(c)
    
#Zadanie 2
def zad2():
    lista1 = [random.randint(1, 15) for i in range(10)]
    print(lista1)
    nowa_lista = [j for j in lista1 if j%2 == 0]
    print(nowa_lista)

#Zadanie 3
def zad3():
    produkty = {'jajka': 7, 'maka': '3kg', 'bulki': 5, 'cukier': '1kg'}
    lista = []

#Zadanie 4
def zad4():
    a = int(input("Podaj dlugosc boku a: "))
    b = int(input("Podaj dlugosc boku b: "))
    c = int(input("Podaj dlugosc boku c: "))
    if a < c and b < c:
        if a*a+b*b==c*c:
            print("Jest to trójkąt prostokątny")
        else:
            print("Nie jest to trójkąt prostokątny")
    else:
        print("Podano złe długości")
       
#Zadanie 5
def zad5():
    a = 5
    b = 4
    h = 6
    pole = (1/2)*(a+b)*h
    print("Pole trapezu o bokach",a,"i",b,"wynosi",pole)

"""
#Zadanie 6
def zad6():
    a = 1
    b = 4
    ile = 10
    while ile > 0:
        a*=a*b
        ile-=1
    print(a)

#Zadanie 7
def zad7():
    p = int(input("Podaj liczbe: "))
    if p < 0:
        print("Blad")
    else:
        print("Pierwiastek z",p,"wynosi",p**(1/2))

"""
def main():
#    zad1()
#    zad2()
#    zad4()
#    zad5()
#    zad6()
#    zad7()
main()