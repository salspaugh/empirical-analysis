import matplotlib.pyplot as plt

x = [0.15, 0.11, 0.06, 0.06, 0.12, 0.56]
flierprops = dict(marker='o', markerfacecolor='red', markersize=16, linestyle='none')
plt.boxplot(x, flierprops=flierprops, sym='o')
plt.show()
