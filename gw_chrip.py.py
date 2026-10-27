import numpy as np
import matplotlib.pyplot as plt

G, c = 6.674e-11, 2.998e8
Msun, Mpc = 1.989e30, 3.086e22

m1, m2 = 36*Msun, 29*Msun
M  = m1 + m2
Mc = (m1*m2)**0.6 / M**0.2          # chirp mass
r  = 410*Mpc                        # distance
Gm = G*Mc/c**3                      # chirp mass in seconds

f_isco = c**3 / (6**1.5 * np.pi * G * M)

def tau_of_f(f):                    # time left to coalescence at frequency f
    return (5/256) * (np.pi*f)**(-8/3) * Gm**(-5/3)

tau_start, tau_end = tau_of_f(20), tau_of_f(f_isco)
fs = 4096
t   = np.arange(-tau_start, -tau_end, 1/fs)
tau = -t

f   = (1/np.pi) * (5/(256*tau))**(3/8) * Gm**(-5/8)
Phi = -2 * (5*Gm)**(-5/8) * tau**(5/8)
h   = (1/r) * (G*Mc/c**2)**(5/4) * (5/(c*tau))**(1/4) * np.cos(Phi)

fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(t, h);  ax[0].set_ylabel("h(t)")
ax[1].plot(t, f);  ax[1].set_ylabel("f [Hz]"); ax[1].set_xlabel("t [s]")
plt.show()
from pathlib import Path
out = Path(__file__).parent / "figures"
out.mkdir(exist_ok=True)
plt.savefig(out / "gw_chirp_leading_order.png", dpi=200, bbox_inches="tight")