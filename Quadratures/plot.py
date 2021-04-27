from matplotlib import pyplot as plt

def plot(XY,  equation):
    plt.fill_between(XY[0], XY[1])
    plt.legend([
            f"Wykres funkcji f(x) w przedziale: [{min(XY[0])};{max(XY[0])}]",
        ],bbox_to_anchor=(-0.15, -0.15, 1, 0))
    plt.title(f"f(x)={equation}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show(block=True)