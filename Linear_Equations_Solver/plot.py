from matplotlib import pyplot as plt

def plot(arr):
    plt.plot(arr)
    plt.title("Wartości błędu w kolejnych iteracjach")
    plt.grid(True)
    plt.show(block=True)