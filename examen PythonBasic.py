
def llegir_llista_enters():
    l=[]
    while True:
        n=input("Introdueix un element: ")
        if n==".":
            break
        else:
            l.append(int(n))
    return l

def senars_llista(llista):
    ls=[]
    for i in llista:
        if i%2 != 0:
            ls.append(i)
    return ls

def sumar_parells_llista(llista):
    np=0
    for i in llista:
        if i%2==0:
            np+=i
    return np

def cercar_numero_llista(llista,numero):
    if numero in llista:
        for p,e in enumerate(llista):
            if numero==e:
                return p
    else:
        return -1

def llegir_llista_paraules():
    l=[]
    while True:
        p=input("Introdueix una paraula: ")
        if p==".":
            break
        else:
            l.append(p)
    return l

def crear_paraula_llista(llista):
    pl=""
    for i in llista:
        pl+=i[0]
    return pl

import random
def crear_llista_num_aletoris():
    l=[]
    for i in range(5):
        l.append(random.randint(1,100))
    return l

def comparar_llistes(llista1,llista2):
    l=[]
    for p,e in enumerate(llista1):
        if e in llista2:
            if e==llista2[p]:
                l.append(2)
            else:
                l.append(1)
        else:
            l.append(0)
    return l

def majors_edat(edat1,edat2):
    if edat1>18 and edat2>18:
        return f"{edat1} i {edat2} són majos d'edat"
    elif edat1>18 and edat2<18:
        return f"{edat1} és majors d'edat i {edat2} és menor d'edat"
    elif edat1<18 and edat2>18:
        return f"{edat1} és menor d'edat i {edat2} és major d'edat"
    else:
        return f"{edat1} i {edat2} són menors d'edat"

def menu():
    print("1- llegir llista de enters")
    print("2- llista de senars")
    print("3- sumar llista de parells")
    print("4- cercar numero de la llista")
    print("5- llegir llista de paraules")
    print("6- crear paraula de la llista")
    print("7- crear llista de numeros aletoris")
    print("8- comparar llistes")
    print("9- majors d'edat")
    print("10-sortir")
    while True:
    
        o=int(input("Introdueix una opció: "))
        match o:
            case 1:
                llegir_llista_enters()
            case 2:
                print(senars_llista([1,2,3,4,5,6,7,8,9]))
            case 3:
                print(sumar_parells_llista([1,2,3,4,5,6,7,8,9]))
            case 4:
                print(cercar_numero_llista([1,2,3,4,5,6,7,8,9],5))
            case 5:
                llegir_llista_paraules()
            case 6:
                print(crear_paraula_llista(["hola","adios","fea","pablo","juan"]))
            case 7:
                print(crear_llista_num_aletoris())
            case 8:
                print(comparar_llistes([1,6,3,7,8],[9,4,3,1,8]))
            case 9:
                print(majors_edat(15,21))
            case 10:
                break

menu()