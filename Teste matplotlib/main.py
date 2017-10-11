import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0, 5, 30)
y = x*2

# Plota y vs x
fig, ax = plt.subplots(nrows=1, ncols=1)
ax.plot(x, y, color='red')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Gráfico simples da função $y=x^2$');
