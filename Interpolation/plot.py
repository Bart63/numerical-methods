from matplotlib import pyplot as plt

def plot(XY, baricentric, newton, points, equation):
    plt.plot(XY[0], XY[1])
    plt.plot(baricentric[0], baricentric[1], color="red")
    plt.plot(newton[0], newton[1], color="green")
    plt.plot(points[0], points[1], '+m', markersize=8)

    print(f"MSE: {sum([(b-n)*(b-n) for b,n in zip(baricentric[1],newton[1])])}")

    plt.legend([
            f"Wykres funkcji f(x) w przedziale: [{min(XY[0])};{max(XY[0])}]",
            "Metodą barycentryczną",
            "Metodą Newtona",
            "Węzły Czybyszewa"
        ],bbox_to_anchor=(-0.15, -0.15, 1, 0))
    plt.title(f"f(x)={equation}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show(block=True)