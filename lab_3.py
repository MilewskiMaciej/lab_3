#Zadanie 1
def zad1():
    a = [i for i in range(1,11)]
    b = [4**j for j in range(0,8)]
    c = [k for k in b if k%2==0]
    print(a)
    print(b)
    print(c)


def main():
    zad1()

main()