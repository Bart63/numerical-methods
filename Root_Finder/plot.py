from matplotlib import pyplot as plt

def plot(XY, bisection, newton, equation, pointPlot=False):
    plt.plot(XY[0], XY[1])

    if(bisection!=False):
        plt.plot(bisection[0], bisection[1], '+r', markersize=8)
    else:
        bisection=[False]

    if(newton!=False):
        plt.plot(newton[0], newton[1], 'xm', markersize=8)
        if pointPlot!=False:
            plt.scatter(pointPlot[0], pointPlot[1], s=2, color="grey")
    else:
        newton=[False]

    plt.legend([
            f"Wykres funkcji f(x) w przedziale: [{min(XY[0])};{max(XY[0])}]",
            f"Metodą bisekcji: x0={bisection[0]}",
            f"Metodą Newtona: x0={newton[0]}"
        ],bbox_to_anchor=(-0.15, -0.15, 1, 0))
    plt.title(f"f(x)={equation}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show(block=True)