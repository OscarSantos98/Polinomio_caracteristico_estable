import math
import numpy as np

validos = []
limite_sup = 100
limite_inf = -20
paso = 0.01

for k in np.arange(limite_inf,limite_sup,paso):

	coeff = [1, k*math.e**(-1)-math.e**(-1) - 1, math.e**(-1) + k*(1-2*math.e**(-1))]
	roots = np.roots(coeff)

	if np.any(roots.real >= 1) or np.any(roots.real <= -1) or np.any(roots.imag >= 1) or np.any(roots.imag <= -1):
		continue

	validos.append(k)

rango = np.array(validos)
print(f'{np.min(rango)} < k < {np.max(rango)}')