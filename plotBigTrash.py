import matplotlib.pyplot as plt
import math as math
import numpy.fft as fft

def generate_data():
    xData = []
    yData = []
    for i in range(0, 100):
        xData.append(i * 0.1)
        yData.append(math.sin(i * 0.1))
    data = [xData, yData]
    return data


if __name__ == '__main__':
    data = generate_data()
    plt.plot(data[0], fft.fft(data[1]))
    plt.grid()
    plt.show()
