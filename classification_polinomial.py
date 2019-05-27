import numpy as np
import math
class Polinomial_Classifier:
    def __init__(self,V,C,initial_A = None,initial_B = None,initial_bias = 0):
        self.D = V.shape[1]
        if initial_A is None:
            self.A = np.zeros(self.D)
        else:
            self.A = initial_A.copy()
        if initial_B is None:
            self.B = np.zeros(self.D)
        else:
            self.B = initial_B.copy()
        self.bias = initial_bias
        self.C = C
        self.V = np.complex64(V)
        self.length = V.shape[0]
        self.flag = 1
    def predict(self,v):
        summation = 0
        d = 0
        while(d<D):
            if v[d] ==  0 : continue
            
            
            summation += self.A[d]*(v[d]**self.B[d]).real
            print(summation)
            d += 1
        return summation + self.bias
    def loss(self,c,pred):
        return (c-pred)**2
    def d_loss_Ad(self,v,c,pred,d):
       # k = -2*(c-pred)*(v[d]**self.B[d])
       # if (k.)
        return (-2*(c-pred)*(v[d]**self.B[d]).real)
    def d_loss_Bd(self,v,c,pred,d):
        if v[d] < 0:
            k = 0
        elif v[d] > 0:
            k = np.log(v[d])
        else :
            return 0
        if math.isnan(k) and self.flag :
            print(v,c,pred,d)
            self.flag -= 1
        return self.A[d]*k*self.d_loss_Ad(v,c,pred,d)
    def d_loss_bias(self,c,pred):
        return -2*(c-pred)

    def total_loss(self,P):
        summation = 0
        i = 0
        while (i<self.length):
            summation += self.loss(self.C[i],P[i])
            i += 1
        return summation
    def d_total_loss_Ad(self,P,d):
        summation = 0
        i = 0
        while (i<self.length):
            summation += self.d_loss_Ad(self.V[i],self.C[i],P[i],d)
            i += 1
        return summation
    def d_total_loss_Bd(self,P,d):
        summation = 0
        i = 0
        while (i<self.length):
            summation += self.d_loss_Bd(self.V[i],self.C[i],P[i],d)
            i += 1
        return summation
    def d_total_loss_bias(self,P):
        summation = 0
        i = 0
        while(i<self.length):
            summation += self.d_loss_bias(self.C[i],P[i])
            i += 1
        return summation
    def train(self,epochs,threshold,learning_rate):
        epoch = 0
        P = [self.predict(v) for v in self.V]
        E = self.total_loss(P)
        while (epoch < epochs and E >= threshold):
            d = 0
            while (d<D):
                A[d]-= learning_rate*self.d_total_loss_Ad(P,d)
                P = [self.predict(v) for v in self.V]
                B[d]-= learning_rate*self.d_total_loss_Bd(P,d)
                P = [self.predict(v) for v in self.V]
                bias -= learning_rate*self.d_total_loss_bias(P)
                P = [self.predict(v) for v in self.V]
                d += 1

            E = self.total_loss(self.C,P)
            epoch += 1

