import matplotlib.pyplot as plt
import math as math
import numpy.fft as fft
import numpy as np
import extremaCalculator

def generate_data():
    xData = []
    yData = []
    for i in range(0, 200):
        xData.append(i * 0.1)
        yData.append(math.sin(i * 0.1) + 0.5*math.sin(i*0.3))
    data = np.asarray([xData, yData])
    return data


# amplitude of sine waves from fft is magnitude of complex vector
# phase of sine waves from fft is angle of complex vector
# divide amplitude by number of samples to get actual amplitude
# ignore all fft values above half of sampling frequency and increase amplitudes
# of remaining fft values accordingly, ie if half of fft values removed, double
# remaining amplitudes
# phase is given in terms of cosine terms
if __name__ == '__main__':
    data = generate_data()

    rfftData = fft.rfft(data[1])
    fftFrequencies = fft.rfftfreq(len(data[1]), 0.1)


    extremaIndeces = extremaCalculator.findAllExtrema(data[1])
    print(extremaIndeces)

    for i, val in enumerate(extremaIndeces[0]):
        plt.plot(data[0][val], data[1][val], 'rx')

    magnitudeArray = []
    for i in range(0, len(rfftData)):
        magnitudeArray.append(abs(rfftData[i])/len(rfftData))
    magnitudeArray = np.asarray(magnitudeArray)
#    plt.plot(fftFrequencies, magnitudeArray)
    plt.plot(data[0], data[1])

    plt.legend(['rff', 'original'])

    plt.grid()
    plt.show()
