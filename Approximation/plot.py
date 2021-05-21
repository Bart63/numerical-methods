from matplotlib import pyplot as plt

def plot(XY, App,  equation):
    plt.plot(XY[0], XY[1])
    plt.plot(App[0], App[1], '--', ms=1)
    plt.legend([
            f"Wykres funkcji f(x) w przedziale: [{min(XY[0])};{max(XY[0]):.1f}]",
            "Aproksymacja funkcji",
        ],bbox_to_anchor=(-0.15, -0.15, 1, 0))
    plt.title(f"f(x)={equation}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show(block=True)

def plot_error(errs, equation):
    plt.plot(errs)
    plt.title(f"Błąd dla aproksymacji f(x)={equation}")
    plt.grid(True)
    plt.show(block=True)