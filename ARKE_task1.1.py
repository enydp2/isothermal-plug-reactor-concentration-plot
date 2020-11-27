
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model (C0,z):
    CA=C0[0]
    u = 0.5
    k = 0.3

    dCAdz = -2 *(CA ** 2) * k / u
    dCBdz =  k * (CA ** 2) / u
    dCCdz = 0
    return(dCAdz,dCBdz,dCCdz)

C0=[2,0,2]
z=np.linspace(0,2.4,20)
C=odeint(model,C0,z)

plt.plot(z,C[:,0],label='CA')
plt.plot(z,C[:,1], label='CB')
plt.plot(z,C[:,2],label='CC')
plt.xlabel("length")
plt.ylabel("Concentration")
plt.legend()
plt.show()