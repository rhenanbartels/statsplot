import matplotlib.pyplot as plt
plt.ion()


def dotplot(values):
    fig, ax = plt.subplots(1, 1)
    ax.plot(values, 'k.')
