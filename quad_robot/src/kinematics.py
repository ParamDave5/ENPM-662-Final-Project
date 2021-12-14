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

vars = sp.symbols('theta_1, theta_2, theta_3, theta_4, theta_5, theta_6')

lenths = sp.symbols('a_1,a_2 ,a_3,a_4,a_5')
# alpha , a , d,  theta
DH = sp.Matrix([[m.radians(90), lenths[0],           0 ,       vars[0]],
               [0,              lenths[1] ,  0 ,       vars[1]],
               [0,               lenths[2],  0          ,vars[2]],
               [0,                lenths[3], 0         ,vars[3]],
               [m.radians(90),     lenths[4],          0 ,     vars[4]],
               [0,                 0,           0 ,    vars[5]]])


def J_Matrix(T_total,TList):   
    # Initialize function variables 
    J = sp.zeros(3,len(vars))
    Z = sp.zeros(3,len(vars))
    
    h = T_total[:-1,-1]

    # Determine the Jacobian
    for i, hi in enumerate(h):
        for j, q in enumerate(vars):
            J[i,j] = sp.diff(hi, q)
            Z[:,j] = TList[j][:-1,2]
          
    
    J = sp.Matrix.vstack(J,Z)
    
    return J

T_total, TList = T_Matrix(DH)
J = J_Matrix(T_total, TList)
J = sp.simplify(J)

# print(J)
q_initial = sp.Matrix([m.radians(0),(m.radians(0)), (m.radians(0)),(m.radians(0)),(m.radians(0)),(m.radians(0))])
Ji = J.subs([(vars[0], q_initial[0]),(vars[1], q_initial[1]), (vars[2], q_initial[2]),(vars[3], q_initial[3]),(vars[4], q_initial[4]),(vars[5], q_initial[5])])

J_inv = np.linalg.pinv(J)

print(J_inv)
# print(T_total)
# # co-ordinates of end effector 
# print(T_total[0:3,3])
