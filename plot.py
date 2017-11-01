import matplotlib.pyplot as plt
import numpy as np

ar = np.load('rewards_trpo_Reacher2-v1.npz')
plt.plot(ar['arr_0'][1000:])
plt.title("Average rewards per episode on Reacher2-v1")
plt.show()
