# gw-chirp-waveform

\# Gravitational-wave inspiral chirp (leading-order post-Newtonian)



A small Python program that generates the gravitational-wave "chirp" from the

inspiral of a binary black hole, using the leading-order (Newtonian quadrupole)

post-Newtonian approximation.



\## What is a chirp?

Two orbiting black holes lose energy by emitting gravitational waves, so their orbit

shrinks and they move faster. As a result both the frequency and the amplitude of the

signal rise with time, sweeping upward like a bird chirp, until the black holes merge.



\## Physics used

For component masses $m\_1$ and $m\_2$, the waveform depends on the chirp mass



$$\\mathcal{M} = \\frac{(m\_1 m\_2)^{3/5}}{(m\_1+m\_2)^{1/5}}.$$



With $\\tau$ the time remaining before coalescence, the leading-order results are



$$f\_{\\rm GW}(\\tau) = \\frac{1}{\\pi}\\left(\\frac{5}{256\\,\\tau}\\right)^{3/8}\\left(\\frac{G\\mathcal{M}}{c^3}\\right)^{-5/8},$$



$$\\Phi(\\tau) = -2\\left(\\frac{5G\\mathcal{M}}{c^3}\\right)^{-5/8}\\tau^{5/8},$$



$$h(\\tau) = \\frac{1}{r}\\left(\\frac{G\\mathcal{M}}{c^2}\\right)^{5/4}\\left(\\frac{5}{c\\,\\tau}\\right)^{1/4}\\cos\\Phi(\\tau),$$



for a face-on binary at distance $r$ (plus polarisation). The signal is stopped at the

innermost stable circular orbit (ISCO), where the approximation stops being valid:



$$f\_{\\rm ISCO} = \\frac{c^3}{6^{3/2}\\,\\pi\\,G\\,(m\_1+m\_2)}.$$



\## Parameters

\- $m\_1 = 36\\,M\_\\odot$, $m\_2 = 29\\,M\_\\odot$ (roughly GW150914)

\- Distance $r = 410$ Mpc

\- Start frequency: 20 Hz; sampling rate: 4096 Hz



Chirp mass: about 28 $M\_\\odot$. ISCO frequency: about 68 Hz.



\## Result

!\[Leading-order inspiral chirp](figures/gw\_chirp\_leading\_order.png)



The strain grows from about $5\\times10^{-22}$ to about $10^{-21}$ and the

frequency rises from 20 Hz to the ISCO frequency in about 0.8 s.



\## Limitations

\- Leading order only: no higher post-Newtonian corrections, spins, or eccentricity.

\- Inspiral only: no merger or ringdown.

\- Face-on orientation and one polarisation; no detector response or noise.

\- Source-frame masses are used with a luminosity distance, so redshift effects are ignored.

\- Meant as a learning exercise, not a data-analysis tool.

\-Internal consistency of $f(\\tau)$, $\\Phi(\\tau)$ and $h(\\tau)$ was checked numerically (relative differences below $10^{-4}$).



\## Run

Needs numpy and matplotlib. Run `python gw\_chirp.py`. The figure is saved to `figures/`.



\## Planned

Add 1PN and 2PN phase corrections and compare them with the leading-order waveform.



\## References

\- M. Maggiore, \*Gravitational Waves, Volume 1: Theory and Experiments\* (Oxford University Press, 2008).

\- B. S. Sathyaprakash and B. F. Schutz, \*Living Reviews in Relativity\* 12, 2 (2009).

\- B. P. Abbott et al. (LIGO and Virgo), \*Phys. Rev. Lett.\* 116, 061102 (2016).

