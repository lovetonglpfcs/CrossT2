from random import randint
from os import system

def init(CT,N):
    for r in range(5):
        CT.append([])
        N.append([])
        for c in range(5):
            CT[r].append([])
            CT[r][c]=0
            N[r].append([])
            N[r][c]=0
    menu()
    RMAX = 0
    CMAX = 0
    
def menu():
    global Option1,Option2
    system('cls')
    print("="*55)
    print(" 0.")
    print(" 1.")
    print(" 2.")
    print(" 3.")
    print("="*55)
    Option1 = 6
    while not(Option1 > -1 and Option1) < 5:
        Option1 = int(input("Enter Option1 : "))
    Option2 = Option1
    while Option1 != 0 and (Option1 == Option2 or Option2 < 0 or Option2 > 4):
        Option2 = int(input("Enter Option2 : "))

def enter(A):
    for r in range(55):
        A.append([])
        for c in range(5):
            A[r].append([])
            #A[r][c]=int(input("Enter data : "))
            A[r][c]=randint(0,4)

def calc(CT,N):
    global Option1,Option2,RMAX,CMAX
    for r in range(55):
        ROW = A[r][Option1]
        COL = A[r][Option2]
        CT[ROW][COL]=CT[ROW][COL]+A[r][4]
        N[ROW][COL]=N[ROW][COL]+1
        if ROW > RMAX:
            RMAX = ROW
        if COL > CMAX:
            CMAX = COL
    for r in range(RMAX):
        for c in range(CMAX):
            if CT[r][c] > 0:
                CT[r][c]=CT[r][c]/N[r][c]

def report(CT):
    global RMAX,CMAX
    for r in range(RMAX):
        print("Column Headings")
        for c in range(CMAX):
            print(f"{CT[r][c]}")
        print()
           
    
#main
RMAX=0
CMAX=0
Option1 = 6
A = []
CT = []
N = []
init(CT,N)
enter(A)
while Option1 > 0:
    calc(CT,N)
    report(CT)
    init(CT,N)
print("Exit Program.")
system('cls')
