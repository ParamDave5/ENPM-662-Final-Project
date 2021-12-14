import sympy as sp
import numpy as np
import math as m

def T_Matrix(DH):

    i = 0
    TList = []
    T_total = 1
        
   
    while i < 6:
        A = sp.Matrix([[sp.cos(DH[i,3]), -sp.sin(DH[i,3])*sp.cos(DH[i,0]), sp.sin(DH[i,3])*sp.sin(DH[i,0]), DH[i,1]*sp.cos(DH[i,3])],
                      [sp.sin(DH[i,3]), sp.cos(DH[i,3])*sp.cos(DH[i,0]), -sp.cos(DH[i,3])*sp.sin(DH[i,0]), DH[i,1]*sp.sin(DH[i,3])],
                      [0, sp.sin(DH[i,0]), sp.cos(DH[i,0]), DH[i,2]],
                      [0, 0, 0, 1]])
        T = sp.nsimplify(A,tolerance=1e-10,rational=True)
        T_total =  T_total * T
        TList.append(T_total)
        i += 1
        
    return T_total , TList

# vars = sp.symbols('theta_1, theta_2, theta_3, theta_4, theta_5, theta_6')

'''for all joint angles to be zero the leg stansds straight.
So the positiion of end effector i.e. the leg will be total length of all the joint lengths which is 50+150+250+150+50 = 650.
Thus putting those values in DH parameters and compution T_0_6 we should get 650 in our last column.'''


vars = sp.Matrix([0,0,0,0,0,0])
lenths = sp.Matrix([50,150,250,150,50])
# lenths = sp.symbols('a_1,a_2 ,a_3,a_4,a_5')

# DH Parameters
#                alpha ,         a ,       d , theta
DH = sp.Matrix([[m.radians(90), lenths[0], 0 , vars[0]],
               [0,              lenths[1], 0 , vars[1]],
               [0,              lenths[2], 0 , vars[2]],
               [0,              lenths[3], 0 , vars[3]],
               [m.radians(90),  lenths[4], 0 , vars[4]],
               [0,                 0,      0 , vars[5]]])

T_total, TList = T_Matrix(DH)

print(T_total)
# co-ordinates of end effector 
print(T_total[0:3,3])